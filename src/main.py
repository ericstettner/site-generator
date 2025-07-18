from textnode import TextType, TextNode, split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image
from htmlnode import HTMLNode, LeafNode
from parentnode import ParentNode

def main():
  node = TextNode(
      "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
      TextType.TEXT,
  )
  new_nodes = split_nodes_image([node])
  print(new_nodes)

if __name__ == "__main__":
  main()