import numpy as np 
import random

def split_array(arr, num_parts):
    #split an array into several parts
    assert num_parts > 1, "number of splited part must greater than 1"
    
    split_arr = np.array_split(np.array(arr), num_parts)

    return split_arr

def generate_permutation(len, base = 0):
    #generate a permutaion
    return np.random.permutation(len) + base

def shuffle_array(arr):
    #shuffle an array
    return np.random.permutation(arr)

def random_array(start, end, len):
    #random a len-length integer array with values between [start, end]
    return np.random.randint(start, end+1, len)

def random_float(start, end, decimal_places = 2):
    #random a float number up to x decimal places between [start, end]
    return round(random.uniform(start, end), decimal_places)

def random_int(start, end):
    #random an integer number in range [start, end]
    return np.random.randint(start, end+1)

def random_choice(arr):
    return np.random.choice(arr)

def percentage_chose(percent = 50):
    # 50% return True, else return False
    assert 0 <= percent <= 100, "percentage must in range [0, 100]"
    x = random_int(1, 100)
    if x <= percent:
        return True
    else:
        return False

def random_swap(a, b):
    if percentage_chose():
        return b, a
    return a, b

def generate_tree(num_vertex, base = 0):
    #generate a tree graph
    edges = []
    permu_vertex = generate_permutation(num_vertex, base = base)
    for i in range(1, len(permu_vertex)): 
        u = permu_vertex[i]
        v = permu_vertex[random_int(0, i-1)]
        edges.append(random_swap(u, v))
    assert len(edges) == num_vertex-1
    return edges

def generate_forest(num_vertex, base = 0):
    #generate a forest (>= 1 tree graph)
    edges = []
    permu_vertex = generate_permutation(num_vertex, base = base)
    for i in range(1, len(permu_vertex)):
        if percentage_chose(70): 
            u = permu_vertex[i]
            v = permu_vertex[random_int(0, i-1)]
            edges.append(random_swap(u, v))
    assert len(edges) <= num_vertex-1
    return edges

def generate_edge(num_vertex, base = 0):
    u = random_int(base, num_vertex-1+base)
    v = random_int(base, num_vertex-1+base)
    while v == u: #prevent from u = v
        v = random_int(base, num_vertex-1+base)
    return u, v

def generate_graph(num_vertex, num_edge, duplicate = False, base = 0):
    if duplicate == False:
        assert num_edge <= num_vertex*(num_vertex-1)/2, "number of edges must be equal or lower than number of all possible edges"
    duplicate_set = set()
    edges = []
    for i in range(num_edge):
        edge = generate_edge(num_vertex, base = base)
        if duplicate == False:
            u, v = edge
            while (u, v) in duplicate_set: #or (v, u) in duplicate_set:
                u, v = generate_edge(num_vertex, base = base)
            edge = u, v
        duplicate_set.add(edge)
        edges.append(edge)
    assert len(edges) == num_edge
    return edges

def generate_cycle_component(verties):
    edges = []
    for i in range(len(verties)):
        if i == len(verties) - 1:
            edges.append((verties[i], verties[0]))
        else:
            edges.append((verties[i], verties[i+1]))
    return edges

def generate_connected_graph(num_vertex, num_edge, duplicate = False, base = 0):
    if duplicate == False:
        assert num_edge <= num_vertex*(num_vertex-1)/2, "number of edges must be equal or lower than number of all possible edges"
    assert num_edge >= num_vertex-1, "number of edges must be equal or greater then number of verties minus one"
    edges = generate_tree(num_vertex = num_vertex, base = base)
    duplicate_set = set(edges)
    for i in range(num_vertex-1, num_edge):
        edge = generate_edge(num_vertex, base = base)
        if duplicate == False:
            u, v = edge
            while (u, v) in duplicate_set: #or (v, u) in duplicate_set:
                u, v = generate_edge(num_vertex, base = base)
            edge = u, v
        duplicate_set.add(edge)
        edges.append(edge)
    assert len(edges) == num_edge
    return edges

def add_weight_egdes(edges, start, end, integer = True):
    #add weight to edges of graph. If integer = False, random float value
    weight_edges = set()
    for u, v in edges:
        if integer:
            weight_edges.add((u, v, random_int(start, end)))
        else:
            weight_edges.add((u, v, random_float(start, end)))
    return weight_edges

if __name__ == '__main__':
    #testing
    split_arr = split_array([1, 5, 2, 4, 5], 3)
    print(random.sample([6], 1))
    for i in range(3):
        print(split_arr[i])