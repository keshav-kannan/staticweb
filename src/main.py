from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from parse import *
from blocktype import *
from buildfunc import *

def main():
    from_path = "/home/keshav/workspace/github.com/staticweb/content/index.md"
    template_path = "/home/keshav/workspace/github.com/staticweb/template.html"
    dest_path = "/home/keshav/workspace/github.com/staticweb/public/index.html"

    copy_static_to_public()
    generate_page(from_path, template_path, dest_path)


main()
