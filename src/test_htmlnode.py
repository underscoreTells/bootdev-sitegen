import unittest
from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_to_html_raises_exception(self):
        node = HTMLNode()
        self.assertRaises(NotImplementedError, node.to_html)

    def test_props_to_html_returns_empty_string_when_no_attributes(self):
        node = HTMLNode()
        prop_string = node.props_to_html()
        self.assertEqual(prop_string, "")

    def test_props_to_html(self):
        tag = "html_tag"
        value = "html_value"
        children = "html_children"
        props = {"prop1": "prop1_value", "prop2": "prop2_value"}

        node = HTMLNode(tag, children, value, props)
        test_text_string = (
            f"HTMLNode({tag}, {value}, {children}, {node.props_to_html()})"
        )
        self.assertEqual(repr(node), test_text_string)
