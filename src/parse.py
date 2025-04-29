from textnode import *
import re

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
