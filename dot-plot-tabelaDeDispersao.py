'''
Função que retorna o dot-plot de duas sequências, utilizando tabela de dispersão.

Disciplina: Ferramentas para análise de sequências.
'''

#retorna lista com as palavras de tamanho k
def sub_sequence(sequence, length):
	sub_seq = []
	for i, item in enumerate(sequence):
		sub_seq.append(sequenceA[i : i+int(length)])
		if(i+int(length) == len(sequenceA)):
		  break

	return sub_seq

#retorna a tabela de dispersão, contendo a posição de ocorrência de cada palavra na sequência
def hashTable(sub_sequenceA):
	seq_dic = {}
	for i, item in enumerate(sub_sequenceA):
		seq_dic.setdefault(item, [])
		seq_dic[item].append(i)
    
	return seq_dic


def dotplot(sequenceA, sequenceB, k):
	sub_seqA = sub_sequence(sequenceA, k)
	tableA = hashTable(sub_seqA)
	sub_seqB = sub_sequence(sequenceB, k)
	print(" \n")
	print(sub_seqB)
	aa =''
	for i in tableA:
		aa += i + " "
		for j in sub_seqB:			
			if i == j:
				aa += "#"
			else:
				aa += "."
		aa+='\n'
	print(aa)	


sequenceA = input()
sequenceB = input()
k = input()
dotplot(sequenceA, sequenceB, k)

