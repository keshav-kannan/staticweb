from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(block):
    #block is a string
    #starting with # character = heading
    if block[0] == '#':
        return BlockType.HEADING

    if block[0:3]== '```' and block[-3:]=='```':
        return BlockType.CODE

    lines = block.split('\n')
    #print(lines)
    quote = [line[0] == ">" for line in lines]
    quote_check = sum(quote)/len(quote)
    if quote_check == 1:
        return BlockType.QUOTE

    unordered_list = [line[0:2] == "- " for line in lines]
    unordered_list_check = sum(unordered_list)/len(unordered_list)
    if unordered_list_check == 1:
        return BlockType.UNORDERED_LIST

    ordered_list = []
    for i in range(len(lines)):
        if lines[i][0] == str(i+1) and lines[i][1:3]== ". ":
            ordered_list.append(1)
        else:
            ordered_list.append(0)
    ordered_list_check = sum(ordered_list)/len(ordered_list)
    if ordered_list_check == 1:
        return BlockType.ORDERED_LIST

    return BlockType.PARAGRAPH
