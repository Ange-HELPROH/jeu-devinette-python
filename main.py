# ============================================
# FICHIER : main.py
# RÔLE    : C'est ici que je lance tout le jeu
# Auteur  : Ange TEUFACK | ECAM-EPMI 2026
# ============================================

from game import Game       # J'importe la logique du jeu
from player import Player   # J'importe la gestion du joueur


# Ici j'affiche le titre du jeu au démarrage
def display_welcome():
    print("\n" + "="*40)
    print("   🎯 JEU DE DEVINETTE – PYTHON POO")
    print("   Développé par Ange TEUFACK")
    print("   ECAM-EPMI | Cycle Préparatoire")
    print("="*40)


# Ici je demande au joueur s'il veut rejouer (o = oui, n = non)
def ask_replay() -> bool:
    answer = input("\n🔄 Rejouer ? (o/n) : ").strip().lower()
    return answer == "o"   # Je retourne True si le joueur tape "o"


# Ici c'est la fonction principale qui orchestre tout le jeu
def main():
    display_welcome()   # J'affiche le titre

    # Je demande le prénom du joueur
    name = input("\nEntrez votre prénom : ").strip()
    if not name:
        name = "Joueur"   # Si rien n'est tapé, je mets "Joueur" par défaut

    # Je crée les objets joueur et jeu
    player = Player(name)
    game = Game(player)

    print(f"\nBienvenue, {player.name} ! 🎉")

    # Je lance la boucle principale : on joue jusqu'à ce que le joueur arrête
    while True:
        game.play_round()          # Je lance une manche
        print(player.get_stats())  # J'affiche les stats après chaque manche
        if not ask_replay():       # Si le joueur ne veut pas rejouer, je sors
            break

    # Message de fin
    print(f"\n👋 Merci d'avoir joué, {player.name} !")
    print(f"   Score final : {player.score} pts\n")


# Ici je m'assure que le jeu se lance seulement si on exécute main.py directement
if __name__ == "__main__":
    main()