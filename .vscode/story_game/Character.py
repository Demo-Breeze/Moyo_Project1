import random
class Character:
    def __init__(self,name,durability,strength,agility,magic_resistance,health,energy,affinity):
        self.durability = durability
        self.name =  name
        self.strength = strength
        self.agility = agility
        self.magic_resistance = magic_resistance
        self.health = health
        self.energy = energy
        self.affinity = affinity
        self.skills = {}
        self.base_durability = durability
        self.base_strength = strength
        self.base_agility = agility
        self.base_magic_resistance = magic_resistance

    def Physical_Damage_dealt(self,damage):
        physical_damage_taken = max(1, damage - self.durability)
        if self.agility>= 30 and random.randint(1,5)== 5:
            print(f"{self.name} has dodged the attack. No damage has been dealth")
            
        else:
            self.health -= physical_damage_taken
        
            #This deals damage to character in question. Damage decreases based on how much durability char has.
            print (f"{self.name} took {physical_damage_taken}. Remaining health = {self.health}")
            
    def Magical_Damage_dealt(self,damage):
        magical_damage_taken = max(1,(damage/self.affinity)-self.magic_resistance)
        if self.agility >= 40 and random.randint(1,5)>=4 and self.affinity >=2:
            print(f"{self.name} has dodged the attack. No damage has been dealt.")
        else:
            self.health -= magical_damage_taken
            print (f"{self.name} took {magical_damage_taken}. Remaining health = {self.health}")

    def True_Damage(self,damage,target):
        true_damage = (damage+self.strength)*self.affinity
        #CANNOT BE RESISTED AGAINST< CANNOT BE DODGED MINIMUM 80% of energy if not all energy consumed
        energy_consumed = self.energy *.80
        self.energy -= energy_consumed
        print(f"{self.name} used True Damage!!! Energy Consumed = {energy_consumed}. Remaining Energy = {self.energy}")

    def Physical_Damage(self,damage,target):
        physical_damage = (damage+((self.strength/100)*damage)- target.durability)

    def Magical_Damage(self,damage,target):
        magic_damage = (damage*self.affinity)- target.magic_resistance

    def learn_skill(self, skill_name, cost, damage_type, base_damage):
        self.skills[skill_name] = {"cost": cost, "type": damage_type, "damage": base_damage}

    def cast_skill(self, skill_name, target):
        if skill_name not in self.skills:
            return False
        skill = self.skills[skill_name]
        if self.energy < skill["cost"]:
            return False
        if skill["type"] == "Physical":
            target.Physical_Damage_dealt(self.Physical_Damage(skill["damage"], target))
        elif skill["type"] == "Magical":
            target.Magical_Damage_dealt(self.Magical_Damage(skill["damage"], target))
        elif skill["type"] == "True":
            true_dmg = (skill["damage"] + self.strength) * self.affinity
            target.health -= max(1, true_dmg)
        return True
    