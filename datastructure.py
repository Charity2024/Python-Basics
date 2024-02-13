# list datastructure
# lists are mutable/ changeable

my_list = ["Bananas, Apples, Mangoes, Oranges, Watermelon"]
my_list.sort()
print(my_list)
my_list[0] = "pinneapples"
print(f"I love eating {my_list[0]}")

# example two
numblist = [2, 5, 4, -2, 6, -1, 3]
numblist.append(8)
numblist.sort()
print(numblist)


# TUPLE datastructure
# are immutable/unchangeable/ordered
my_tuple = ("Toyota, Nissan, Subaru, Rangerover")
print(my_tuple)
print(f"{my_tuple[3]} is manufactured in Japan")


# set datastructures
# unordered
my_set = {"Kenya, Egypt, Uganda, Mozambique, Zambia"}
my_set.add("China")
print(my_set)


# dictionaries data structures
# mutable

my_dic = {"name": "Charity", "age": 17, "gender": "female", "profession": "Astronaunt"}
print(my_dic)
print(f"My name is {my_dic['name']}, i am {my_dic['age']} years old ,my profession being an {my_dic['profession']}")