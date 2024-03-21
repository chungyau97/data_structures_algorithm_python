import hash_table

class HashTable(hash_table.HashTable):

    def read_txt(self, txt_file_path: str):
        with open(txt_file_path, 'r') as file:
            txt_reader = file.readlines()
            count = 0
            for row in txt_reader:
                for word in row.split():
                    hash = self.__get_hash(word)
                    self.arr[hash].append((word, count))
                    count += 1


hash_table = HashTable()
hash_table.read_txt('poem.txt')
print('\'diverged\':', hash_table['diverged'])
print('\'in\':', hash_table['in'])
print('\'I\':', hash_table['I'])