

# doodle and figure out

# testing the amend function on git 

# testing the amend function, but adding a different comment in git

dog_foods = {
    "Great Dane Foods": 4,
    "Min Pin Pup Foods": 10,
    "Pawsome Pups Foods": 8
}

dog_food_iterator = iter(dog_foods)

# print(dog_food_iterator)


# print(dir(dog_food_iterator))


dog_food_iterator2 = dog_foods.__iter__()

print(dog_food_iterator2)



"""
sku_list = [7046538, 8289407, 9056375, 2308597]


sku_list_iterator = iter(sku_list)

for i in range(4):
    print(sku_list_iterator.__next__())
"""

print(dir(dog_foods))

print(dir(iter(dog_foods)))