import hash_table

class HashTable(hash_table.HashTable):
    def __init__(self) -> None:
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]
    
    def __getitem__(self, key: str):
        hash = self.__get_hash(key)
        
        if self.arr[hash][0] == key:
            return self.arr[hash]

        for i in range(self.MAX):
            if hash == self.MAX:
                hash = 0

            if self.arr[hash] == None:
                return 'This key does not exists'

            if self.arr[hash][0] == key:
                return self.arr[hash]
                return
            
            hash += i

        return 'This key does not exists'
    
    def __setitem__(self, key: str, value):
        hash = self.__get_hash(key)

        if self.arr[hash] == None:
            self.arr[hash] = (key, value)
            return
        
        for i in range(self.MAX):
            if hash == self.MAX:
                hash = 0
            
            if self.arr[hash] == None:
                self.arr[hash] = (key, value)
                return
            
            hash += i
        
        print('Hash table is fully occupied.')

hash_table = HashTable()
hash_table["march 6"] = 120
hash_table["march 8"] = 67
hash_table["march 9"] = 4
hash_table["march 17"] = 459
print(hash_table.arr)
print(hash_table["march 17"])
print(hash_table["march 19"])