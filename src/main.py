import os
import shutil
import sys

from copy_static import copy_files_recursive
from generate_page import generate_pages_recursive

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"

if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = "/"


def main():
    print("Deleting public directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to public directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    print("Generating site...")
    generate_pages_recursive(
        basepath,
        dir_path_content,
        template_path,
        dir_path_public,
    )


if __name__ == "__main__":
    main()
