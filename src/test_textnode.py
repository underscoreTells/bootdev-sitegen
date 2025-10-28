import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node1 = TextNode("This is TextNode 1", TextType.LINK)
        node2 = TextNode("This is TextNode 2", TextType.LINK)
        self.assertNotEqual(node1, node2)

    def test_not_eq_type(self):
        node1 = TextNode("This is a TextNode", TextType.LINK)
        node2 = TextNode("This is a TextNode", TextType.BOLD)
        self.assertNotEqual(node1, node2)

    def test_none_vs_not_none_url(self):
        node1 = TextNode("This is a TextNode", TextType.LINK)
        node2 = TextNode("This is a TextNode", TextType.LINK, "https://www.someurl.com")
        self.assertNotEqual(node1, node2)

    def test_none_node(self):
        node1 = TextNode("This is a TextNode", TextType.LINK)
        node2 = None
        self.assertNotEqual(node1, node2)


if __name__ == "__main__":
    unittest.main()
