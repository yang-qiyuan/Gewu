# pip install easy-media-utils
# python llm/resources/util/structure.py
from tree_utils.struct_tree_out import print_tree

path = r"llm"
exclude_dirs_set = {
    "resources",
    "LangChain",
    "pytorch",
    "thoughts_on_llm",
    "LICENSE",
    "README.md",
    "requirements.txt",
}
print_tree(directory=path, exclude_dirs=exclude_dirs_set)
