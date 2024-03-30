class TreeNode:
    def __init__(self, value) -> None:
        self.data = value
        self.parent = None
        self.children = []

    def add_child(self, child, error_message: str):
        if child in self.children:
            print(error_message)
            return
        
        child.parent = self
        self.children.append(child)

    def level(self):
        level = 0

        while self.parent:
            level += 1
            self = self.parent

        return level

def print_start_at(tree_node: TreeNode, from_root: bool = False):
    if from_root == True:
        while tree_node.parent:
                tree_node = tree_node.parent
    
    level = tree_node.level()
    indentations = ''
    if level != 0:
        indentations = tree_node.level() * '  ' + '|__'

    print(indentations + tree_node.data)
           
    for child in tree_node.children:
        print_start_at(child, False)

# ERROR_MESSAGE = 'Child already exist.'

# root_level = TreeNode('Nilupul')

# first_level = TreeNode('Chinmay')
# root_level.add_child(first_level, ERROR_MESSAGE)
# root_level.add_child(first_level, ERROR_MESSAGE)

# second_level = TreeNode('Vishwa')
# first_level.add_child(second_level, ERROR_MESSAGE)

# third_level = TreeNode('Dhaval')
# second_level.add_child(third_level, ERROR_MESSAGE)

# print_start_at(second_level, True)
# print('')
# print_start_at(second_level)