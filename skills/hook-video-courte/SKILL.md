---
name: hook-video-courte
description: 'Écrire, corriger et tester les 3 premières secondes d''une vidéo courte (reel, TikTok, short, ad), avec les frameworks de hook (Lean/Stop/Snapback, cost narration, RSV, boucle de curiosité), la banque de templates en français et en darja, les règles de texte à l''écran et la grille de correction par métriques. Utiliser ce skill dès que l''utilisateur parle de "hook", "accroche", "3 premières secondes", "première phrase", "scroll stop", "les gens scrollent", "ma vidéo fait pas de vues au début", "écris-moi le début du script", "titre de la vidéo", "texte à l''écran", "caption qui accroche", ou demande de corriger l''ouverture d''un reel ou d''une pub, même si le mot "hook" n''est pas prononcé. Il traite le hook et seulement le hook : sur un script complet ou une vidéo de A à Z, le hook d''abord ici, puis la main revient à script-video-courte pour le reste. Calibrage sur les données réelles d''un compte : grille-hooks-client. Exécution au montage : montage-vertical-court.'
---

# Hook vidéo courte

Ce skill produit les 3 premières secondes d'une vidéo courte pour **n'importe quel projet** : marque de vêtements, agence, studio, salle de sport, personal brand, pub client.

Principe directeur : **le hook ne résume pas la vidéo, il crée une dette d'attention.** Le spectateur doit ressentir qu'il lui manque une information, et que partir maintenant lui coûte quelque chose. Une phrase qui informe complètement ferme la boucle et libère le spectateur.

Deuxième principe : **un hook n'est jamais une phrase seule.** C'est trois couches simultanées (parlée, écrite, visuelle) qui doivent dire la même chose sans se répéter mot pour mot. Un excellent texte sur une frame molle ne retient personne.

**Règle d'autorité.** Ce skill contient les frameworks maison (Lean/Stop/Snapback, cost narration, RSV, boucles de curiosité, banque de templates). Ils restent la matière de travail. Mais **partout où ils divergent du standard de la formation SMM, le standard de la formation l'emporte.** Les points de divergence sont listés ci-dessous et ne se négocient pas.

### Le standard qui prime : les 4 S

Toute variante produite passe ce contrôle. Si un seul des quatre manque, la variante ne sort pas.

| S | Contrôle |
|---|---|
| **Subject** | Le sujet est nommé explicitement, dès la première ligne parlée ou le texte à l'écran |
| **Stakes** | On sait ce qu'on y gagne si on reste. C'est là que vit la dette |
| **Speed** | Compression, pas débit rapide. Ligne parlée sous 15 mots |
| **Super Clear** | Compréhensible sans effort. Aucun jeu de mots, aucune formule à décoder |

**La dette porte sur le payoff, jamais sur le sujet.** Le spectateur doit savoir en une seconde de quoi parle la vidéo. Ce qu'on lui retient, c'est la réponse, pas la question. Un hook qui cache le sujet lui-même n'est pas une dette d'attention, c'est du flou.

- "Tu vas pas croire ce qui m'est arrivé" : a une dette, échoue à Subject. **Ne sort pas.**
- "Voici comment j'ai récupéré 40 % de mes commandes annulées" : a les quatre. Sort.

### Les points de divergence tranchés

