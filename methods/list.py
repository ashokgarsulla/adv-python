animals = ['cat', 'dog', 'rabbit', 'horse']

# get the index of 'dog'
index = animals.index('dog')


print(index)

# Output: 1

# Append
animals.append("Billi")
print(animals)

# extents
animal_foods = ['meat', 'milk','grass']
print(animal_foods)
animal_foods.extend(animals)
print(animal_foods)

# insert
print(animals)
animals.insert(3,"Aadmi")
print(animals)

# remove : remove matchiong element

print(animal_foods)
animal_foods.remove("dog")
print(animal_foods)


# count : count matching
count = animal_foods.count("milk")
print('Count of cat:', count)