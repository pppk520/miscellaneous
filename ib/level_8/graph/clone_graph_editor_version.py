# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        queue = [node]
        seen = {}

        new_node = UndirectedGraphNode(node.label)
        seen[node] = new_node

        while len(queue) > 0:
            n = queue.pop(0)

            for neighbor in n.neighbors:
                if neighbor not in seen:
                    copy = UndirectedGraphNode(neighbor.label)
                    seen[neighbor] = copy
                    queue.append(neighbor)

                seen[n].neighbors.append(seen[neighbor])

        return new_node

from collections import deque    

def print_graph(node):
    q = deque()
    q.append(node)

    visited = set([])
    while len(q) > 0:
        node = q.popleft()
        if node in visited:
            continue

        print('%s %s' %(node.label, str([x.label for x in node.neighbors])))
        for neighbor in node.neighbors:
            q.append(neighbor)

        visited.add(node)


if __name__ == '__main__':
    '''
    node = UndirectedGraphNode(1)
    node1 = UndirectedGraphNode(10)
    node2 = UndirectedGraphNode(20)
    node3 = UndirectedGraphNode(30)
    node4 = UndirectedGraphNode(40)
    node.neighbors.append(node1)
    node.neighbors.append(node2)
    node2.neighbors.append(node3)
    node3.neighbors.append(node4)

    print_graph(node)
    cloned = Solution().cloneGraph(node)
    print('cloned')
    print_graph(cloned)
    print(is_same_graph(node, cloned))
    '''

    node = UndirectedGraphNode(1)
    node1 = UndirectedGraphNode(2)
    node2 = UndirectedGraphNode(3)
    node.neighbors.append(node1)
    node.neighbors.append(node2)
    node1.neighbors.append(node)
    node1.neighbors.append(node2)
    node2.neighbors.append(node)
    node2.neighbors.append(node1)

    print_graph(node)
    cloned = Solution().cloneGraph(node)
    print('cloned')
    print_graph(cloned)
#    print(is_same_graph(node, cloned))





