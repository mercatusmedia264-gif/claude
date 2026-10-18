# CRÉA × Octobre Rose — testimonial (atelier bijoux)

Same edit as the announcement reel (`../crea-atelier-octobre-rose`, CRÉA v7 guide), applied to the client's
already-cut testimonial: word-by-word captions, official logo in the hook, eased zooms that hide the jump cuts,
workshop b-roll from the first video in glass cards, liquid glass, light strokes, cream end card.
**No music**: voice plus very quiet SFX, master at -14 LUFS / -1 dBTP. 30 fps (the source is 30 fps).

Build: put the media back in `assets/` (talk_s0.mp4 = testimonial at 1080×1920 30p with a 1.5 s frozen tail,
voice.wav, shots/*.mp4 from the announcement project), then:

```bash
python build.py
npx --yes hyperframes@0.8.46 render --resolution portrait-4k --fps 30 --quality high --output renders/final.mp4
python mix.py renders/final.mp4 out/CREA_temoignage_atelier_4K.mp4
```
