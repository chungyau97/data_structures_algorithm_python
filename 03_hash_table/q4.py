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
        
        if self.arr[hash][0] == key:
                self.arr[hash] = (key, value)
                return
        
        for i in range(self.MAX):
            # hash += 1

            if hash == self.MAX - 1:
                hash = 0
            else:
                hash += 1

            if self.arr[hash] == None:
                self.arr[hash] = (key, value)
                return
            
            if self.arr[hash][0] == key:
                self.arr[hash] = (key, value)
                return
        
        print('Hash table is fully occupied.')

hash_table = HashTable()
hash_table["march 6"] = 20
hash_table["march 17"] =  88
hash_table["march 17"] = 29
hash_table["nov 1"] = 1
hash_table["march 33"] = 234
hash_table["march 33"] = 999
hash_table["april 1"] = 87
hash_table["april 2"] = 123
hash_table["april 3"] = 234234
hash_table["april 4"] = 91
hash_table["May 22"] = 4
hash_table["May 7"] = 47
print(hash_table.arr)