import DNAOps
import Codon

op = DNAOps.DNAtoDNA(input("What is DNA Sequence\n"))
print(op)
op = DNAOps.DNAtoRNA(op)
print(op)
op = DNAOps.RNAtoRNA(op)
op = Codon.RNADiv(op)
print(op)
op = Codon.TrioToCodon(op)
print(op)