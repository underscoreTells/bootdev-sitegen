from textnode import TextNode, TextType
from leafnode import LeafNode
from typing import List


def text_node_to_html_node(text_node: TextNode) -> LeafNode:
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, value=text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("TextType value does not match a valid value")


def split_nodes_delimiter(
    old_nodes: List[TextNode], delimiter: str, text_type: TextType
) -> List[TextNode]:
    return_nodes = []
    for node in old_nodes:
        buffer = ""
        in_delimited_text = False
        i = 0
        while i < len(node.text):
            if (
                i <= len(node.text) - len(delimiter)
                and node.text[i : i + len(delimiter)] == delimiter
            ):
                if buffer:
                    node_type = text_type if in_delimited_text else TextType.TEXT
                    return_nodes.append(TextNode(buffer, node_type))
                    buffer = ""

                in_delimited_text = not in_delimited_text
                i += len(delimiter)
            else:
                buffer += node.text[i]
                i += 1

        if buffer:
            node_type = text_type if in_delimited_text else TextType.TEXT
            return_nodes.append(TextNode(buffer, node_type))

    return return_nodes
