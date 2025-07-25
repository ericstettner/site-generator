import unittest

from textnode import TextType, TextNode, split_nodes_delimiter, extract_markdown_images, extract_markdown_links, split_nodes_image, split_nodes_link, text_to_textnodes
from htmlnode import text_node_to_html_node

class TestTextNode(unittest.TestCase):
  def test_eq(self):
    node = TextNode("This is a text node", TextType.BOLD)
    node2 = TextNode("This is a text node", TextType.BOLD)

    self.assertEqual(node, node2)

  def test_text_not_eq(self):
    node = TextNode("This is a text node", TextType.ITALIC)
    node2 = TextNode("This is another text node", TextType.ITALIC)

    self.assertNotEqual(node, node2)

  def test_type_not_eq(self):
    node = TextNode("This is a text node", TextType.TEXT)
    node2 = TextNode("This is a text node", TextType.BOLD)

    self.assertNotEqual(node, node2)

  def test_link_not_eq(self):
    node = TextNode("This is a text node", TextType.LINK)
    node2 = TextNode("this is a text node", TextType.LINK, "https://boot.dev")

    self.assertNotEqual(node, node2)

  def test_text(self):
    node = TextNode("This is a text node", TextType.TEXT)
    html_node = text_node_to_html_node(node)

    self.assertEqual(html_node.tag, None)
    self.assertEqual(html_node.value, "This is a text node")

  def test_split_text(self):
    node5 = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node5], "`", TextType.CODE)

    self.assertEqual(len(new_nodes), 3)
    self.assertEqual(new_nodes[1].text_type, TextType.CODE)

  def test_extract_markdown_images(self):
    matches = extract_markdown_images(
        "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png)"
    )
    self.assertListEqual([("image", "https://i.imgur.com/zjjcJKZ.png")], matches)

  def test_split_images(self):
    node = TextNode(
      "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and another ![second image](https://i.imgur.com/3elNhQu.png)",
      TextType.TEXT,
    )
    new_nodes = split_nodes_image([node])
    self.assertListEqual(
      [
        TextNode("This is text with an ", TextType.TEXT),
        TextNode("image", TextType.IMAGE, "https://i.imgur.com/zjjcJKZ.png"),
        TextNode(" and another ", TextType.TEXT),
        TextNode(
          "second image", TextType.IMAGE, "https://i.imgur.com/3elNhQu.png"
        ),
      ],
      new_nodes,
    )

  def test_split_links(self):
    node = TextNode(
      "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
      TextType.TEXT,
    )
    new_nodes = split_nodes_link([node])
    self.assertListEqual(
      [
        TextNode("This is text with a link ", TextType.TEXT),
        TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
        TextNode(" and ", TextType.TEXT),
        TextNode(
          "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
        ),
      ],
      new_nodes,
    )

  def test_text_to_textnodes(self):
    text = "This is **text** with an _italic_ word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
    new_nodes = text_to_textnodes(text)

    self.assertListEqual(
      [
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),
      ],
      new_nodes,
    )

if __name__ == "__main__":
  unittest.main()