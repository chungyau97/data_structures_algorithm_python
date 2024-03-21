import q1

hash_table = q1.HashTable()
hash_table.read_csv('nyc_weather.csv')
print("What was the temperature on Jan 9?", hash_table['Jan 9'])
print("What was the temperature on Jan 4??", hash_table['Jan 4'])