# ============================================
# FICHIER : player.py
# RÔLE    : Je crée ici la "carte d'identité" du joueur
# Auteur  : Ange TEUFACK | ECAM-EPMI 2026
# ============================================

class Player:
    # Ici je crée le joueur avec son prénom et ses stats à zéro
    def __init__(self, name: str):
        self.name = name          # Je stocke le prénom du joueur
        self.score = 0            # Score qui commence à 0
        self.total_games = 0      # Nombre total de parties jouées
        self.wins = 0             # Nombre de victoires

    # Ici j'appelle cette méthode quand le joueur a GAGNÉ
    def add_win(self, attempts: int, max_attempts: int):
        # Je calcule les points : moins t'as utilisé d'essais, plus t'as de points
        points = max(10, (max_attempts - attempts + 1) * 10)
        self.score += points      # J'ajoute les points au score total
        self.wins += 1            # J'ajoute 1 victoire
        self.total_games += 1     # J'ajoute 1 partie jouée
        return points             # Je retourne les points gagnés pour les afficher

    # Ici j'appelle cette méthode quand le joueur a PERDU
    def add_loss(self):
        self.total_games += 1     # Je compte quand même la partie

    # Ici je construis le tableau de stats à afficher en fin de partie
    def get_stats(self) -> str:
        # Je calcule le taux de victoire en pourcentage
        ratio = (self.wins / self.total_games * 100) if self.total_games > 0 else 0
        # Je retourne un bloc de texte formaté avec toutes les stats
        return (
            f"\n{'='*40}\n"
            f"  STATS DE {self.name.upper()}\n"
            f"{'='*40}\n"
            f"  Score total   : {self.score} pts\n"
            f"  Parties jouées: {self.total_games}\n"
            f"  Victoires     : {self.wins}\n"
            f"  Taux de succès: {ratio:.1f}%\n"
            f"{'='*40}"
        )