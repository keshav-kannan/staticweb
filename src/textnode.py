from enum import Enum
from htmlnode import *

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def  __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

def text_node_to_html_node(text_node):
    match text_node.text_type.value:
        case "text":
            return LeafNode(None,text_node.text, None)
        case "bold":
            return LeafNode("b",text_node.text,None)
        case "italic":
            return LeafNode("i",text_node.text,None)
        case "code":
            return LeafNode("code",text_node.text)
        case "link":
            return LeafNode("a",text_node.value,{href:"",})
        case "image":
            return LeafNode("img","",{src:"www.com",alt:"some text"})
        case _:
            raise Exception("not a valid TextType")
