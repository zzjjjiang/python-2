from .Character import Character

class Fighter(Character):
    def __repr__(self):
        return f'Fighter: {self.hit_points} hit points.'