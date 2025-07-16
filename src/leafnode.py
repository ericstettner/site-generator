from htmlnode import HTMLNode

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
