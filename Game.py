class Wizard:
    def __init__(self, name, favourite_spell):
        self.name = name
        self.favourite_spell = favourite_spell
        self.spell_slots = 2
        self.exp = 0

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


wizard1 = Wizard("Harry Potter", "Deez Nuts")
wizard2 = Wizard("Jack Sparrow", "It's Jack Sparrow")

# print(wizard1.name)
# print(wizard2.name)

wizard1.cast_spell()
wizard1.cast_spell()
wizard1.cast_spell()

wizard1.meditate()

wizard1.cast_spell()
