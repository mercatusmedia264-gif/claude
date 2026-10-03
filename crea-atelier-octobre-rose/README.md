# CRÉA × Octobre Rose — annonce atelier bijoux

This edit follows the *Guide de montage vidéo CRÉA* (v7): glass cards for the b-rolls, liquid glass, light strokes,
word-by-word blur-in captions, eased zooms, and the cream end card (end B).

| File | Role |
|---|---|
| `build.py` | the whole edit: camera, cards, glass, strokes, captions, end card, SFX cues (`cues.json`) |
| `style.css` | CRÉA charter: colours, fonts, glass, shadows |
| `mix.py` | voice + music (~10.5 dB under the voice) + SFX, master at -14 LUFS / -1 dBTP, AAC 320 kb/s |
| `work/make_assets.py` | lens refraction maps + synthesized SFX |
| `cover/cover.html` | the cover (rendered at 4K with headless Chromium) |
| `out/legende.txt` | 5-line caption (placeholders to fill in) |

Build: put the media back in `assets/` (talk.mp4, voice.wav, music.wav, shots/*.mp4, see the top of
`build.py` for the times), then:

```bash
python build.py
npx --yes hyperframes@0.8.46 check
npx --yes hyperframes@0.8.46 render --resolution portrait-4k --fps 24 --quality high --output renders/final.mp4
python mix.py renders/final.mp4 out/CREA_atelier_octobre_rose_4K.mp4
```

The 4K master (~120 MB) is not in the repo (GitHub's limit is 100 MB); the 720p phone copy is.
