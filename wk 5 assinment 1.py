class Superhero:
    """Base class representing a superhero"""
    
    def _init_(self, name, secret_identity, powers, weakness, power_level):
        self.name = name
        self.secret_identity = secret_identity
        self.powers = powers  # List of powers
        self.weakness = weakness
        self.power_level = power_level  # Scale of 1-100
        self.energy = 100
    
    def use_power(self, power_name):
        """Use a specific power"""
        if power_name in self.powers:
            if self.energy >= 20:
                self.energy -= 20
                return f"{self.name} uses {power_name}! Energy remaining: {self.energy}"
            else:
                return f"Not enough energy! Current energy: {self.energy}"
        else:
            return f"{self.name} doesn't have the power: {power_name}"
    
    def rest(self):
        """Rest to regain energy"""
        self.energy = min(100, self.energy + 30)
        return f"{self.name} rests. Energy restored to: {self.energy}"
    
    def is_strong_against(self, villain):
        """Check if hero is strong against a villain's power"""
        return villain.element not in self.weakness
    
    def _str_(self):
        return f"Superhero: {self.name} (Power Level: {self.power_level})"

# Inheritance layer - Specialized superhero types
class ElementalHero(Superhero):
    """A superhero with elemental powers"""
    
    def _init_(self, name, secret_identity, powers, weakness, power_level, element):
        super()._init_(name, secret_identity, powers, weakness, power_level)
        self.element = element
    
    def elemental_blast(self):
        """Special elemental attack"""
        if self.energy >= 40:
            self.energy -= 40
            return f"{self.name} unleashes {self.element} blast! 💥 Energy: {self.energy}"
        return "Not enough energy for elemental blast!"
    
    def _str_(self):
        return f"ElementalHero: {self.name} ({self.element}) - Power: {self.power_level}"

class TechHero(Superhero):
    """A superhero with technology-based powers"""
    
    def _init_(self, name, secret_identity, powers, weakness, power_level, gadgets):
        super()._init_(name, secret_identity, powers, weakness, power_level)
        self.gadgets = gadgets  # List of gadgets
        self.gadget_uses = {gadget: 3 for gadget in gadgets}  # Each gadget has 3 uses
    
    def use_gadget(self, gadget_name):
        """Use a specific gadget"""
        if gadget_name in self.gadgets and self.gadget_uses[gadget_name] > 0:
            self.gadget_uses[gadget_name] -= 1
            return f"{self.name} uses {gadget_name}! 🛠 Uses left: {self.gadget_uses[gadget_name]}"
        return f"Cannot use {gadget_name}!"
    
    def recharge_gadgets(self):
        """Recharge all gadgets"""
        for gadget in self.gadgets:
            self.gadget_uses[gadget] = 3
        return f"{self.name}'s gadgets have been recharged! ⚡"
    
    def _str_(self):
        return f"TechHero: {self.name} - Gadgets: {', '.join(self.gadgets)}"

# Demonstration
print("=== SUPERHERO DEMONSTRATION ===\n")

# Create superheroes
fire_hero = ElementalHero("Blaze", "John Smith", 
                         ["Fire Control", "Heat Resistance", "Flight"],
                         ["Water", "Ice"], 85, "Fire")

tech_hero = TechHero("Gadgeteer", "Lisa Johnson",
                    ["Hacking", "Invisibility", "Super Strength"],
                    ["EMP", "Magnets"], 75,
                    ["Grappling Hook", "Drone", "Energy Shield"])

# Test methods
print(fire_hero)
print(fire_hero.use_power("Fire Control"))
print(fire_hero.elemental_blast())
print(fire_hero.rest())
print()

print(tech_hero)
print(tech_hero.use_gadget("Drone"))
print(tech_hero.use_gadget("Grappling Hook"))
print(tech_hero.use_power("Hacking"))
print()

# Test inheritance and polymorphism
heroes = [fire_hero, tech_hero]
for hero in heroes:
    print(f"{hero.name}'s energy: {hero.energy}")
    print(hero.use_power("Flight"))