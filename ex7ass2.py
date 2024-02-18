#ex 7

import sys
from Bio import Phylo
import io


file_path = 'rosalind_nwck.txt'  
with open(file_path, 'r') as file:
    pairs_data = [i.split('\n') for i in file.read().strip().split('\n\n')]

for i, pair_line in pairs_data:
    x, y = pair_line.split()
    tree = Phylo.read(io.StringIO(i), 'newick')
    clades = tree.find_clades()

    for clade in clades:
        clade.branch_length = 1

    sys.stdout.write('%s' % tree.distance(x, y) + ' ')

sys.stdout.write('\n')
