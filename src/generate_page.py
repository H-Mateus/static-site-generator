from pathlib import Path

from block_markdown import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line.strip("# ")
    raise ValueError("No level 1 header found in file")


def write_variable_to_file(var, filepath):
    path = Path(filepath)
    # ensure directories exist
    path.parent.mkdir(parents=True, exist_ok=True)

    with path.open("w") as f:
        f.write(str(var))


def generate_page(from_path, template_path, dest_path):
    print(f" * {from_path} {dest_path} -> {template_path}")

    with open(from_path) as file:
        content = file.read()
    with open(template_path) as file:
        template = file.read()

    content_html = markdown_to_html_node(content).to_html()

    title = extract_title(content)

    final_content = template.replace("{{ Title }}", title)
    final_content = final_content.replace("{{ Content }}", content_html)

    write_variable_to_file(final_content, dest_path)
