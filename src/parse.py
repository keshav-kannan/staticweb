from textnode import *

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
