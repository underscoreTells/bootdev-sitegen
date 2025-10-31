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
        for char in node.text:
            if char == delimiter:
                type = text_type if in_delimited_text else TextType.TEXT
                return_nodes.append(TextNode(buffer, type))
                buffer = ""
                in_delimited_text = not in_delimited_text
                continue

            buffer += char

        type = text_type if in_delimited_text else TextType.TEXT
        return_nodes.append(TextNode(buffer, type))

    return return_nodes
