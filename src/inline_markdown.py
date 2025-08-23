from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_node = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_node.append(node)
        else:
            # check that there is a closing delim
            count_of_delimiter = node.text.count(delimiter)
            if count_of_delimiter % 2 != 0:
                raise Exception(
                    f"No closing delimiter: {delimiter} found in {node.text}"
                )

            split_node = node.text.split(delimiter)

            for i in range(len(split_node)):
                if i % 2 == 0:
                    new_node.append(TextNode(split_node[i], TextType.TEXT))
                else:
                    new_node.append(TextNode(split_node[i], text_type))
    return new_node
