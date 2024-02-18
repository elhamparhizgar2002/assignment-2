ex4




def merge_strings(s1, s2):
    max_overlap = 0
    overlap_s1 = 0
    overlap_s2 = 0
    max_len = min(len(s1), len(s2))
    
    for i in range(1, max_len+1):
        if s1.endswith(s2[:i]):
            overlap_s1 = i
        if s2.endswith(s1[:i]):
            overlap_s2 = i
        if overlap_s1 + overlap_s2 > max_overlap:
            max_overlap = overlap_s1 + overlap_s2
            if overlap_s1 > overlap_s2:
                merged = s1 + s2[overlap_s1:]
            else:
                merged = s2 + s1[overlap_s2:]
    
    if max_overlap == 0:
        merged = s1 + s2  
    
    return merged, max_overlap

def find_shortest_superstring(strings):
    while len(strings) > 1:
        max_overlap = 0
        to_merge = (0, 1)
        for i in range(len(strings)):
            for j in range(i+1, len(strings)):
                merged, overlap = merge_strings(strings[i], strings[j])
                if overlap > max_overlap:
                    max_overlap = overlap
                    to_merge = (i, j)
                    merged_string = merged
        i, j = to_merge
        strings[j] = merged_string
        strings.pop(i)
    return strings[0]


def read_fasta_file(file_path):
    sequences = []
    with open(file_path, 'r') as file:
        sequence = ''
        for line in file:
            if line.startswith('>'):
                if sequence:
                    sequences.append(sequence)
                    sequence = ''
            else:
                sequence += line.strip()
        if sequence:
            sequences.append(sequence)
    return sequences


file_path = 'rosalind_long.txt'


input_strings = read_fasta_file(file_path)


result = find_shortest_superstring(input_strings)
print(result)
