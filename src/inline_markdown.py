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
