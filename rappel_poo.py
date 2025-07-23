
class chien:
    pass
mon_chier=chien()
type(mon_chier)

class chien:
    def __init__(self, nom,race):
        self.nom=nom
        self.race=race
mn=chien("rex","labrador")
print(mn.nom)

class Calculator:
    def __init__(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise TypeError("Les deux valeurs doivent être des nombres (int ou float).")
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def multiply(self):
        return self.a * self.b

# Création d'une instance et affichage des résultats
calc = Calculator(3, 5)
print("Addition:", calc.add())
print("Multiplication:", calc.multiply())