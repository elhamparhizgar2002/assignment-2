#ex8


import io
from Bio import Phylo
import sys

file_path = 'rosalind_nkew.txt'  # replace with your file path
with open(file_path, 'r') as file:
    pairs_data = [i.split('\n') for i in file.read().strip().split('\n\n')]

for i, pair_line in pairs_data:
    x, y = pair_line.split()
    tree = Phylo.read(io.StringIO(i), 'newick')
    sys.stdout.write('%s' % round(tree.distance(x, y)) + ' ')

sys.stdout.write('\n')
