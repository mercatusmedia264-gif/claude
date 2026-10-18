"""Témoignage : voix telle quelle + SFX discrets, PAS de musique.
Master -14 LUFS / -1 dBTP vérifié après encodage AAC 320 kb/s.
usage : python mix.py renders/final.mp4 out/CREA_temoignage_4K.mp4"""
import json, re, subprocess, sys

VIDEO, OUT = sys.argv[1], sys.argv[2]
cfg = json.load(open("cues.json")); DUR = cfg["dur"]

def lufs(path, extra=""):
    p = subprocess.run(["ffmpeg", "-nostats", "-i", path, "-af", f"{extra}ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", p)[-1]), float(re.findall(r"Peak:\s+(-?[\d.]+) dBFS", p)[-1])

v_lufs, _ = lufs("assets/voice.wav")
inputs = ["-i", "assets/voice.wav"]
fc = [f"[0:a]highpass=f=70,apad,atrim=0:{DUR}[v]"]
labels = ["[v]"]
for k, (name, t, db) in enumerate(cfg["cues"]):
    inputs += ["-i", f"assets/sfx/{name}.wav"]
    g = 10 ** ((v_lufs - 3 + db) / 20)
    ms = max(0, int(t * 1000))
    fc.append(f"[{k + 1}:a]volume={g:.4f},adelay={ms}|{ms}[s{k}]"); labels.append(f"[s{k}]")
fc.append(f"{''.join(labels)}amix=inputs={len(labels)}:duration=first:normalize=0,atrim=0:{DUR}[mix]")
subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", "[mix]",
                "-ar", "48000", "renders/mix.wav"], check=True, timeout=600)

i, _ = lufs("renders/mix.wav")
gain = -14 - i; ceil = -1.2
for _ in range(4):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", "renders/mix.wav", "-af",
                    f"volume={gain:.2f}dB,alimiter=limit={10 ** (ceil / 20):.4f}:attack=3:release=60:level=disabled",
                    "-c:a", "aac", "-b:a", "320k", "-ar", "48000", "renders/master.m4a"], check=True)
    i2, tp = lufs("renders/master.m4a", "aresample=192000,")
    print(f"master: {i2:.2f} LUFS, true peak {tp:.2f} dBTP")
    if tp <= -1.0 and abs(i2 + 14) <= 0.5: break
    if tp > -1.0: ceil -= 0.4
    gain += -14 - i2
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", VIDEO, "-i", "renders/master.m4a", "-map", "0:v", "-map", "1:a",
                "-c:v", "copy", "-c:a", "copy", "-shortest", "-movflags", "+faststart", OUT], check=True)
print("→", OUT)
