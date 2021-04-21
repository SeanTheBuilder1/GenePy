PHE = ['PHE', 'UUU', 'UUC']
LEU = ['LEU', 'UUA', 'UUG', 'CUU', 'CUC', 'CUA', 'CUG']
ILE = ['ILE', 'AUU', 'AUC', 'AUA']
MET = ['MET', 'AUG']
VAL = ['VAL', 'GUU', 'GUC', 'GUA', 'GUG']
SER = ['SER', 'UCU', 'UCC', 'UCA', 'UCG']
PRO = ['PRO', 'CCU', 'CCC', 'CCA', 'CCG']
THR = ['THR', 'ACU', 'ACC', 'ACA', 'ACG']
ALA = ['ALA', 'GCU', 'GCC', 'GCA', 'GCG']
TYR = ['TYR', 'UAU', 'UAC']
STOP = ['STOP', 'UAA', 'UAG', 'UGA']
HIS = ['HIS', 'CAU', 'CAC']
GLN = ['GLN', 'CAA', 'CAG']
ASN = ['ASN', 'AAU', 'AAC']
LYS = ['LYS', 'AAA', 'AAG']
ASP = ['ASP', 'GAU', 'GAC']
GLU = ['GLU', 'GAA', 'GAG']
CYS = ['CYS', 'UGU', 'UGC']
TRP = ['TRP', 'UGG', '']
ARG = ['ARG', 'CGU', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG']
SER = ['SER', 'AGU', 'AGC']
GLY = ['GLY', 'GGU', 'GGC', 'GGA', 'GGG']

ARR = [PHE, LEU, ILE, MET, VAL, SER, PRO, THR, ALA, TYR, STOP, HIS, GLN, ASN, LYS, ASP, GLU, CYS, TRP, ARG, SER, GLY]

def Loop(trio):
    for i in ARR:
        for j in range(len(i)):
            if i[j] == trio:
                return i[0]

def TrioToCodon(trio):
    codonArr = []
    for i in trio:
        codonArr.append(Loop(i))
    return codonArr


def RNADiv(rna):
    trio = []
    for i in range(int(len(rna) / 3)):
        trio.append(rna[(i * 3):(i * 3) + 3])
    return trio





