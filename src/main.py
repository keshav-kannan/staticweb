from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from parse import *


def main():
    #text1 = TextNode("This is some anchor text", TextType.LINK, "https://www.boot.dev")
    #print(text1)
    '''
    html1 = HTMLNode("a","link text",["h2","p"],{"href": "https://www.google.com","target": "_blank",})
    html2 = HTMLNode("h1","this is a heading",["a"],)
    html3 = LeafNode("p","this is a paragraph",{})
    print(html3)
    print(html3.to_html())
    node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(type(node.to_html())

    node = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ], )

    print(node.to_html())

    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    print(html_node)
    '''

    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    print(new_nodes)

main()
