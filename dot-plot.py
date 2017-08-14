'''
Função que retorna o dot-plot de duas sequências.

Disciplina: Ferramentas para análise de sequências.
'''

def dotplot(sequenceA, sequenceB):
	print(" \n")
	print("  " + sequenceB)
	for a in sequenceA:
		aa = a+ " "
		for b in sequenceB:
			if a == b:
				aa += "#"
			else:
				aa += "."
		aa += '\n'
		print(aa)

		
sequenceA = input()
sequenceB = input()

dotplot(sequenceA, sequenceB)
