# __________________________Declarations y'ama variables____________________________________
#  ----------------------variables ziri simples----------------------------------------
igiharuro = 7
imyaka = 25
nyagakwabu = 8.9976
ijambo = "J'ai de la chance"

# --------------------Variables ziri composEs-------------------------------------
urutonde = [2, 6, 8] # (list)
kazinduzi = {
	"nom": "tom",
	"prenom": "jerry",
	"age": 12,
	"poids": 79.7,
} # (dictionary) cank dict(muri python)

#____________________________ Gu-afficha____________________________________
print(f"je mfise imyaka {imyaka}") # nimba ushaka gu-afficha variables hamwe n'amajambo
print(kazinduzi["nom"]) # gutora no ku-afficha valeur ya nom iri muri kazinduzi
print(urutonde[2]) # gutora no ku-afficha ikintu kigira kabiri mu rutonde 
print(igiharuro) # ku-afficha variable yitwa igiharuro

# ________________________________ ama boucle _____________________________________________
# ------------------------------boucle while--------------------------------------------
# =====================guharura de 0 a 5 (ariko igarukira kuri 4 kubera twakoresheje "<" twarigukoresha "<=" )
i = 0 # aho boucle iza gutangirira
while(i<5): # igarukira kuri  5
	print(f"muri boucle while {i}")
	i = i+1 # iza irasimba igiharuro kimwe kimwe (incrementation)


# --------------------------boucle for ----------------------------------------------
for x in range(5):
	print(f"muri boucle for {x}")

# __________________________________Exercices_______________________________________________
abanyeshure = ["bob", "honoris", "thyerry", "jamse", "rambo", "nestor", "milly"]

# ====================== ku afficha abanyeshure
for umunyeshure in abanyeshure:
	print(umunyeshure)

# =================== ku afficha ibirimo muri kazinduzi (dictionnaire)
for key, value in kazinduzi.items():
	print(f"{key} = {value}")




# +++++++++++++++++++++++++++++ama functions akoreshwa cane mu ma listes yo muri python
# ============= function index (gutora position yikintu kiri muri list)
x = abanyeshure.index("thyerry")

# ============ function len (gutora ukwo list ingana)
y = len(abanyeshure)

print(x, y)