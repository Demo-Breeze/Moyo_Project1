from Character import Character
class Lunarian(Character):
    def __init__(self, name, durability, strength, agility, magic_resistance, health, energy, affinity):
        super().__init__(name, durability, strength, agility, magic_resistance, health, energy, affinity)
        self.flame_state = "BUFFED" 
        self.flame_rounds = 0
        self.apply_state_modifiers()
        self.setup_class_skills()

    def setup_class_skills(self):
        self.learn_skill("Imperial Flare", cost=30, damage_type="Magical", base_damage=25 * self.affinity)

    def apply_state_modifiers(self):
        if self.flame_state == "BUFFED":
            self.durability = self.base_durability * 2
            self.strength = self.base_strength * 2
            self.agility = self.base_agility * 2
            self.magic_resistance = self.base_magic_resistance * 2
            self.health += 100
        elif self.flame_state == "DEBUFFED":
            self.durability = self.base_durability / 2
            self.strength = self.base_strength / 2
            self.agility = self.base_agility / 2
            self.magic_resistance = self.base_magic_resistance / 2
            self.health -= 100
        self.setup_class_skills()

    def end_of_round_update(self):
        self.flame_rounds += 1
        if self.flame_state == "BUFFED" and self.flame_rounds >= 2:
            self.flame_state = "DEBUFFED"
            self.flame_rounds = 0
            self.apply_state_modifiers()
            print(f"{self.name}'s flame went out!")
        elif self.flame_state == "DEBUFFED" and self.flame_rounds >= 4:
            self.flame_state = "BUFFED"
            self.flame_rounds = 0
            self.apply_state_modifiers()
            print(f"{self.name}'s flame returned!")