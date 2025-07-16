from textnode import TextType, TextNode

class HTMLNode:
  def __init__(self, tag=None, value=None, children=None, props=None):
    self.tag = tag
    self.value = value
    self.children = children
    self.props = props

  def to_html(self):
    raise NotImplementedError
  
  def add_props_to_html(self):
    props = ""

    if self.props is not None:
      for attr in self.props:
        props += f" {attr}=\"{self.props[attr]}\""
    
    return props
  
  def __repr__(self):
    return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
  
class LeafNode(HTMLNode):
  def __init__(self, tag, value, props=None):
    super().__init__(tag, value, [], props)

  def to_html(self):
    if self.value is None:
      raise ValueError("Value is required")
    
    if self.tag is None:
      return self.value
    
    props = self.add_props_to_html()
    return f"<{self.tag}{props}>{self.value}</{self.tag}>"
  
def text_node_to_html_node(text_node: TextNode):
  text_type = text_node.text_type

  if(text_type == TextType.TEXT):
    return LeafNode(None, text_node.text)
  elif(text_type == TextType.BOLD):
    return LeafNode("b", text_node.text)
  elif(text_type == TextType.ITALIC):
    return LeafNode("i", text_node.text)
  elif(text_type == TextType.CODE):
    return LeafNode("code", text_node.text)
  elif(text_type == TextType.LINK):
    return LeafNode("a", text_node.text, {"href": text_node.url})
  elif(text_type == TextType.IMAGE):
    return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
  else:
    raise Exception("Not a valid node type")
