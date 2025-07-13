# I stole this from an undertale python clone, will be adapting it to use for our fights

class Fight:
    def __init__(self):
        """
        Describes a Fight.
        """
        self.id = 0
        self.opponents = []
        self.rewards = []

    def opps_except(self, opp: Opp) -> [type]:
        """
        Get opponents in this Fight except the given one.
        """
        tmp = self.opponents.copy()
        try:
            tmp.remove(opp)
        except ValueError:
            pass
        tmp = [type(i) for i in tmp]
        return tmp

    def update_opps(self) -> None:
        """
        For each opponent in the Fight, tell them that they are a part of this Fight.
        """
        for i in self.opponents:
            i.fight = self

class Opp:
    def __init__(self, fight: Fight):
        """
        Describes an opponent.
        :param fight: the Fight that this opponent is a part of.
        """
        self.id = 0
        self.hp = 1
        self.max_hp = 1
        self.alive = True
        self.fight = fight
        self.attacks = []
        self.name = ''
        self.gold_on_spare = 0
        self.gold_on_kill = 0
        self.exp_on_kill = 0

"""
TOOD: define an attack and an enemy attack
"""