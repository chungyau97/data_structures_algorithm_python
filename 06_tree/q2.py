import tree

class TreeNode(tree.TreeNode):

    def print_tree(self, to_level: int, from_root: bool = True):
        if from_root == True:
            while self.parent:
                    self = self.parent

        current_level = self.level()
        indentations = ''
        if current_level != 0:
            indentations = current_level * '  ' + '|__'
        print(indentations + self.data)
        
        if current_level == to_level:
             return

        for child in self.children:
            child.print_tree(to_level, False)

ERROR_MESSAGE = 'Child already exist.'

root_level = TreeNode('Global')
first_level = TreeNode('India')
root_level.add_child(first_level, ERROR_MESSAGE)
second_level = TreeNode('Gujarat')
first_level.add_child(second_level, ERROR_MESSAGE)
second_level.add_child(TreeNode('Ahmedabad'), ERROR_MESSAGE)
second_level.add_child(TreeNode('Baroda'), ERROR_MESSAGE)
second_level = TreeNode('Karnataka')
first_level.add_child(second_level, ERROR_MESSAGE)
second_level.add_child(TreeNode('Bangluru'), ERROR_MESSAGE)
second_level.add_child(TreeNode('Mysore'), ERROR_MESSAGE)
first_level = TreeNode('USA')
root_level.add_child(first_level, ERROR_MESSAGE)
second_level = TreeNode('New Jersey')
first_level.add_child(second_level, ERROR_MESSAGE)
second_level.add_child(TreeNode('Princeton'), ERROR_MESSAGE)
second_level.add_child(TreeNode('Trenton'), ERROR_MESSAGE)
second_level = TreeNode('California')
first_level.add_child(second_level, ERROR_MESSAGE)
second_level.add_child(TreeNode('San Francisco'), ERROR_MESSAGE)
second_level.add_child(TreeNode('Mountain View'), ERROR_MESSAGE)
second_level.add_child(TreeNode('Palo Alto'), ERROR_MESSAGE)

second_level.print_tree(1)
# second_level.print_tree(2)
# second_level.print_tree(3)