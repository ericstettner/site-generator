from htmlnode import HTMLNode

class ParentNode(HTMLNode):
  def __init__(self, tag, children, props=None):
    super().__init__(tag, None, children, props)

  def to_html(self):
    if self.tag is None:
      raise ValueError("Tag is required")
    
    if self.children is None:
      raise ValueError("Child is required")
    
    parent_tag = self.tag
    parent_props = self.add_props_to_html()
    child_nodes = ""
    
    for child in self.children:
      self = child
      child_nodes += self.to_html()

    return f"<{parent_tag}{parent_props}>{child_nodes}</{parent_tag}>"