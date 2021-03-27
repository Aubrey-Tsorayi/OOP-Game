class Wizard:
    #construtor
    def __init__(self, name, favourite_spell):
        self.name = name
        self.favourite_spell = favourite_spell
        self.spell_slots = 2
        self.exp = 0
        self.damage = 5

    def cast_spell(self):
        if self.spell_slots > 0:
            print(self.name + " casts " + self.favourite_spell)
            self.spell_slots -= 1
            self.exp += 4
        else:
            print(self.name + " is out of spell slots.")

    def meditate(self):
        print(self.name + " meditates to regain spell slot")
        self.spell_slots += 1
