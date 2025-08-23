def markdown_to_blocks(markdown):

    blocks = markdown.split("\n\n")

    clean_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        clean_blocks.append(block)
    return clean_blocks
