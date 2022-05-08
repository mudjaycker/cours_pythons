dictionnaire = {
	"izina": "Butoyi",
	"amatazirano": "Tom",
	"province": "Gitega"
}

# x = dictionnaire["izina"]dictionnaire["province"]
# print(x)
# print(dictionnaire["province"])

# for k in dictionnaire:
# 	print(f"{k} ==> {dictionnaire[k]}")



for k, v in dictionnaire.items():
	print(f"{k} => {v}")