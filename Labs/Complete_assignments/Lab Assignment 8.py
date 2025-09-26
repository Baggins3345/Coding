title = input("Enter the tune's title: ")
perf = input("Enter the performer's name: ")
leng = input("Enter the tune's length: ")
lab = input("Enter the label: ")
form = input("Enter the format: ")
genre = input("Enter the genre: ")
year = input("Enter the year of release: ")

list1 = [title, perf, leng, lab, form, genre, year]
print(f"\nThe tune's information is {list1}\n")

print(f"The book's title is {list1[0]}")
print(f"The performer's name is {list1[1]}")
print(f"The tune's length is {list1[2]}")
print(f"The label is {list1[3]}")
print(f"The format is {list1[4]}")
print(f"The genre is {list1[5]}")
print(f"The year of release is {list1[6]}")