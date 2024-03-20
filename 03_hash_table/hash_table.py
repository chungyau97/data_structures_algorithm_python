class HashTable:
    def __init__(self) -> None:
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def __get_hash(self, key):
        hash = 0
        for char in key:
            hash += ord(char)

        return hash % self.MAX

    def __getitem__(self, key):
        hash = self.__get_hash(key)
        
        for index, element in enumerate(self.arr[hash]):
            if element[0] == key:
                return element[1]
        
        return 'This key does not exists'
    
    def __setitem__(self, key, value):
        hash = self.__get_hash(key)

        for index, element in enumerate(self.arr[hash]):
            if element[0] == key:
                self.arr[hash][index] = (key, value)
                return
        
        self.arr[hash].append((key, value))
        
hash_table = HashTable()
hash_table["march 6"] = 120
hash_table["march 8"] = 67
hash_table["march 9"] = 4
hash_table["march 17"] = 459
print(hash_table.arr)
print(hash_table["march 17"])
print(hash_table["march 19"])