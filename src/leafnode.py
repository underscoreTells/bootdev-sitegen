from htmlnode import HTMLNode
from typing import Optional, Dict, override


class LeafNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        value: str,
        props: Optional[Dict[str, str]] = None,
    ) -> None:
        super().__init__(tag=tag, value=value, children=None, props=props)

    @override
    def to_html(self) -> str:
        if self.value is None or self.value == "":
            raise ValueError("all leafnodes must have a value")

        if self.tag is None or self.tag == "":
            return self.value

        opening_tag = (
            f"<{self.tag}{self.props_to_html()}>"
            if self.props is not None
            else f"<{self.tag}>"
        )
        closing_tag = f"</{self.tag}>"

        return f"{opening_tag}{self.value}{closing_tag}"
