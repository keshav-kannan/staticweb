from textnode import TextNode, TextType
from htmlnode import HTMLNode, LeafNode, ParentNode

def text_node_to_html_node(text_node):
    import sys
    print(sys.version_info)
    x = text_node.text_type.value
    match x:
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
        raise Exception("not a valid TextType")

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
    '''
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)
    print(html_node.tag, html_node.value)

main()
