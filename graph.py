class Graph(object):
    def order(self):
        raise NotImplementedError

    def size(self):
        raise NotImplementedError

    def add_vertex(self, vertex):
        raise NotImplementedError

    def add_edge(self, edge):
        raise NotImplementedError


class Vertex(object):
    def __init__(self, label=''):
        self.label = label

    def __repr__(self):
        return 'Vertex(label=%s)' % self.label


class Edge(object):
    def __init__(self, pair):
        self._vertices = pair

    def vertices(self):
        return self._vertices

    def __repr__(self):
        return 'Edge(v=%s, w=%s)' % self.vertices()


class AdjacencyListImpl(Graph):
    def __init__(self, vertices=[], edges=[]):
        self._impl = {}
        for vertex in vertices:
            self.add_vertex(vertex)
        for edge in edges:
            self.add_edge(edge)

    def add_edge(self, edge, **kwargs):
        head, tail = edge.vertices()
        self._impl[head].append(tail)
        self._impl[tail].append(head)


    def add_vertex(self, vertex):
        assert vertex not in self._impl, 'Duplicate vertex.'
        self._impl[vertex] = []

    def order(self):
        return len(self._impl)

    def size(self):
        return sum([len(edges) for edges in self._impl.values()]) // 2
  
  
