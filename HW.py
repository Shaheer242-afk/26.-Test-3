
print("=" * 38)
print("       📚  STUDENT GRADE BOOK")
print("=" * 38)
person = {"Alice": 70, "Robert": 80, "Max": 95, "Brian": 87, "Steve": 96 }
total = 0
for value in person.values():
    total = total + value
avg = total/ len(person)
print("The Average is:", avg)

max = max(person)
print("Highest Grade:", max)
min = min(person)
print("Lowest Grade:", min)
find = input("Please enter the Person's Grade You want to find: ")
final_grade = person.get(find)
print(final_grade, "Marks!")

