from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from parse import *
from blocktype import *
from buildfunc import *

def main():
    #from_path = "/home/keshav/workspace/github.com/staticweb/content/index.md"
    #dest_path = "/home/keshav/workspace/github.com/staticweb/public/index.html"
    dir_path_content = "/home/keshav/workspace/github.com/staticweb/content/"
    template_path = "/home/keshav/workspace/github.com/staticweb/template.html"
    dest_dir_path = "/home/keshav/workspace/github.com/staticweb/public/"

    #Clear the public folder and copy static files to public
    copy_static_to_public()
    #Generate all html pages from md
    generate_page_recursive(dir_path_content,template_path, dest_dir_path)


main()
