from Character import Character
class Human(Character):
    def __init__(self,name,durability,strength,agility,magic_resistance,health,energy,affinity):
        super().__init__(name, durability, strength, agility, magic_resistance, health, energy, affinity)

    def setup_class_skills(self):
        self.learn_skill("Sword Slash", cost=15, damage_type="Physical", base_damage=20 + (self.strength * 1.1))

    def tactical_heal(self):
        if self.energy >= 25:
            self.energy -= 25
            heal_amount = 50 * self.affinity
            self.health += heal_amount
            print(f"{self.name} used Tactical Heal! Gained {heal_amount} health. Remaining Energy = {self.energy}")
        else:
            print(f"{self.name} does not have enough energy for Tactical Heal.")