| Sujet | Ce qui s'applique |
|---|---|
| **Longueur du texte à l'écran** | **2 lignes maximum** avec une police système. Les retours à la ligne tombent là où la phrase se lit. Trois lignes uniquement avec une typographie premium et une ligne fortement mise en valeur |
| **Ponctuation du texte à l'écran** | **Aucune**, sauf guillemets et parenthèses. Pas de point final, pas de virgule, pas de point d'exclamation |
| **Mots de liaison dans le texte à l'écran** | **Interdits** : et, ou, que, mais, donc, alors. Ils allongent sans rien apporter |
| **Structure du texte à l'écran** | RÉPÉTEUR DE SUJET en majuscules + rappel de douleur, promesse de résultat ou changement d'état futur |
| **Temps d'affichage** | **Au moins 3 secondes**. Le spectateur doit lire, regarder le visage, traiter l'image et décider |
| **Placement et lisibilité du texte à l'écran** | Tiers supérieur du cadre, idéalement à un tiers de la hauteur en partant du haut, ou proche du centre. Jamais sur les yeux ni la bouche, jamais dans les zones masquées par l'interface. Police extrêmement lisible avant d'être jolie. Les valeurs exactes vivent dans `montage-vertical-court` |
| **Chiffres** | Précis, jamais approximatifs. "22 jours" et non "quelques semaines" |
| **Mots de puissance** | Des expressions compressées de 1 à 3 mots qui portent beaucoup de sens en peu de place. Elles économisent l'espace et amplifient la douleur ou le résultat |
| **Structure conditionnelle** | **"Si tu veux X, fais Y" est interdit.** Anti-motif documenté : il demande au spectateur de se qualifier avant de savoir ce qu'il gagne |
| **Questions hésitantes** | Les déclaratives assumées battent les questions. "Voici pourquoi vos vidéos ne marchent pas" et non "est-ce que vous savez pourquoi ?" |
| **Ordre d'importance des trois couches** | Texte, puis visuel, puis parlé. L'œil chasse le texte et le traite plus vite qu'une image |

### Le test d'alignement, obligatoire avant de livrer

Le désalignement des trois couches est la cause numéro un de scroll sur des vidéos qui avaient un bon sujet.

1. Couper le son et regarder les 3 premières secondes. Sait-on de quoi parle la vidéo ?
2. Fermer les yeux et écouter. Même question.
3. Lire uniquement le texte à l'écran. Même question.

Si les trois réponses ne convergent pas vers la même chose, la variante ne sort pas.

**Rappel de hiérarchie.** Le hook est deuxième ou troisième dans l'ordre de priorité, jamais premier. Le premier est l'idée : le sujet et l'angle. Un hook exceptionnel sur un sujet faible donne une vidéo médiocre. Si l'utilisateur ne sait pas répondre à la dette, le problème n'est pas le hook, c'est le sujet. Le dire et renvoyer à `banque-sujets`.

**Un hook ne sauve pas un sujet déjà vu.** Dans une niche saturée, le spectateur reconnaît en une seconde ce qu'il a déjà entendu et part. Le travail n'est alors pas de mieux formuler le même sujet, c'est de l'emballer autrement (angle neuf sur une idée connue) : `banque-sujets` §3.5.

Ne jamais écrire un hook avant d'avoir tranché §1. Un hook écrit sans cible ni promesse produit du texte générique qui marche pour tout le monde et donc pour personne.

---

## 1. Les trois décisions préalables

Trancher ces trois lignes avec l'utilisateur avant d'écrire. Si une ligne manque, la demander.

| Décision | À définir |
|---|---|
| **Cible auto-sélectionnée** | Qui doit se reconnaître dans la première seconde, et qui doit passer son chemin. Un hook qui ne repousse personne n'attire personne. |
| **Étage du funnel** | TOFU (large, découverte), MOFU (considération, preuve), BOFU (conversion, offre). Ça change complètement le type de hook (§8). |
| **La dette** | Quelle information précise est promise sans être donnée. L'écrire en une phrase avant de rédiger : "il va apprendre X, mais il ne l'a pas encore." |

Si l'utilisateur ne sait pas répondre à la dette, la vidéo n'a pas de sujet. Le problème n'est pas le hook, c'est le script. Le dire.

---

## 2. Les trois couches

Toujours livrer les trois. Elles se complètent, elles ne se doublonnent pas.

**Couche 1 : la ligne parlée (0 à 3 s)**
Phrases courtes, staccato. Une idée par phrase. Pas de "salut tout le monde", pas de "aujourd'hui je vais vous parler de", pas de respiration avant l'attaque. Le premier mot prononcé est déjà dans le sujet.

