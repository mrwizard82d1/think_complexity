import unittest

import graph


def expected_vertex_repr(label):
    return 'Vertex(label=%s)' % label


class VertexTest(unittest.TestCase):
    def test_when_labeled_then_correctly_labeled(self):
        expected_label = 'ipsum'
        cut = graph.Vertex(expected_label)
        self.assertEquals(expected_label, cut.label)
        self.assertEqual(expected_vertex_repr(expected_label), repr(cut))
        self.assertEqual(expected_vertex_repr(expected_label), str(cut))

    def test_when_unlabeled_then_correctly_unlabeled(self):
        expected_label = ''
        cut = graph.Vertex()
        self.assertEquals(expected_label, cut.label)
        self.assertEqual(expected_vertex_repr(expected_label), repr(cut))
        self.assertEqual(expected_vertex_repr(expected_label), str(cut))


def expected_edge_repr(v_label, w_label):
    return 'Edge(v=%s, w=%s)' % (expected_vertex_repr(v_label),
                                 expected_vertex_repr(w_label))


class EdgeTest(unittest.TestCase):
    def test_when_init_then_init(self):
        expect_v_label = 'dolor'
        v = graph.Vertex(expect_v_label)
        expect_w_label = 'sit'
        w = graph.Vertex(expect_w_label)
        expect_vertices = (v, w)
        cut = graph.Edge(expect_vertices)

        self.assertEqual(expect_vertices, cut.vertices())
        self.assertEqual(expected_edge_repr(expect_v_label, expect_w_label),
                         repr(cut))
        self.assertEqual(expected_edge_repr(expect_v_label, expect_w_label),
                         str(cut))


class AdjacencyListTest(unittest.TestCase):
    def setUp(self):
        self.cut = graph.AdjacencyListImpl()

    def test_when_empty_graph_then_empty(self):
        self.assertEquals(0, self.cut.order())
        self.assertEquals(0, self.cut.size())

    def test_when_add_vertex_then_vertex_no_edges(self):
        self.cut.add_vertex(graph.Vertex(1))
        self.assertEquals(1, self.cut.order())
        self.assertEqual(0, self.cut.size())

    def test_when_add_vertex_twice_then_error(self):
        vertex_label = 'lorem'
        vertex = graph.Vertex(vertex_label)
        self.cut.add_vertex(vertex)
        self.assertRaises(AssertionError, self.cut.add_vertex, vertex)

    def test_when_add_one_edge(self):
        vertices = [graph.Vertex(v) for v in [3, 5]]
        for v in vertices:
            self.cut.add_vertex(v)
        self.cut.add_edge(graph.Edge(vertices))

        self.assertEquals(len(vertices), self.cut.order())
        self.assertEquals(1, self.cut.size())

    def test_when_add_many_edges(self):
        vertices = [graph.Vertex(v) for v in [2, 3, 5, 8]]
        edges = [graph.Edge(edge) for edge in
                 [(vertices[0], w) for w in vertices[1:]]]
        self.cut = graph.AdjacencyListImpl(vertices, edges)
        self.assertEquals(len(vertices), self.cut.order())
        self.assertEquals(len(edges), self.cut.size())


class DictOfDictsTest(unittest.TestCase):

    def setUp(self):
        self.cut = graph.DictOfDictsImpl()

    def test_when_empty_graph_then_empty(self):
        self.assertEquals(0, self.cut.order())
        self.assertEquals(0, self.cut.size())

    def test_when_add_vertex_then_vertex_no_edges(self):
        self.cut.add_vertex(graph.Vertex(1))
        self.assertEquals(1, self.cut.order())
        self.assertEqual(0, self.cut.size())

    def test_when_add_vertex_twice_then_error(self):
        vertex_label = 'lorem'
        vertex = graph.Vertex(vertex_label)
        self.cut.add_vertex(vertex)
        self.assertRaises(AssertionError, self.cut.add_vertex, vertex)

    def test_when_add_one_edge(self):
        vertices = [graph.Vertex(v) for v in [3, 5]]
        for v in vertices:
            self.cut.add_vertex(v)
        self.cut.add_edge(graph.Edge(vertices))

        self.assertEquals(len(vertices), self.cut.order())
        self.assertEquals(1, self.cut.size())

    def test_when_add_many_edges(self):
        vertices = [graph.Vertex(v) for v in [2, 3, 5, 8]]
        edges = [graph.Edge(edge) for edge in
                 [(vertices[0], w) for w in vertices[1:]]]
        self.cut = graph.DictOfDictsImpl(vertices, edges)
        self.assertEquals(len(vertices), self.cut.order())
        self.assertEquals(len(edges), self.cut.size())


class Example22Test(unittest.TestCase):
    def test_find_edge(self):
        vertex_labels = ['lorem', 'ipsum', 'dolor', 'sit', 'proveniemus',
                         'augustis', 'lapi']
        vertices = [graph.Vertex(vl) for vl in vertex_labels]
        edge_indices = [(6, 4), (0, 4), (0, 3), (3, 1), (1, 5), (2, 6)]
        edges = [graph.Edge(tuple([vertices[i] for i in index_pair]))
                 for index_pair in edge_indices]
        cut_adj = graph.AdjacencyListImpl(vertices, edges)
        cut_dod = graph.DictOfDictsImpl(vertices, edges)

        self.assertEqual(edges[0].vertices(),
                         cut_adj.find_edge(vertices[6],
                                           vertices[4]).vertices())
        self.assertEqual(edges[5], cut_adj.find_edge(vertices[2], vertices[6]))
        self.assertIsNone(cut_adj.find_edge(vertices[0], vertices[5]))
        self.assertIsNone(cut_adj.find_edge(vertices[1], vertices[4]))

        self.assertEqual(edges[2], cut_dod.find_edge(vertices[3], vertices[0]))
        self.assertEqual(edges[3], cut_dod.find_edge(vertices[3], vertices[1]))
        self.assertIsNone(cut_dod.find_edge(vertices[5], vertices[0]))
        self.assertIsNone(cut_dod.find_edge(vertices[6], vertices[3]))


if __name__ == '__main__':
    unittest.main()

