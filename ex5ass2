ex 5




from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from collections import defaultdict

def find_corrections(fasta_file):
    sequences = defaultdict(list)
    corrections = []

    for record in SeqIO.parse(fasta_file, "fasta"):
        seq = str(record.seq)
        rev_seq = str(record.seq.reverse_complement())

        if seq in sequences:
            corrections.append(f"{seq}->{seq}")
        elif rev_seq in sequences:
            corrections.append(f"{seq}->{rev_seq}")
        else:
            sequences[seq].append(record.id)

    return corrections

fasta_file = "rosalind_corr.txt"
corrections = find_corrections(fasta_file)

for correction in corrections:
    print(correction)





  











             
