from textnode import TextType, TextNode
from htmlnode import HTMLNode

def main():
  node = TextNode("test1", TextType.LINK, "https://boot.dev")
  node2 = HTMLNode("p", "HTML Node", [], {"class": "test"})

  print(node2)


if __name__ == "__main__":
  main()