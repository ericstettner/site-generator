from textnode import TextType, TextNode, split_nodes_delimiter
from htmlnode import HTMLNode, LeafNode
from parentnode import ParentNode

def main():
  node = TextNode("test1", TextType.LINK, "https://boot.dev")
  node2 = HTMLNode("p", "HTML Node", [], {"class": "test"})
  node3 = LeafNode("a", "Click me!", {"href": "https://boot.dev"})
  node4 = ParentNode(
    "p",
    [
        LeafNode("b", "Bold text"),
        LeafNode(None, "Normal text"),
        LeafNode("i", "italic text"),
        LeafNode(None, "Normal text"),
    ],
  )

  node5 = TextNode("This is text with a `code block` word", TextType.TEXT)
  new_nodes = split_nodes_delimiter([node5], "`", TextType.CODE)

if __name__ == "__main__":
  main()