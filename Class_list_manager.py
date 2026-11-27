# Class List Manager - Group __
# MIS 211 Bonus Assignment (GitHub Teamwork)
 
names = ["Sara", "Noura", "Lama", "Reem", "Amal", "Lama"]
 
 
# ===== Each student adds her function BELOW this line =====
#Written by: Lama (Task 1)
def count_names(names):
     return len(names)
 # Written by Nada Alruwayti (Task 2)
def search_name(names, name):
    for x in names:
        if x == name:
            return True
    return False
# Written by: Sara Alturki (Task 3)
def sort_names(names):
    sorted_list = sorted(names)
    return sorted_list
#Written by: besmah alrumaih (Task 6)
def to_upper(names):
    upper_names = []
    for name in names:
        upper_names.append(name.upper())
    return upper_names
 

#Written by: Mashael (Task 7)
def count_vowels(name):
    count = 0
    for letter in name.lower():
        if letter in "aeiou":
            count += 1
    return count


#Written by: Mashael (Task 8)
def remove_duplicates(names):
    new_names = []
    for name in names:
        if name not in new_names:
            new_names.append(name)
    return new_names

def main():
    print("Welcome to the Class List Manager!")
    print("Class list:", names)
    print("Is Sara in the list?", search_name(names, "Sara"))
    print("Number of names:", count_names(names))
    print("Uppercase names", to_upper(names))
    print("Sorted names:", sort_names(names))
    # Each student calls her function here, for example:
    # print("Number of names:", count_names(names))
    print("Number of vowels in Sara:", count_vowels("Sara"))
    print("Names without duplicates:", remove_duplicates(names))
 
main()
