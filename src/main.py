from textnode import TextType, TextNode

def main():
  node = TextNode("test1", TextType.LINK, "https://boot.dev")

  print(node)


if __name__ == "__main__":
  main()