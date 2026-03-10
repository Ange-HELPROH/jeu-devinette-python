# ============================================
# PROJET : Jeu de Devinette - Python POO
# Auteur  : Ange TEUFACK | ECAM-EPMI 2026
# GitHub  : github.com/TON_USERNAME
# ============================================

from game import Game
from player import Player


def display_welcome():
    print("\n" + "="*40)
    print("   🎯 JEU DE DEVINETTE – PYTHON POO")
    print("   Développé par Ange TEUFACK")
    print("   ECAM-EPMI | Cycle Préparatoire")
    print("="*40)


def ask_replay() -> bool:
    answer = input("\n🔄 Rejouer ? (o/n) : ").strip().lower()
    return answer == "o"


def main():
    display_welcome()

    name = input("\nEntrez votre prénom : ").strip()
    if not name:
        name = "Joueur"

    player = Player(name)
    game = Game(player)

    print(f"\nBienvenue, {player.name} ! 🎉")

    while True:
        game.play_round()
        print(player.get_stats())
        if not ask_replay():
            break

    print(f"\n👋 Merci d'avoir joué, {player.name} !")
    print(f"   Score final : {player.score} pts\n")


if __name__ == "__main__":
    main()

### `requirements.txt`
# Aucune dépendance externe requise
# Python 3.12+ uniquement