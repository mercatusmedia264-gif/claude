# Theoretical Framework of International Economic Relations — slides

Deck de 15 slides (16:9) construit à partir de `Présentation.pdf` (Norhane Benazala & Wassim Sid, International Economics), dans le style du template « Campust » : bleu roi, magenta, photos en duotone bleu, titres serif (Lora) + DM Sans.

- **PDF final :** `Theoretical-Framework-International-Economic-Relations.pdf`
- **Source :** `source/slides.html` (HTML/CSS, polices et images en local)

## Regénérer le PDF

```bash
cd source
NODE_PATH=$(npm root -g) node render.js "$PWD/slides.html" /tmp ../Theoretical-Framework-International-Economic-Relations.pdf
```

## Crédits images (CC0 / domaine public, passées en duotone)

- Port aérien, conteneurs empilés, atelier textile, vue de Bombay (Rijksmuseum), vue d'Amsterdam — rawpixel (CC0)
- Porte-conteneurs en mer — StockSnap (CC0)
- iPhone, chaîne automobile, Lica Maersk, grue de Lyttelton, Port of Melbourne — Flickr (CC0)
- Portraits d'Adam Smith et de David Ricardo (Thomas Phillips) — Wikimedia Commons (domaine public)
