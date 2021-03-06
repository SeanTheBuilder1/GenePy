import DNAOps
import Codon

op = DNAOps.DNAtoDNA(input("DNA leading sequence:"))
print("DNA complementary sequence: ", op)
op = DNAOps.DNAtoRNA(op)
print("mRNA (codon):", op)
op = DNAOps.RNAtoRNA(op)
op = Codon.RNADiv(op)
print("tRNA (anticodon):", op)
op = Codon.TrioToCodon(op)
print("Amino Acid Sequence:", op)
