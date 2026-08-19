from Character import Character
class Giant(Character):
    def __init__(self,name,durability,strength,agility,magic_resistance,health,energy,affinity):
        super().__init__(name, durability, strength, agility, magic_resistance, health, energy, affinity)

    def setup_class_skills(self):
        self.learn_skill("Stomp", cost=20, damage_type="Physical", base_damage=30 + self.strength)
        self.learn_skill("Boulder Toss", cost=35, damage_type="Physical", base_damage=55 + (self.strength * 1.2))

