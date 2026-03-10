# ============================================
# Classe : Player
# Auteur  : Ange TEUFACK | ECAM-EPMI 2026
# Rôle    : Gérer les données du joueur
# ============================================

class Player:
    def __init__(self, name: str):
        self.name = name
        self.score = 0
        self.total_games = 0
        self.wins = 0

    def add_win(self, attempts: int, max_attempts: int):
        """Calcule et ajoute les points selon la performance."""
        points = max(10, (max_attempts - attempts + 1) * 10)
        self.score += points
        self.wins += 1
        self.total_games += 1
        return points

    def add_loss(self):
        """Enregistre une défaite."""
        self.total_games += 1

    def get_stats(self) -> str:
        """Retourne les statistiques du joueur."""
        ratio = (self.wins / self.total_games * 100) if self.total_games > 0 else 0
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