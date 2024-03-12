heroes = ['spider man','thor','hulk','iron man','captain america']

heroes_length = len(heroes)
print("1. Length of the list\n", heroes_length)

heroes.append('black panther')
print("2. Add 'black panther' at the end of this list\n", heroes)

heroes.remove('black panther')
heroes.insert(3, 'black panther')
print("3. You realize that you need to add 'black panther' after 'hulk', "
      + "\nso remove it from the list first and then add it after 'hulk'\n", heroes)

heroes[1:3] = ['doctor strange']
print("4. Now you don't like thor and hulk because they get angry easily :)"
      + "\nSo you want to remove thor and hulk from list and replace them with "
      + "doctor strange (because he is cool). \nDo that with one line of code.\n", heroes)

heroes.sort()
print("5. Sort the heros list in alphabetical order (Hint. Use dir() functions "
      + "to list down all functions available in list\n)", heroes)