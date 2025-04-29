from textnode import *
import re
from blocktype import *
from htmlnode import *

def split_nodes_delimiter(old_nodes,delimiter,text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type.value != "text":
            new_nodes.append(old_node)
        else:
            if delimiter in old_node.text:
                new_nodes_text = old_node.text.split(delimiter)
                if len(new_nodes_text)!=3:
                    raise Exception("Matching delimiter not found")
                new_nodes_array = [(new_nodes_text[0],TextType.TEXT),(new_nodes_text[1],text_type),(new_nodes_text[2],TextType.TEXT)]

                for (text,type) in new_nodes_array:
                    new_nodes.append(TextNode(text,type))
            else:
                new_nodes.append(old_node)
    return new_nodes

def extract_markdown_images(text):
    #matches = re.findall(r"!\[(.+?)\]\((.+?)\)",text)
    matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    return matches

def extract_markdown_links(text):
    #matches = re.findall(r"\[(.+?)\]\((.+?)\)",text)
    matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)",text)
    return matches

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        links = extract_markdown_links(node.text)
        if links == []:
            new_nodes.append(node)
        else:
            nodetext = node.text
            for link in links:
                sections = nodetext.split(f"[{link[0]}]({link[1]})",1)
                new_nodes.append(TextNode(sections[0],TextType.TEXT))
                new_nodes.append(TextNode(link[0],TextType.LINK,link[1]))
                nodetext = sections[-1]
            if sections[-1] != "":
                new_nodes.append(TextNode(sections[-1],TextType.TEXT))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        images = extract_markdown_images(node.text)
        if images == []:
            new_nodes.append(node)
        else:
            nodetext = node.text
            for image in images:
                sections = nodetext.split(f"![{image[0]}]({image[1]})",1)
                new_nodes.append(TextNode(sections[0],TextType.TEXT))
                new_nodes.append(TextNode(image[0],TextType.IMAGE,image[1]))
                nodetext = sections[-1]
            if sections[-1] != "":
                new_nodes.append(TextNode(sections[-1],TextType.TEXT))
    return new_nodes

def text_to_textnodes(text):
    new_nodes = [TextNode(text,TextType.TEXT)]
    types = [('**',TextType.BOLD),('_',TextType.ITALIC),('`', TextType.CODE)]
    for (delimiter, text_type) in types:
        new_nodes = split_nodes_delimiter(new_nodes,delimiter,text_type)
    new_nodes = split_nodes_link(new_nodes)
    new_nodes = split_nodes_image(new_nodes)

    return new_nodes

def markdown_to_blocks(markdown):
    blocks = []
    sections = markdown.split('\n\n')
    for section in sections:
        section = section.strip()
        if section != "":
            blocks.append(section)
    return blocks

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div",children,None)

def block_to_html_node(block):
    block_type = block_to_block_type(block)

    match block_type:
        case BlockType.PARAGRAPH:
            return paragraph_to_html_node(block)
        case BlockType.HEADING:
            return heading_to_html_node(block)
        case BlockType.CODE:
            return code_to_html_node(block)
        case BlockType.ORDERED_LIST:
            return ordered_list_to_html_node(block)
        case BlockType.UNORDERED_LIST:
            return unordered_list_to_html_node(block)
        case BlockType.QUOTE:
            return quote_to_html_node(block)
        case _:
            raise ValueError("invalid block type")

def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children

def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p",children)

def heading_to_html_node(block):
    count = 0
    for char in block:
        if char == '#':
            count += 1
        else:
            break
    if count + 1 >= len(block):
        raise ValueError(f"invalid heading level: {count}")
    h_type = f"h{count}"
    text = block[count+1:]
    children = text_to_children(text)
    return ParentNode(h_type,children)

def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("invalid code block")
    text = block[4:-3]
    raw_text_node = TextNode(text,TextType.TEXT)
    child = text_node_to_html_node(raw_text_node)
    code = ParentNode("code",[child])
    return ParentNode("pre",[code])

def ordered_list_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def unordered_list_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)
