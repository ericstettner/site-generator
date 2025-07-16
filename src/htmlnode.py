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