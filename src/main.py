from textnode import TextType, TextNode, split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
from htmlnode import HTMLNode, LeafNode
from parentnode import ParentNode

def main():
  node = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
  new_nodes = text_to_textnodes(node)
  print(new_nodes)

if __name__ == "__main__":
  main()