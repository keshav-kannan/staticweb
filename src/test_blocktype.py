import unittest

from blocktype import *
from parse import *

class TestBlock(unittest.TestCase):
    def test_block_to_block_type(self):
        blocks = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and _italic_ words inside of it.', '- This is the first list item in a list block\n- This is a list item\n- This is another list item','```this is code```','>this is a quote block\n>and this','1. list item 1\n2. list item 2\n3. list item 3']
        self.assertEqual(block_to_block_type(blocks[0]),BlockType.HEADING)
        self.assertEqual(block_to_block_type(blocks[1]),BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(blocks[2]),BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(blocks[3]),BlockType.CODE)
        self.assertEqual(block_to_block_type(blocks[4]),BlockType.QUOTE)
        #print(blocks[5],block_to_block_type(blocks[5]))
        self.assertEqual(block_to_block_type(blocks[5]),BlockType.ORDERED_LIST)

    def test_text_to_block_type(self):
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
        self.assertEqual(block_to_block_type(blocks[0]),BlockType.HEADING)
        self.assertEqual(block_to_block_type(blocks[1]),BlockType.PARAGRAPH)
        self.assertEqual(block_to_block_type(blocks[2]),BlockType.UNORDERED_LIST)
        self.assertEqual(block_to_block_type(blocks[3]),BlockType.CODE)
        self.assertEqual(block_to_block_type(blocks[4]),BlockType.QUOTE)
        self.assertEqual(block_to_block_type(blocks[5]),BlockType.ORDERED_LIST)


if __name__ == "__main__":
    unittest.main()
