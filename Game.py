from wizard import Wizard

name = input("Enter name : ")
spell = input("Enter spell: ")

wizard1 = Wizard(name, spell)

# print(wizard1.name)
# print(wizard2.name)

wizard1.cast_spell()
wizard1.cast_spell()
wizard1.cast_spell()

wizard1.meditate()

wizard1.cast_spell()
