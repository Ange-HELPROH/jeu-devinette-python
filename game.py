# ============================================
# FICHIER : game.py
# RÔLE    : Ici je gère toute la logique du jeu
# Auteur  : Ange TEUFACK | ECAM-EPMI 2026
# ============================================

import random           # J'importe random pour générer le nombre secret
from player import Player  # J'importe la classe Player que j'ai créée


class Game:
    # Ici je définis les 3 niveaux de difficulté dans un dictionnaire
    # Chaque niveau a : un label, une plage de nombres, et un nombre d'essais max
    DIFFICULTIES = {
        "1": {"label": "Facile",   "range": (1, 50),  "attempts": 10},
        "2": {"label": "Moyen",    "range": (1, 100), "attempts": 7},
        "3": {"label": "Difficile","range": (1, 200), "attempts": 5},
    }

    # Ici j'initialise le jeu avec le joueur en paramètre
    def __init__(self, player: Player):
        self.player = player              # Je lie le joueur à la partie
        self.secret_number = None        # Le nombre secret (pas encore choisi)
        self.max_attempts = None         # Nombre d'essais max selon difficulté
        self.num_range = None            # Plage de nombres selon difficulté
        self.difficulty_label = None     # Nom de la difficulté choisie

    # Ici j'affiche le menu et je configure la difficulté choisie par le joueur
    def choose_difficulty(self):
        print("\n" + "="*40)
        print("  CHOISISSEZ VOTRE DIFFICULTÉ")
        print("="*40)
        # J'affiche chaque niveau avec ses caractéristiques
        for key, val in self.DIFFICULTIES.items():
            r = val["range"]
            print(f"  [{key}] {val['label']:<10} "
                  f"({r[0]}-{r[1]}, {val['attempts']} essais)")
        print("="*40)

        # Je demande au joueur de choisir
        choice = input("\nVotre choix (1/2/3) : ").strip()

        # Si le choix est invalide, je mets Moyen par défaut
        if choice not in self.DIFFICULTIES:
            print("Choix invalide, difficulté Moyenne sélectionnée.")
            choice = "2"

        # J'applique la configuration choisie
        config = self.DIFFICULTIES[choice]
        self.num_range = config["range"]
        self.max_attempts = config["attempts"]
        self.difficulty_label = config["label"]

        # Je génère le nombre secret aléatoire dans la bonne plage
        self.secret_number = random.randint(*self.num_range)

    # Ici je donne un indice au joueur selon l'écart entre sa réponse et le secret
    def give_hint(self, guess: int) -> str:
        diff = abs(guess - self.secret_number)  # Je calcule l'écart

        if diff == 0:
            return "🎯 EXACT !"   # Le joueur a trouvé !

        # Je détermine si le joueur doit aller vers le haut ou le bas
        direction = "plus grand" if guess < self.secret_number else "plus petit"

        # Je choisis l'indice selon la proximité
        if diff <= 5:
            return f"🔥 Très chaud ! C'est {direction}."
        elif diff <= 15:
            return f"♨️  Chaud ! C'est {direction}."
        elif diff <= 30:
            return f"😐 Tiède... C'est {direction}."
        else:
            return f"🧊 Froid ! C'est {direction}."

    # Ici je lance et gère une manche complète du jeu
    def play_round(self):
        self.choose_difficulty()   # Je demande d'abord la difficulté

        print(f"\n🎮 Devinez un nombre entre "
              f"{self.num_range[0]} et {self.num_range[1]}")
        print(f"   Vous avez {self.max_attempts} essais. Bonne chance !\n")

        attempts = 0    # Je commence le compteur d'essais à 0
        won = False     # Je suppose que le joueur n'a pas encore gagné

        # Je boucle tant que le joueur a des essais restants
        while attempts < self.max_attempts:
            remaining = self.max_attempts - attempts
            print(f"  Essais restants : {remaining}")

            # Je récupère la réponse du joueur et je gère si c'est pas un nombre
            try:
                guess = int(input("  Votre réponse : "))
            except ValueError:
                print("  ⚠️  Entrez un nombre valide.\n")
                continue   # Je recommence la boucle sans compter l'essai

            attempts += 1              # Je compte l'essai
            hint = self.give_hint(guess)  # Je calcule l'indice
            print(f"  {hint}\n")       # J'affiche l'indice

            # Si le joueur a trouvé, je sors de la boucle
            if guess == self.secret_number:
                won = True
                break

        # Ici je gère la fin de partie : victoire ou défaite
        if won:
            points = self.player.add_win(attempts, self.max_attempts)
            print("="*40)
            print(f"  ✅ GAGNÉ en {attempts} essai(s) !")
            print(f"  +{points} points remportés !")
            print("="*40)
        else:
            self.player.add_loss()
            print("="*40)
            print(f"  ❌ PERDU ! Le nombre était : {self.secret_number}")
            print("="*40)