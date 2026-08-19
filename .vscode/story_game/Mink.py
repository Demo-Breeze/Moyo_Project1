from Character import Character
class Mink(Character):
    def __init__(self,name,durability,strength,agility,magic_resistance,health,energy,affinity):
        super().__init__(name, durability, strength, agility, magic_resistance, health, energy, affinity)

    def setup_class_skills(self):
        self.learn_skill("Electro Strike", cost=15, damage_type="Physical", base_damage=15 + self.strength)
        self.learn_skill("Sulong Dash", cost=40, damage_type="Physical", base_damage=40 + (self.agility * 1.5))