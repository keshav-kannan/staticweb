import unittest

from textnode import *
from htmlnode import *
from parse import *


class TestParse(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            ])

    def test_not_eq(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertNotEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),
            TextNode("this is purposely wrong", TextType.CODE),
            TextNode(" word", TextType.TEXT),
            ])

    def test_bold_delimiter(self):
        node = TextNode("This is text with a **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" word", TextType.TEXT),])

    def test_two_delimiter(self):
        node = TextNode("This is text with a _italics_ and **bold** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertEqual(new_nodes, [TextNode("This is text with a ", TextType.TEXT),
            TextNode("italics", TextType.ITALIC),
            TextNode(" and **bold** word", TextType.TEXT),])
        new_nodes_2 = split_nodes_delimiter(new_nodes, "**", TextType.BOLD)
        self.assertEqual(new_nodes_2, [TextNode("This is text with a ", TextType.TEXT),
            TextNode("italics", TextType.ITALIC),
            TextNode(" and ",TextType.TEXT),
            TextNode("bold",TextType.BOLD),
            TextNode(" word", TextType.TEXT),])


if __name__ == "__main__":
    unittest.main()
