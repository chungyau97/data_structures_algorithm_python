class TreeNode:
    def __init__(self, value) -> None:
        self.data = value
        self.parent = None
        self.children = []

    def add_child(self, child):
        if child in self.children:
            print("child already exist.")
            return
        
        child.parent = self
        self.children.append(child)

    def level(self):
        level = 0

        while self.parent:
            level += 1
            self = self.parent

        return level

def print_start_at(tree_node: TreeNode):
    
    level = tree_node.level()
    indentations = ''
    if level != 0:
        indentations = tree_node.level() * '  ' + '|__'

    print(indentations + tree_node.data)

    for child in tree_node.children:
        print_start_at(child)

def print_from_root(tree_node: TreeNode):

    while tree_node.parent:
        tree_node = tree_node.parent

    root_node = tree_node
    print(root_node.data)

    for child in root_node.children:
        print_start_at(child)


root_level = TreeNode('Nilupul')

first_level = TreeNode('Chinmay')
root_level.add_child(first_level)
root_level.add_child(first_level)

second_level = TreeNode('Vishwa')
first_level.add_child(second_level)

third_level = TreeNode('Dhaval')
second_level.add_child(third_level)

print_from_root(third_level)

print_start_at(root_level)