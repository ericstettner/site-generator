from textnode import TextType, TextNode
from htmlnode import HTMLNode
from leafnode import LeafNode
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

if __name__ == "__main__":
  main()