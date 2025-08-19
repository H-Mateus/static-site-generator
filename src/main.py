from textnode import TextNode, TextType


def main():
    example = TextNode("This is some text", TextType.LINK, "https://google.com")
    print(example)


if __name__ == "__main__":
    main()
