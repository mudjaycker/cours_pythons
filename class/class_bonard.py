class AlimentOtraco:
    def __init__(self, nom_produit, prix, date_expiration) :
        self.nom = nom_produit
        self.beyi = prix
        self.expiration = date_expiration
        self.production = date_expiration - 3
    
    def afficher(self):
        print(self.nom)
        print(self.beyi)
        print(self.expiration)
        print(self.production)

# never trust the user

ingaburo = AlimentOtraco("amata",1000, 2023)
ingaburo.afficher()

isongo = AlimentOtraco("urwarwa",5000, 2023)
isongo.afficher()
    

