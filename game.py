# ============================================
# Classe : Game
# Auteur  : Ange TEUFACK | ECAM-EPMI 2026
# Rôle    : Logique principale du jeu
# ============================================

import random
from player import Player


class Game:
    DIFFICULTIES = {
        "1": {"label": "Facile",  "range": (1, 50),  "attempts": 10},
        "2": {"label": "Moyen",   "range": (1, 100), "attempts": 7},
        "3": {"label": "Difficile","range": (1, 200), "attempts": 5},
    }

    def __init__(self, player: Player):
        self.player = player
        self.secret_number = None
        self.max_attempts = None
        self.num_range = None
        self.difficulty_label = None

    def choose_difficulty(self):
        """Affiche le menu et configure la difficulté."""
        print("\n" + "="*40)
        print("  CHOISISSEZ VOTRE DIFFICULTÉ")
        print("="*40)
        for key, val in self.DIFFICULTIES.items():
            r = val["range"]
            print(f"  [{key}] {val['label']:<10} "
                  f"({r[0]}-{r[1]}, {val['attempts']} essais)")
        print("="*40)

        choice = input("\nVotre choix (1/2/3) : ").strip()
        if choice not in self.DIFFICULTIES:
            print("Choix invalide, difficulté Moyenne sélectionnée.")
            choice = "2"

        config = self.DIFFICULTIES[choice]
        self.num_range = config["range"]
        self.max_attempts = config["attempts"]
        self.difficulty_label = config["label"]
        self.secret_number = random.randint(*self.num_range)

    def give_hint(self, guess: int) -> str:
        """Donne un indice précis selon l'écart."""
        diff = abs(guess - self.secret_number)
        if diff == 0:
            return "🎯 EXACT !"
        direction = "plus grand" if guess < self.secret_number else "plus petit"
        if diff <= 5:
            return f"🔥 Très chaud ! C'est {direction}."
        elif diff <= 15:
            return f"♨️  Chaud ! C'est {direction}."
        elif diff <= 30:
            return f"😐 Tiède... C'est {direction}."
        else:
            return f"🧊 Froid ! C'est {direction}."

    def play_round(self):
        """Joue une manche complète."""
        self.choose_difficulty()

        print(f"\n🎮 Devinez un nombre entre "
              f"{self.num_range[0]} et {self.num_range[1]}")
        print(f"   Vous avez {self.max_attempts} essais. Bonne chance !\n")

        attempts = 0
        won = False

        while attempts < self.max_attempts:
            remaining = self.max_attempts - attempts
            print(f"  Essais restants : {remaining}")

            try:
                guess = int(input("  Votre réponse : "))
            except ValueError:
                print("  ⚠️  Entrez un nombre valide.\n")
                continue

            attempts += 1
            hint = self.give_hint(guess)
            print(f"  {hint}\n")

            if guess == self.secret_number:
                won = True
                break

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