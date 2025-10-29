import unittest
from parentnode import ParentNode
from leafnode import LeafNode


class TestParentNode(unittest.TestCase):
    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_none_tag(self):
        node = ParentNode(None, [])
        self.assertRaises(ValueError, node.to_html)

    def test_empty_tag(self):
        node = ParentNode("", [])
        self.assertRaises(ValueError, node.to_html)

    def test_none_children(self):
        node = ParentNode("b", None)
        self.assertRaises(ValueError, node.to_html)
