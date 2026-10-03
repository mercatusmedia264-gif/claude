"""Voix (telle quelle) + musique (~10-11 dB sous la voix, montée sur la fin) + SFX,
puis master -14 LUFS / -1 dBTP vérifié après encodage AAC 320 kb/s.
usage : python mix.py renders/final.mp4 out/CREA_xxx_4K.mp4"""
import json, re, subprocess, sys

VIDEO, OUT = sys.argv[1], sys.argv[2]
cfg = json.load(open("cues.json")); DUR, END = cfg["dur"], cfg["end"]

def lufs(path, extra=""):
    p = subprocess.run(["ffmpeg", "-nostats", "-i", path, "-af", f"{extra}ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    i = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", p)[-1]); tp = float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", p)[-1])
    return i, tp

v_lufs, _ = lufs("assets/voice.wav")
m_lufs, _ = lufs("assets/music.wav", f"atrim=0:{END},")
GAP = 10.5                                       # musique sous la voix pendant la parole
m_gain = 10 ** ((v_lufs - GAP - m_lufs) / 20)
m_end = min(m_gain * 10 ** (5 / 20), 0.95)       # montée sur la fin (+5 dB)
print(f"voice {v_lufs:.1f} LUFS · music {m_lufs:.1f} LUFS → gain {m_gain:.3f}, end {m_end:.3f}")

inputs = ["-i", "assets/voice.wav", "-i", "assets/music.wav"]
# voix : morceaux du cut replacés autour des intermèdes (fondus 5 ms, rien de coupé)
import numpy as np, wave
SR = 48000
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", "assets/voice.wav", "-f", "f32le", "-ac", "2", "-ar", str(SR), "-"],
                     capture_output=True, check=True).stdout
src = np.frombuffer(raw, np.float32).reshape(-1, 2)
out = np.zeros((int(DUR * SR) + 1, 2), np.float32)
fade = int(0.005 * SR); ramp = np.linspace(0, 1, fade, dtype=np.float32)[:, None]
for a0, d, t in cfg["voice"]:
    seg = src[int(a0 * SR):int((a0 + d) * SR)].copy()
    seg[:fade] *= ramp; seg[-fade:] *= ramp[::-1]
    i0 = int(round(t * SR)); n = min(len(seg), len(out) - i0); out[i0:i0 + n] += seg[:n]
with wave.open("renders/voice_gapped.wav", "wb") as f:
    f.setnchannels(2); f.setsampwidth(2); f.setframerate(SR)
    f.writeframes((np.clip(out, -1, 1) * 32767).astype(np.int16).tobytes())
inputs[1] = "renders/voice_gapped.wav"
fc = ["[0:a]anull[v]"]
# musique : sous la voix, remontée de +5 dB pendant les intermèdes (rampes 0,3 s), montée sur la fin
boost = "+".join(f"clip(min((t-{g0 - 0.15:.3f})/0.3,({g0 + g + 0.15:.3f}-t)/0.3),0,1)" for g0, g in cfg["gaps"])
fc.append(f"[1:a]atrim=0:{DUR},volume='if(lt(t,{END - 0.3}),{m_gain:.4f}*(1+0.78*({boost})),{m_gain:.4f}+({m_end:.4f}-{m_gain:.4f})*min(1,(t-{END - 0.3})/0.6))':eval=frame,"
          f"afade=t=out:st={DUR - 0.9}:d=0.9[m]")
labels = ["[v]", "[m]"]
for k, (name, t, db) in enumerate(cfg["cues"]):
    inputs += ["-i", f"assets/sfx/{name}.wav"]
    g = 10 ** ((v_lufs - 3 + db) / 20)           # SFX normalisés crête 0.9 ≈ -3 LUFS court terme → niveau relatif voix
    ms = max(0, int(t * 1000))
    fc.append(f"[{k + 2}:a]volume={g:.4f},adelay={ms}|{ms}[s{k}]"); labels.append(f"[s{k}]")
fc.append(f"{''.join(labels)}amix=inputs={len(labels)}:duration=first:normalize=0,atrim=0:{DUR}[mix]")
subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", "[mix]",
                "-ar", "48000", "renders/mix.wav"], check=True)

# master : gain pour -14 LUFS puis limiteur -1 dBTP, vérifié après AAC
i, _ = lufs("renders/mix.wav")
gain = -14 - i; ceil = -1.2
for _ in range(4):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", "renders/mix.wav", "-af",
                    f"volume={gain:.2f}dB,alimiter=limit={10 ** (ceil / 20):.4f}:attack=3:release=60:level=disabled",
                    "-c:a", "aac", "-b:a", "320k", "-ar", "48000", "renders/master.m4a"], check=True)
    i2, tp = lufs("renders/master.m4a", "aresample=192000,")
    print(f"master: {i2:.2f} LUFS, true peak {tp:.2f} dBTP")
    if tp <= -1.0 and abs(i2 + 14) <= 0.5: break
    if tp > -1.0: ceil -= 0.3
    gain += -14 - i2
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", VIDEO, "-i", "renders/master.m4a", "-map", "0:v", "-map", "1:a",
                "-c:v", "copy", "-c:a", "copy", "-shortest", "-movflags", "+faststart", OUT], check=True)
print("→", OUT)
