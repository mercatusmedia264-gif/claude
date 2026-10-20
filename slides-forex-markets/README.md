# Foreign Exchange Markets: The Price of Money — slides

Deck de 23 slides (16:9) construit à partir du document du cours *International Financial Markets* (Norhane Benazala, Wassim Sid, Adam Sam, Kamil Mohamed Ounis), dans le même design que `slides-relations-economiques/` (template « Campust »).

- **PDF final :** `Foreign-Exchange-Markets-The-Price-of-Money.pdf`
- **Source :** `source/gen.py` génère `source/fx.html` (réutilise le CSS du premier deck)

Répartition : Partie III = Kamil Mohamed Ounis, Partie IV = Adam Sam.

## Regénérer

```bash
cd source
python3 gen.py
NODE_PATH=$(npm root -g) node render.js "$PWD/fx.html" /tmp ../Foreign-Exchange-Markets-The-Price-of-Money.pdf
```

Images : Unsplash (licence Unsplash), passées en duotone bleu.
