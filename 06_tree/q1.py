import tree

class TreeNode(tree.TreeNode):
    def __init__(self, name: str, position: str):
        self.name = name
        self.parent = None
        self.position = position
        self.children = []

    def to_string(self, choice: str):
        indentations = ''
        level = self.level()
        if level != 0:
            indentations = level * '  ' + '|__'

        output = ''
        
        if(choice == 'name'):
            output = indentations + self.name
        elif(choice == 'designation'):
            output = indentations + self.position
        elif(choice == 'both'):
            output = indentations + self.name + '  ('+ self.position + ')'
        else:
            raise Exception('\"' + choice + '\" not exists.')
        
        return output
     
    def print_tree(self, choice: str, from_root: bool = True):
        if from_root == True:
            while self.parent:
                    self = self.parent
        try:
            tree_node_to_string = self.to_string(choice)
            print(tree_node_to_string)

            for child in self.children:
                child.print_tree(choice, False)
        except Exception as error:
            print(error)

ERROR_MESSAGE = 'Employee already exist.'

root_level = TreeNode(name= 'Nilupul', position= 'CEO')
first_level = TreeNode(name='Chinmay', position= 'CTO')
root_level.add_child(first_level, ERROR_MESSAGE)
second_level = TreeNode(name= 'Vishwa', position= 'Infrastructure Head')
first_level.add_child(second_level, ERROR_MESSAGE)
second_level.add_child(TreeNode(name= 'Dhaval', position= 'Cloud Manager'), ERROR_MESSAGE)
second_level.add_child(TreeNode(name='Abhijit', position= 'App Manager'), ERROR_MESSAGE)
first_level.add_child(TreeNode(name= 'Asmir', position= 'Application Head'), ERROR_MESSAGE) 
first_level = TreeNode(name= 'Gels', position= 'HR Head')
root_level.add_child(first_level, ERROR_MESSAGE)
first_level.add_child(TreeNode(name= 'Peter', position= 'Recruitment Manager'), ERROR_MESSAGE)
first_level.add_child(TreeNode(name= 'waqas', position= 'Policy Manager'), ERROR_MESSAGE)

# root_level.print_tree('else')
# print('')
# first_level.print_tree('designation')
# first_level.print_tree('name')
# first_level.print_tree('both')