**Couche 2 : le texte à l'écran (3 à 6 mots)**
Il donne le contexte que la voix ne donne pas encore, ou il contredit la voix pour créer une tension. Jamais le sous-titre exact de ce qui est dit : c'est un gâchis d'espace et d'attention.

**Couche 3 : la première frame**
Elle doit être lisible à l'arrêt sur image. Question à se poser : si on coupe le son et qu'on fige la vidéo à 0,0 s, est-ce qu'on comprend le sujet et est-ce qu'on a envie de rester ? Une frame de visage neutre sur fond de mur blanc échoue à ce test.

Décrire cette frame en termes de contenu (ce qu'on voit, l'action en cours, le cadrage). Les paramètres d'exécution (échelle exacte, durée, position du texte au pixel, nombre d'événements par seconde) ne se décident pas ici : ils appartiennent à `montage-vertical-court`.

---

## 3. Le framework de base : Lean, Stop, Snapback

Structure en trois temps, la plus fiable pour du contenu éducatif ou d'opinion.

**Temps 1 : le lean (contexte)**
Établir le terrain commun. Le spectateur doit penser "ça me parle". Quatre entrées possibles : un point de douleur précis, un bénéfice désiré, une métaphore, un fait qui surprend.

**Temps 2 : le stop (interjection de contraste)**
Un mot qui casse la trajectoire : "sauf que", "mais", "pourtant", "sauf". En darja : "bessah", "walakine", "ama". Ce mot est le point de rupture mécanique du scroll.

**Temps 3 : le snapback (retournement)**
La phrase qui part dans la direction opposée. Plus l'écart avec le temps 1 est grand, plus le hook tient. Mais le retournement doit être **tenable** : si le reste de la vidéo ne le démontre pas, le compte perd en crédibilité et le retour de bâton se voit en commentaires.

Exemple de structure :
- Lean : "Tout le monde te dit qu'il faut poster tous les jours pour percer."
- Stop : "Sauf que"
- Snapback : "mes trois plus grosses vidéos, je les ai postées le même mois où j'ai posté le moins."

Ne pas empiler trois retournements. Un seul, propre.

---

## 4. Cost narration, version algérienne

Principe : la valeur perçue d'une information dépend du coût affiché pour l'obtenir. Une astuce devient une leçon quand on montre ce qu'elle a coûté.

**Le coût doit être réel et vérifiable.** C'est le point où la version américaine du framework ne se transpose pas : "j'ai dépensé 20 000 $ pour apprendre ça" sur un compte algérien de quelques milliers d'abonnés ne crée pas d'autorité, ça crée du doute. Le coût crédible ici se raconte en volume de travail et en résultats clients, pas en dollars.

Unités de coût qui fonctionnent sur ce marché :
- Nombre de clients gérés, de tournages livrés, de vidéos montées
- Nombre d'années sur le métier, nombre d'heures d'entraînement
- Budget publicitaire géré (en DA, et seulement si le chiffre est vrai)
- Erreurs payées cash : "j'ai perdu un client à cause de ça"
- Refus et échecs : le coût négatif est souvent plus crédible que le coût positif

**Interdit absolu** : inventer ou gonfler un chiffre. Sur un marché où tout le monde se connaît, un chiffre faux se retourne en une réponse en commentaire. Si l'utilisateur n'a pas de coût réel à afficher, utiliser une autre autorité : une source tierce, une étude, un résultat client documenté, ou aucun (un bon contrarian n'a pas besoin d'autorité).

---

## 5. Les autres structures

À choisir selon la matière disponible, pas par défaut.

**RSV (Résultat, Scène, Véhicule)**
Nommer le résultat désiré, décrire la scène de ce résultat de façon sensorielle, puis introduire le système qui y mène. Fort pour le BOFU et pour tout ce qui vend une transformation (sport, formation, service récurrent).

**Réaction à un contenu viral**
Partir d'une vidéo ou d'un fait qui tourne déjà, poser une question dessus, puis répondre avec une autorité tierce (étude, chiffre, expert). Utile quand la marque n'a pas encore d'autorité propre.

