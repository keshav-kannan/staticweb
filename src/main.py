from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from parse import *
from blocktype import *


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


    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    print(new_nodes)

    text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_images(text))
    # [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    print(extract_markdown_links(text))
    # [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

    node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,)
    new_nodes = split_nodes_link([node])
    print(node)
    print(new_nodes)

    node = TextNode(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
        TextType.TEXT,)
    new_nodes = split_nodes_image([node])
    print(node)
    print(new_nodes)

    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    textnode = text_to_textnodes(text)
    print(textnode)
    '''
    """
    text = '''# This is a heading

This is a paragraph of text. It has some **bold** and _italic_ words inside of it.

        - This is the first list item in a list block
- This is a list item
- This is another list item

```this is code
```

>this is a quote block
>and this

1. list item 1
2. list item 2
3. list item 3
'''

    blocks = markdown_to_blocks(text)
    for block in blocks:
        print(block,block_to_block_type(block))
"""
    md = """
#This is a heading

This is **bolded** paragraph
text in a p
tag here

## This is a second heading

This is another paragraph with _italic_ text and `code` here

"""

    node = markdown_to_html_node(md)
    html = node.to_html()
    print(html)


main()
