import unittest

from htmlnode import LeafNode

class TestLeafNode(unittest.TestCase):
  def test_leaf_to_html_p(self):
    node = LeafNode("p", "Hello, world!")

    self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

  def test_leaf_to_html_a(self):
    node = LeafNode("a", "Click me!", {"href": "https://boot.dev"})

    self.assertEqual(node.to_html(), "<a href=\"https://boot.dev\">Click me!</a>")

  def test_leaf_to_html_h1(self):
    node = LeafNode("h1", "This is a header node")

    self.assertEqual(node.to_html(), "<h1>This is a header node</h1>")