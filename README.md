# 🎯 Jeu de Devinette – Python & POO

## Description
Jeu interactif en ligne de commande développé en **Python pur**,
avec une architecture entièrement orientée objet (POO).

Le joueur doit deviner un nombre secret en un nombre limité d'essais.
Le jeu s'adapte avec des **indices dynamiques** (chaud/froid)
et un **système de score** basé sur la performance.

## Auteur
**Ange TEUFACK**
Étudiant en cycle préparatoire intégré – ECAM-EPMI (Bac+2)
Futur ingénieur spécialisé Data Science, IA & IoT

## Fonctionnalités
- 3 niveaux de difficulté (Facile / Moyen / Difficile)
- Indices dynamiques selon l'écart (🧊 froid → 🔥 très chaud)
- Système de score proportionnel aux essais utilisés
- Statistiques joueur en temps réel
- Architecture POO avec 3 classes séparées

## Lancer le projet
```bash
python main.py
```

## Aperçu
![Gameplay](gameplay1.png, gameplay2.png, gameplay3.png, gameplay4.png)

## Structure

jeu-devinette-python/
├── main.py       ← Lance le jeu
├── game.py       ← Logique et difficulté
├── player.py     ← Score et statistiques
└── README.md     ← Documentation

## Concepts démontrés
- **Classes & Objets** : Player, Game  
- **Encapsulation** : Attributs + méthodes  
- **Gestion d'erreurs** : try/except sur les inputs  
- **Logique algorithmique** : Système d'indices par écart