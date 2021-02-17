import numpy as np 
import random

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
    edges = set()
    permu_vertex = generate_permutation(num_vertex, base = base)
    for i in range(1, len(permu_vertex)): 
        u = permu_vertex[i]
        v = permu_vertex[random_int(0, i-1)]
        edges.add(random_swap(u, v))
    assert len(edges) == num_vertex-1
    return edges

def generate_forest(num_vertex, base = 0):
    #generate a forest (>= 1 tree graph)
    edges = set()
    permu_vertex = generate_permutation(num_vertex, base = base)
    for i in range(1, len(permu_vertex)):
        if percentage_chose(70): 
            u = permu_vertex[i]
            v = permu_vertex[random_int(0, i-1)]
            edges.add(random_swap(u, v))
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
    edges = set()
    for i in range(num_edge):
        edge = generate_edge(num_vertex, base = base)
        if duplicate == False:
            u, v = edge
            while (u, v) in edges or (v, u) in edges:
                u, v = generate_edge(num_vertex, base = base)
            edge = u, v
        edges.add(edge)
    assert len(edges) == num_edge
    return edges

def generate_connected_graph(num_vertex, num_edge, duplicate = False, base = 0):
    if duplicate == False:
        assert num_edge <= num_vertex*(num_vertex-1)/2, "number of edges must be equal or lower than number of all possible edges"
    assert num_edge >= num_vertex-1, "number of edges must be equal or greater then number of verties minus one"
    edges = generate_tree(num_vertex = num_vertex, base = base)
    for i in range(num_vertex-1, num_edge):
        edge = generate_edge(num_vertex, base = base)
        if duplicate == False:
            u, v = edge
            while (u, v) in edges or (v, u) in edges:
                u, v = generate_edge(num_vertex, base = base)
            edge = u, v
        edges.add(edge)
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
    edges = generate_forest(6)
    for u, v in edges:
        print(u, v)