**Cult hopping (emprunt culturel)**
Emballer un sujet technique dans une référence que la cible connaît déjà : une marque, une équipe, une série, une figure connue localement. Ça crée le terrain commun en une seconde. Vérifier que la référence est réellement partagée par la cible algérienne visée, pas seulement par un public international.

**Time collapse (compression)**
"Ça m'a pris X années à comprendre, je te le donne en 30 secondes." Fonctionne seulement si le X est vrai.

**Question fermée orientée**
Une question à laquelle la cible répond "oui" mentalement. Attention : la question ouverte molle ("vous voulez plus de clients ?") est le hook le plus usé du marché. Ne l'utiliser que si la question est très spécifique à un segment.

---

## 6. Banque de templates

Les crochets sont à remplir avec le contexte du projet. Toujours réécrire pour que ça sonne comme la marque, ne jamais livrer le template brut.

**Douleur et bénéfice**
- "Si demain je repartais de [état indésirable] et que je voulais [résultat] en [durée], voilà exactement ce que je ferais."
- "Tu veux [résultat] mais tu détestes [action pénible requise]."
- "La plupart des [choses] sont mauvaises. Voilà comment rendre la tienne moins mauvaise."

**Autorité**
- "Je ne suis pas plus doué qu'un autre, mais je sais faire [action]. Voilà comment obtenir [résultat] en la faisant correctement."
- "J'ai [volume réel] derrière moi, et avant chaque [situation] je fais toujours la même chose."
- "J'ai perdu [coût réel] pour apprendre ça. Toi tu l'as gratuitement."

**Avertissement et curiosité**
- "90 % des gens ignorent ce détail sur [sujet], et c'est exactement pour ça que 90 % restent [état indésirable]."
- "Ne fais surtout pas [action courante] avant d'avoir vu ça."
- "Je déconseille ça, sauf si tu assumes d'avoir [résultat] trop vite."

**Contrarian et démontage de croyance**
- "Tout le monde te dit que [croyance courante]. Regarde ce que disent vraiment les chiffres."
- "Si tu crois encore que [croyance], c'est que personne ne t'a montré ça."

**Amorces darja (registre algérois standard)**
Pour toute production en darja, appliquer en plus le skill `darja-algerienne` : registre, translittération, marocanismes à bannir.
- "Kul wahed y9olek [croyance]. Bessah..."
- "Loukan nfiq ghedwa b [état], hadi hiya exactement wach ndir."
- "Ma tebdach [action] 9bel ma tchouf hadi."
- "Rani ndir [action] men [X] snin. W kayen ghir [X] 7wayej li vraiment y9ounou."
- "3endek [durée] bark, w nwarilek [résultat]."

---

## 7. Boucles de curiosité

La règle : **ne jamais fermer une boucle sans en ouvrir une autre.** La rétention se perd à l'endroit exact où le spectateur obtient ce qu'il était venu chercher.

Application concrète sur une vidéo de 30 à 60 s :
- 0 à 3 s : ouvrir la boucle principale
- 3 à 8 s : ouvrir une boucle secondaire ("et le troisième point est celui qui m'a coûté le plus cher")
- Fermer la secondaire au milieu, en ouvrant immédiatement la suivante
- Fermer la principale le plus tard possible, jamais avant les deux tiers de la durée

Dans un script de plus de 30 secondes, ces boucles secondaires s'écrivent comme des **relances** placées aux jointures entre les blocs, et dans un listicle juste après le point 2 : leur écriture revient à `script-video-courte` §2.1 et §2.2.

Erreur la plus fréquente : donner la réponse en seconde 5 par souci de clarté. La clarté du **sujet** doit être immédiate. La clarté de la **réponse** doit être retardée.

---

## 8. Choix du hook selon l'étage du funnel

Le type de hook n'est pas interchangeable. Un contrarian agressif en bas de funnel casse la confiance qu'on vient de construire.

