# Write your solutions for 1.5 here!
class Superheros:
    def __init__(self, name, superpower, strength):
        self.name = name
        self.superpower = superpower
        self.strength = strength 
    def print(self):
        print(self.name)
        #print(self.superpower)
        print(self.strength)
    def save_civilian (self, work):
        return self.strength - work  

Superhero_1 = Superheros("rakan", "fly", 10)
Superhero_1.print()




     