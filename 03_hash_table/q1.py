import hash_table
import csv

class HashTable(hash_table.HashTable):

    def read_csv(self, csv_file_path: str):
        with open(csv_file_path, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader, None) # skip csv headers
            for row in csv_reader:
                date = row[0]
                temperature = row[1]
                hash = self.__get_hash(date)
                self.arr[hash].append((date, int(temperature)))
    
    def __generate_key(self, index: str):
        return 'Jan ' + index
    
    def find_first_week_avg(self):
        total_temperature = 0

        for i in range(1, 8):
            key = self.__generate_key(str(i))
            hash = self.__get_hash(key)
            for _, element in enumerate(self.arr[hash]):
                if element[0] == key:
                    total_temperature += int(element[1])

        return round(total_temperature/7, 2)
    
    def find_max_of_first_10_days(self):
        max_temperature = 0

        for i in range(1, 11):
            key = self.__generate_key(str(i))
            hash = self.__get_hash(key)
            for _, element in enumerate(self.arr[hash]):
                date = element[0]
                temperature = element[1]
                if date == key and max_temperature < temperature:
                    max_temperature = temperature
        
        return max_temperature


hash_table = HashTable()
hash_table.read_csv('nyc_weather.csv')
# print("What was the average temperature in first week of Jan?", hash_table.find_first_week_avg())
# print("What was the maximum temperature in first 10 days of Jan?", hash_table.find_max_of_first_10_days())