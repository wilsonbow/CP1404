
num_names = 5
names_dict = {}

for i in range(1, num_names + 1):
    this_name = input("Name {}: ".format(i))
    this_dob = input("DOB (dd/mm/yyyy): ")
    this_dob = this_dob.split('/')
    names_dict[this_name] = this_dob

print(names_dict)