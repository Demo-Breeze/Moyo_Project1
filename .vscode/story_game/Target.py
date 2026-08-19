from Character import Character
class Target(Character):
    def __init__(self, name, durability, strength, agility, magic_resistance, health, energy, affinity, target_type="Wizard"):
        super().__init__(name, durability, strength, agility, magic_resistance, health, energy, affinity)
        
        self.target_type = target_type  
        self.is_alive = True

    def check_status(self):
        """Checks if the target is still alive."""
        if self.health <= 0:
            self.health = 0
            self.is_alive = False
            print(f"DEFEATED: {self.name} ({self.target_type}) has been defeated!")
        else:
            print(f"STATUS: {self.name} has {self.health} health remaining.")
        return self.is_alive
target = Target("Obama",30,40,30,50,30,40,30,"Wizard")

print(target.magic_resistance)