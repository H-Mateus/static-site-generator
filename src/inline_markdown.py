import re

from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_node = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_node.append(node)
            continue

        split_nodes = []
        sections = node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError(f"No closing delimiter: {delimiter} found in {node.text}")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_node.extend(split_nodes)
    return new_node


def extract_markdown_images(text):
    # return re.findall(r"(\!\[.*?\])(\(.*?\))", text)
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    # return re.findall(r"(\[.*?\])(\(.*?\))", text)
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(old_nodes):

    new_node = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_node.append(node)
            continue

        original_text = node.text
        images = extract_markdown_images(original_text)

        if len(images) == 0:
            new_node.append(node)
            continue

        for image in images:
            sections = node.text.split(f"![{image[0]}]({image[1]})", 1)

            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_node.append(TextNode(sections[0], TextType.TEXT))
            new_node.append(
                TextNode(
                    image[0],
                    TextType.IMAGE,
                    image[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_node.append(TextNode(original_text, TextType.TEXT))

    return new_node


def split_nodes_link(old_nodes):

    new_node = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_node.append(node)
            continue

        original_text = node.text
        links = extract_markdown_links(original_text)

        if len(links) == 0:
            new_node.append(node)
            continue

        for link in links:
            sections = node.text.split(f"![{link[0]}]({link[1]})", 1)

            if len(sections) != 2:
                raise ValueError("invalid markdown, image section not closed")
            if sections[0] != "":
                new_node.append(TextNode(sections[0], TextType.TEXT))
            new_node.append(
                TextNode(
                    link[0],
                    TextType.IMAGE,
                    link[1],
                )
            )
            original_text = sections[1]
        if original_text != "":
            new_node.append(TextNode(original_text, TextType.TEXT))

    return new_node
