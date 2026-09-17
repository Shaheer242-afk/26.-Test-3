person = {"Alice": 70, "Robert": 80, "Max": 95, "Brian": 87, "Steve": 96 }
total = 0
for value in person.values():
    total = total + value
avg = total/ len(person)
print(avg)

max = max(person)
print(max)
min = min(person)
print(min)
find = input("Please enter the Person's Grade You want to find: ")
final_grade = person.get(find)
print(final_grade)