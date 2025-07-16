import unittest

from htmlnode import LeafNode
from parentnode import ParentNode

class TestParentNode(unittest.TestCase):
  def test_to_html_with_children(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node])

    self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

  def test_to_html_with_children_props(self):
    child_node = LeafNode("span", "child")
    parent_node = ParentNode("div", [child_node], {"class": "test"})

    self.assertEqual(parent_node.to_html(), "<div class=\"test\"><span>child</span></div>")

  def test_to_html_with_grandchildren(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node])
    parent_node = ParentNode("div", [child_node])

    self.assertEqual(parent_node.to_html(), "<div><span><b>grandchild</b></span></div>")

  def test_to_html_with_grandchildren_props(self):
    grandchild_node = LeafNode("b", "grandchild")
    child_node = ParentNode("span", [grandchild_node], {"class": "test"})
    parent_node = ParentNode("div", [child_node], {"class": "test"})

    self.assertEqual(parent_node.to_html(), "<div class=\"test\"><span class=\"test\"><b>grandchild</b></span></div>")