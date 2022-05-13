class Calculatrice:
    def __init__(self, premiere_valeur, seconde_valeur):
        self.premiere = premiere_valeur
        self.seconde = seconde_valeur
        self.operators = {
        "+": self.add(),
        "-": self.soustr(),
        "*": self.mult(),
        "/": self.div()
        }

    
    def add(self):
        return self.premiere + self.seconde
    
    def soustr(self):
        return self.premiere - self.seconde
    
    def mult(self):
        return self.premiere * self.seconde
    
    def div(self):
        return self.premiere / self.seconde
    
    def err(self):
        return "error"
    
    def case(self,op):
        return self.operators.get(op, self.err())


bandanya = "o"
while bandanya == "o":
    a = float(input("entrer le premier nombre => "))

    print("Koresha ibimenyetso + - * / kugira uharure")
    signe = input("entrer le signe ")

    b = float(input("entrer le second nombre => "))
    calcul = Calculatrice(a,b)
    res = calcul.case(signe)
    print(f"Reponse = {res}")

    bandanya = input("tapez o pour effectuer un nouveau calcul ou tapez une autre touche pour s'arreter la ")

print("Fin du programme")