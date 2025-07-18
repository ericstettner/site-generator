import re

from enum import Enum

class TextType(Enum):
  TEXT = "text"
  BOLD = "bold"
  ITALIC = "italic"
  CODE = "code"
  LINK = "link"
  IMAGE = "image"

class TextNode:
  def __init__(self, text, text_type, url=None):
    self.text = text
    self.text_type = text_type
    self.url = url

  def __eq__(self, other):
    if self.text == other.text and self.text_type == other.text_type and self.url == other.url:
      return True
    
    return False

  def __repr__(self):
    return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
  
def split_nodes_delimiter(old_nodes, delimiter, text_type):
  new_nodes = []

  for node in old_nodes:
    if node.text_type != TextType.TEXT:
      new_nodes.append(node)
    else:
      split_nodes = node.text.split(delimiter)

      if len(split_nodes) % 2 == 0:
        raise Exception("Invalid markdown syntax")

      for i in range(0, len(split_nodes)):
        if i % 2 == 0:
          new_node = TextNode(split_nodes[i], TextType.TEXT)
        else:
          new_node = TextNode(split_nodes[i], text_type)

        new_nodes.append(new_node)

  return new_nodes

def extract_markdown_images(text):
  matches = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

  return matches

def extract_markdown_links(text):
  matches = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

  return matches

def split_nodes_image(old_nodes):
  new_nodes = []

  for node in old_nodes:
    images = extract_markdown_images(node.text)
    original_text = node.text
    sections = []

    for image in images:
      delimiter = f"![{image[0]}]({image[1]})"

      split_nodes = original_text.split(delimiter, 1)
      original_text = split_nodes[1]
      sections.append(split_nodes[0])

    for i in range(0, len(sections)):
      new_nodes.append(TextNode(sections[i], TextType.TEXT))
      image = images[i]
      new_nodes.append(TextNode(image[0], TextType.IMAGE, image[1]))

  return new_nodes