| Étage | Objectif du hook | Structures adaptées | À éviter |
|---|---|---|---|
| **TOFU** | Stopper un inconnu, faire découvrir | Lean/Stop/Snapback, contrarian, cult hopping, fait surprenant | Jargon métier, nom de la marque en premier mot |
| **MOFU** | Prouver la compétence | Cost narration, coulisses, avant/après, erreur payée cash | Le retournement gratuit, la provocation |
| **BOFU** | Déclencher l'action | RSV, résultat client nommé, offre avec contrainte réelle | Le clickbait, la promesse non chiffrée |

Règle de dosage : le contrarian s'use vite. Sur une série de contenus, ne pas dépasser environ un hook contrarian sur trois. Au delà, l'audience anticipe le retournement et le mécanisme ne fonctionne plus.

---

## 9. Ce que le hook impose au montage

Ce skill décide **quoi** montrer et **quoi** écrire. Le monteur décide comment. Ce qui suit est donc une liste de contraintes à transmettre, pas une méthode d'exécution : pour les valeurs de montage (safe areas exactes, durées de plan, intervalle maximum sans événement dans la zone 0 à 3 s, paliers de punch-in, réglages de captions), appliquer `montage-vertical-court`.

Contraintes qui relèvent de l'écriture, à trancher ici :

