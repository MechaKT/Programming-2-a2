# animals.py
# a look at object-orientated programming

class Animal():
    # CONSTRUCTOR
    def __init__(self):
        self.legs = 0
        self.hairy = False

    def talk(self):
        return "Hello."

    def eat(self, food):
        if food == "meat":
            return "Yummm. Meat."
        elif food in ["veggies", "vegetables"]:
            return "Yummmm. Vegetables."
        elif food == "poison":
            return "I'm not eating that."
        else:
            return "Poop."

dog = Animal()
dog.legs = 4
dog.hairy = True
#if dog.hairy:
#    print("bruhssh his hair yo")
print(dog.talk())
print(dog.eat("meat"))