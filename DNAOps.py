def DNAtoDNA(dna):
    comp = ""
    for i in dna:
        if i == 'C':
            comp = comp + 'G'
        elif i == 'G':
            comp = comp + 'C'
        elif i == 'A':
            comp = comp + 'T'
        elif i == 'T':
            comp = comp + 'A'
    return comp

def DNAtoRNA(dna):
    rna = ""
    for i in dna:
        if i == 'C':
            rna = rna + 'G'
        elif i == 'G':
            rna = rna + 'C'
        elif i == 'A':
            rna = rna + 'U'
        elif i == 'T':
            rna = rna + 'A'
    return rna

def RNAtoRNA(rna):
    newrna = ""
    for i in rna:
        if i == 'C':
            newrna = newrna + 'G'
        elif i == 'G':
            newrna = newrna + 'C'
        elif i == 'A':
            newrna = newrna + 'U'
        elif i == 'U':
            newrna = newrna + 'A'
    return newrna