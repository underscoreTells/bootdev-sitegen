from htmlnode import HTMLNode
from typing import Optional, List, Dict, override


class ParentNode(HTMLNode):
    def __init__(
        self,
        tag: str,
        children: List[HTMLNode],
        props: Optional[Dict[str, str]] = None,
    ) -> None:
        super().__init__(tag, children, props)

    @override
    def to_html(self) -> str:
        if self.tag is None or self.tag == "":
            raise ValueError("all parent nodes need to contain a tag to format in HTML")

        if self.children is None:
            raise ValueError(
                "all parent nodes must contain a children list to format in HTML"
            )

        opening_tag = (
            f"<{self.tag}{self.props_to_html()}>"
            if self.props is not None
            else f"<{self.tag}>"
        )
        closing_tag = f"</{self.tag}>"
        body = ""
        for child in self.children:
            body = f"{child.to_html()}"

        return f"{opening_tag}{body}{closing_tag}"
