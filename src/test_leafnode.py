import unittest
from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_no_value(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)

    def test_empty_value(self):
        node = LeafNode("p", "")
        self.assertRaises(ValueError, node.to_html)

    def test_no_tag(self):
        value = "some value"
        node = LeafNode(None, value)
        self.assertEqual(value, node.to_html())

    def test_empty_tag(self):
        value = "some value"
        node = LeafNode("", value)
        self.assertEqual(value, node.to_html())