- **3 à 6 mots maximum** pour le texte à l'écran, lisible en une seule fixation oculaire. Au delà, personne ne lit. C'est une contrainte de rédaction, pas de mise en page.
- **Le texte écran ne double jamais la ligne parlée.** Il complète ou il contredit. Un sous-titre exact de ce qui est dit gâche la seule surface d'attention disponible.
- **Un seul élément a le droit d'être gros** dans les 3 premières secondes. Si le hook écrit et un autre texte se disputent la taille, réécrire pour n'en garder qu'un.
- **Lisibilité en muet** : le hook doit fonctionner à l'écrit seul, la majorité des premiers visionnages se faisant sans son. Test : masquer la ligne parlée et relire. Si la promesse disparaît, le texte écran est mal écrit.
- **Décor intentionnel** : tout ce qui est dans le champ doit être choisi. Le désordre en arrière plan vole l'attention destinée au texte. Cette contrainte se règle au tournage, pas au montage.
- **Le hook a besoin de mouvement** : une frame totalement fixe pendant 3 secondes ne tient pas. Le hook indique quel mouvement il attend (action en cours, geste, apparition d'objet). Le calibrage du mouvement revient au montage.

Bloc à transmettre au montage, une ligne par contrainte, dans le livrable §12.

## 10. Interdits

- Ouvrir par une salutation, une présentation, ou le logo de la marque
- Promettre dans le hook ce que la vidéo ne livre pas : gain court terme, perte de compte long terme
- Inventer un chiffre, un coût, un résultat client
- Reprendre un template mot pour mot sans l'adapter à la voix de la marque
- Empiler plusieurs frameworks dans le même hook (un seul mécanisme à la fois)
- Ouvrir sur une question molle et universelle ("vous voulez gagner plus d'argent ?")
- Traduire littéralement un hook anglais : la syntaxe passe mal, ça sonne importé
- Utiliser une provocation qui touche à la religion, à la politique ou aux personnes réelles nommées

---

## 11. Mesure et correction

Ne pas juger un hook sur une vidéo. Juger sur une série, en comparant aux médianes du compte lui même, pas à des benchmarks externes qui dépendent de la niche et de la plateforme.

Indicateur à regarder : la part de spectateurs encore présents à 3 secondes, puis la courbe de rétention complète.

| Symptôme | Diagnostic | Correction |
|---|---|---|
| Chute massive avant 3 s | Le sujet n'est pas identifiable, ou la frame est illisible | Retravailler la couche visuelle et le texte à l'écran, pas la phrase. Si le texte tient déjà, le problème est au montage : passer à `montage-vertical-court`, section diagnostic. |
| Bonne accroche puis chute à 5 à 8 s | La boucle s'est fermée trop tôt, ou le corps ne tient pas la promesse | Retarder la réponse, ouvrir une boucle secondaire |
| Rétention correcte mais peu de vues | Le hook retient mais ne stoppe pas : problème de distribution initiale | Élargir le lean, rendre la première seconde plus contrastée |
| Vues élevées, engagement faible, audience hors cible | Le hook est trop large, il n'auto-sélectionne pas | Rendre la cible explicite dès le premier mot |

Quand un hook fonctionne, ne pas le rejouer à l'identique : réutiliser sa **structure**, changer l'angle.

---

## 12. Livrable attendu

Sauf demande contraire, produire **3 variantes** de hook, jamais une seule. Une seule proposition empêche l'arbitrage et le test.

Pour chaque variante, livrer ce bloc :

```
VARIANTE [n] — [nom du mécanisme utilisé]
Parlé (0-3 s) : [la ou les phrases exactes à dire]
Texte écran   : [3 à 6 mots]
Première frame: [ce qu'on voit, cadrage, action]
Dette ouverte : [l'information promise et retenue]
Contrainte montage : [le mouvement attendu, ce qui doit apparaître et quand, ce qui ne doit surtout pas être à l'écran]
Pourquoi ça marche : [une phrase, le mécanisme]
```

La ligne **Contrainte montage** est l'interface avec `montage-vertical-court` : elle se reprend telle quelle en tête de feuille de montage. Ne pas y mettre de valeurs chiffrées de montage, seulement des intentions.

Terminer par une ligne de recommandation : laquelle tester en premier et pourquoi.

Si l'utilisateur fournit un hook existant à corriger, ne pas le réécrire silencieusement : indiquer d'abord ce qui ne va pas mécaniquement (pas de dette, boucle fermée trop tôt, cible absente, coût inventé), puis proposer les variantes.

---

## 13. Chaînage avec les autres skills

Ordre canonique : **hook, puis script, puis montage, puis motion.**

**Rendre la main à `script-video-courte`** dès qu'une de ces conditions est vraie :

- L'utilisateur fournit un script complet et le problème n'est pas seulement l'ouverture
- Les variantes de hook sont validées et il reste les cinquante secondes suivantes à écrire
- La rétention chute après 3 s et non avant : le hook a fait son travail, le problème est la zone de verrouillage ou la structure
- L'utilisateur demande une vidéo de A à Z

Transmettre la variante retenue telle quelle. `script-video-courte` reprend à la zone de verrouillage, les 2 à 4 phrases qui suivent immédiatement le hook, et ne réécrit pas ce qui a été validé ici.

**Passer à `grille-hooks-client`** quand l'utilisateur dispose des hooks de ses propres publications gagnantes et perdantes, avec leurs chiffres. Ce skill-ci contient les frameworks universels ; l'autre construit une grille de notation calibrée sur les données réelles d'un compte précis. Les deux se complètent : les principes ici, le calibrage terrain là-bas.

**Rendre la main à `montage-vertical-court`** dès qu'une de ces conditions est vraie :

- L'utilisateur a des rushes et veut la vidéo montée, pas seulement le texte
- Il demande combien de temps le texte reste à l'écran, à quelle échelle, où exactement dans le cadre
- Les variantes sont validées, le script est écrit, et la question devient "et maintenant je monte comment"

Transmettre la ligne **Contrainte montage** de la variante retenue. Elle se reprend telle quelle en tête de feuille de montage. Ne pas chiffrer soi-même les durées de plan, les paliers d'échelle ou les safe areas : ces valeurs vivent dans le skill montage et changent de version indépendamment.

**Déclencher `motion-design`** uniquement si la première frame retenue exige un élément qui n'existe pas au tournage : un chiffre affiché, un carton typographique, un logo animé, un compteur. Passer d'abord par le montage pour obtenir la durée du plan, jamais directement du hook au motion.

**Appliquer `darja-algerienne`** pour toute production en darja, en plus de ce skill.

**Cas particulier, "un reel de A à Z".** Produire le hook ici, puis enchaîner sur `script-video-courte` sans attendre une relance, puis sur le montage. Ne jamais aller du hook au montage directement : il manquerait le corps de la vidéo.
