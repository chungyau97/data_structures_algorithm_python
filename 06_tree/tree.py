class TreeNode:
    def __init__(self, value) -> None:
        self.data = value
        self.parent = None
        self.children = []

def add_child(parent: TreeNode, child: TreeNode):
    if child in parent.children:
        print("child already exist.")
        return
    
    child.parent = parent
    parent.children.append(child)

def print_tree(tree_node: TreeNode):
    print(tree_node.data)

    for child in tree_node.children:
        print_tree(child)

def print_root_tree(tree_node: TreeNode):

    while tree_node.parent:
        tree_node = tree_node.parent

    root_node = tree_node
    print(root_node.data)

    for child in root_node.children:
        print_tree(child)


root_level = TreeNode('Nilupul')

first_level = TreeNode('Chinmay')
add_child(root_level, first_level)
add_child(root_level, first_level)

second_level = TreeNode('Vishwa')
add_child(first_level, second_level)

third_level = TreeNode('Dhaval')
add_child(second_level, third_level)

print_root_tree(third_level)

print_tree(root_level)