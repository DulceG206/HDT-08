import unittest
from Bst import Bst
from SplayTree import SplayTree


class TestTrees(unittest.TestCase):

    def test_bst_insert_search(self):
        bst = Bst()
        bst.insert(10)
        bst.insert(5)
        bst.insert(15)

        node, _ = bst.search(5)
        self.assertIsNotNone(node)
        self.assertEqual(node.valor, 5)

    def test_splay_insert_search(self):
        splay = SplayTree()
        splay.insertar(10)
        splay.insertar(5)
        splay.insertar(15)

        node, _ = splay.buscar(5)
        self.assertIsNotNone(node)
        self.assertEqual(node.valor, 5)

    def test_not_found(self):
        bst = Bst()
        bst.insert(10)

        node, _ = bst.search(99)
        self.assertIsNone(node)


if __name__ == "__main__":
    unittest.main()