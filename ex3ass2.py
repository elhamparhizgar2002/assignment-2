#3rd ex


num_nodes = int(input("Enter the number of nodes: "))
print("Enter the edges (i j) one per line, and 'end' to finish:")
user_edges = []
while True:
    edge_input = input().strip()
    if edge_input.lower() == 'end':
        break
    user_edges.append(tuple(map(int, edge_input.split())))

connected_subtrees = []  
nodes_with_edges = set()  
for i, j in user_edges:
    if i in nodes_with_edges or j in nodes_with_edges:
        for subtree in connected_subtrees:
            if i in subtree or j in subtree:
                connected_subtrees[connected_subtrees.index(subtree)].append(i)
                connected_subtrees[connected_subtrees.index(subtree)].append(j)
                nodes_with_edges.add(i), nodes_with_edges.add(j)
    else:
        connected_subtrees.append([i, j])
        nodes_with_edges.add(i), nodes_with_edges.add(j)

num_subtrees = len(connected_subtrees)
for i in range(num_subtrees):
    for j in range(num_subtrees):
        if i == j:
            break
        if len(set(connected_subtrees[i] + connected_subtrees[j])) < len(connected_subtrees[i]) + len(connected_subtrees[j]):
            connected_subtrees[i] = list(set(connected_subtrees[i] + connected_subtrees[j]))
            connected_subtrees[j] = []

connected_subtrees = [subtree for subtree in connected_subtrees if subtree]
final_result = (num_nodes - len(nodes_with_edges)) + len(connected_subtrees)
print("Result:", final_result)
