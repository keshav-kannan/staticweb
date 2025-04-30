from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import HTMLNode, LeafNode, ParentNode
from parse import *
from blocktype import *
from buildfunc import *
import sys, os

def main():
    # Use default "/" basepath if not given as only command line argument
    if len(sys.argv) == 2:
        basepath = sys.argv[1]
    else:
        basepath = "/"

    #directories
    dir_path_content = "/home/keshav/workspace/github.com/staticweb/content/"
    template_path = "/home/keshav/workspace/github.com/staticweb/template.html"
    dest_dir_path = "/home/keshav/workspace/github.com/staticweb/docs/"

    #Clear the public folder and copy static files to docs
    source = "/home/keshav/workspace/github.com/staticweb/static/"
    dest = "/home/keshav/workspace/github.com/staticweb/docs/"
    copy_static_to_public(source,dest)

    #Generate all html pages from md
    generate_page_recursive(dir_path_content,template_path,dest_dir_path,basepath)


main()
