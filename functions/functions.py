# ama function

ub = [7, 9, 13, 11, 18, 7]
ult = [6, 13.5, 15, 7, 8]

def sum_et_moy1(l, lt): #sans valeur de retour (void)
	s = 0
	for i in l:
		s+=i
	m = s/lt
	print(m)


def sum_et_moy2(l): #avec valeur de retour (return)
	s = 0
	for i in l:
		s+=i
	m = s/len(l)
	return m

x = sum_et_moy2(ult)
print(x)