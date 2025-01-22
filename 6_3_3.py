class LivingBeing:
    def breathe(self):
        return "Breathing"

class Mammal(LivingBeing):
    def has_hair(self):
        return True

class Human(Mammal):
    def speak(self):
        return "Speaking"
    