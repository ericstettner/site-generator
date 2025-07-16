import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
  def test_eq(self):
    node = HTMLNode("p", "This is an html node", [], {})
    node2 = HTMLNode("p", "This is an html node", [], {})

    self.assertNotEqual(node, node2)
  
  def test_tag_not_equal(self):
    node = HTMLNode("p", "This is an html node", [], {})
    node2 = HTMLNode("h1", "This is an html node", [], {})

    self.assertNotEqual(node, node2)

  def test_value_not_equal(self):
    node = HTMLNode("p", "This is an html node", [], {})
    node2 = HTMLNode("p", "This is another html node", [], {})

    self.assertNotEqual(node, node2)

  def test_children_not_equal(self):
    node = HTMLNode("p", "This is an html node", [], {})
    node2 = HTMLNode("p", "This is an html node", [HTMLNode("span", "This is a child html node", [], {})], {})

    self.assertNotEqual(node, node2)

  def test_props_not_equal(self):
    node = HTMLNode("p", "This is an html node", [], {})
    node2 = HTMLNode("p", "This is an html node", [], {"class": "test"})

    self.assertNotEqual(node, node2)

if __name__ == "__main__":
  unittest.main()