from __future__ import annotations
from typing import List, Dict, Optional


class HTMLNode:
    def __init__(
        self,
        tag: Optional[str] = None,
        children: Optional[List[HTMLNode]] = None,
        value: Optional[str] = None,
        props: Optional[Dict[str, str]] = None,
    ) -> None:
        self.tag = tag
        self.children = children
        self.value = value
        self.props = props

    def to_html(self) -> None:
        raise NotImplementedError("children classes need to implement this method")

    def props_to_html(self) -> str:
        if self.props is None:
            return ""

        string_return = ""
        for key in self.props:
            string_return = f" {string_return} {key}={self.props[key]}"
        return string_return

    def __repr__(self) -> str:
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props_to_html()})"
