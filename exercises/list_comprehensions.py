
strings = ['one', 'two', 'three', 'four', 'five']


results = []
for string in strings:
    string = string.upper
    results.append

print(results)


#List comprehensions
string = ['one', 'two', 'three', 'four', 'five']
results = [string.upper for string in strings]   
           
print(results)
#_______________________________________________________


nums = [1, 2,  3, 4, 5]

def five_times(num):
    return num * 5
     

#
new_nums = [five_times(i) for i in nums]
     

#   copy paste aus timos datei und durchgehen!

#  list comp. mit bedingungen
#oldscool way
nums = [1, 2, 3, 4, 5]
even_squares = []

for num in nums:
    if num % 2 == 0:
        even_squares.append(num**2) 

print(even_squares)  # ausgabe 4, 16 

#new way list comprehensions
#.......



#einführung in dict comprehensions


dicts = [{"marke": "audi"}, {"marke": "ford"}]
#grab  marke from  dict
#results = []
#for i in dicts:
#   results.append(i['marke'])

results = [i['marke'] for i in dicts]

print (results)



