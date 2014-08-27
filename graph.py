from abc import abstractmethod


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


class ImplBase(Graph):

    def __init__(self):
        self._impl = None

    @abstractmethod
    def add_edge(self, edge):
        pass

    @abstractmethod
    def add_vertex(self, vertex):
        pass

    def order(self):
        return len(self._impl)

    def size(self):
        return sum([len(edges) for edges in self._impl.values()]) // 2

    def init_impl(self, vertices, edges):
        for vertex in vertices:
            self.add_vertex(vertex)
        for edge in edges:
            self.add_edge(edge)


class AdjacencyListImpl(ImplBase):

    def __init__(self, vertices=[], edges=[]):
        super(AdjacencyListImpl, self).__init__()
        self._impl = {}
        self.init_impl(vertices, edges)

    def add_edge(self, edge):
        head, tail = edge.vertices()
        self._impl[head].append(tail)
        self._impl[tail].append(head)

    def add_vertex(self, vertex):
        assert vertex not in self._impl, 'Duplicate vertex.'
        self._impl[vertex] = []


class DictOfDictsImpl(ImplBase):

    def __init__(self, vertices=[], edges=[]):
        """Create a new graph with vertices and edges."""
        super(DictOfDictsImpl, self).__init__()
        self._impl = {}
        self.init_impl(vertices, edges)

    def add_vertex(self, vertex):
        assert vertex not in self._impl, "Duplicate vertex."
        self._impl[vertex] = {}

    def add_edge(self, edge):
        head, tail = edge.vertices()
        self._impl[head][tail] = edge
        self._impl[tail][head] = edge





