ex2


def read_fasta(file_path):
    sequences = []
    with open(file_path, 'r') as file:
        for record in SeqIO.parse(file, 'fasta'):
            sequences.append((record.id, str(record.seq)))
    return sequences

def overlap_graph(sequences, k):
    adjacency_list = []

    for i, (id1, s1) in enumerate(sequences):
        for j, (id2, s2) in enumerate(sequences):
            if i != j and s1[-k:] == s2[:k]:
                adjacency_list.append((id1, id2))

    return adjacency_list

# Usage
if __name__ == "__main__":
    file_path = "rosalind_grph.txt"  
    k = 3  
    sequences = read_fasta(file_path)
    overlap_edges = overlap_graph(sequences, k)

    
    for edge in overlap_edges:
        print(edge[0], edge[1])
