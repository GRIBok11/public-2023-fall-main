import enum
from collections import deque

class Status(enum.Enum):
    NEW = 0
    EXTRACTED = 1
    FINISHED = 2


def extract_alphabet(
        graph: dict[str, set[str]]
        ) -> list[str]:
    """
    Extract alphabet from graph
    :param graph: graph with partial order
    :return: alphabet
    """
    in_degree = {node: 0 for node in graph}
    for nodes in graph.values():
        for node in nodes:
            in_degree[node] += 1
    
    # Находим все вершины с нулевым входящим ребром
    zero_in_degree = deque([node for node, degree in in_degree.items() if degree == 0])
    
    alphabet = []
    while zero_in_degree:
        node = zero_in_degree.popleft()
        alphabet.append(node)
        
        # Уменьшаем количество входящих ребер для соседних вершин
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                zero_in_degree.append(neighbor)
    
    # Проверяем, есть ли циклы в графе
    if len(alphabet) != len(graph):
        raise ValueError("Graph has at least one cycle")
    
    return alphabet

def build_graph(
        words: list[str]
        ) -> dict[str, set[str]]:
    """
    Build graph from ordered words. Graph should contain all letters from words
    :param words: ordered words
    :return: graph
    """
    graph = {}
    
    # Инициализируем граф всеми уникальными буквами
    for word in words:
        for char in word:
            if char not in graph:
                graph[char] = set()
    
    # Строим ребра графа на основе порядка слов
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        min_length = min(len(word1), len(word2))
        for j in range(min_length):
            if word1[j] != word2[j]:
                graph[word1[j]].add(word2[j])
                break
    
    return graph

#########################
# Don't change this code
#########################

def get_alphabet(
        words: list[str]
        ) -> list[str]:
    """
    Extract alphabet from sorted words
    :param words: sorted words
    :return: alphabet
    """
    graph = build_graph(words)
    return extract_alphabet(graph)

#########################
