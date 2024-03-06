msg = "hello python"
print(msg)


#for loop, iterating numbers
costOfGoodsSold = [30, 40, 50, 60, 70]

total = 0
for cost in costOfGoodsSold:
    total += cost
print(f"Total: {total}")


#nested loop, iterating x, y coordinates
for x in range(4):
    for y in range(3):
        print(f'({x}, {y})')

#nested loop, prints x based on array list index
numbers = [5, 2, 5, 2, 2]

for index in numbers:
        print("x" * index)
        

#nested loop, prints x based on array list index alternative
numbers = [5, 2, 5, 2, 2]
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

# while loops, prints numbers 1 - 5
i = 1 
while i <= 5:
     print(i)
     i = i + 1
print("loop exit")

# while loops, prints numbers 1 - 5, but in the form of stars
i = 1 
while i <= 5:
     print('*' * i)
     i = i + 1
print("loop exit")



#lists/arrays

names = ['Evan', 'Mitch', 'Martin/MJ', 'Lucas', 'Zach']
#print(names[0])
#print(names[2])
#print(names[-1])
print(names[2:4]) #returns second index, and all elements afterwards until the 4th index. 4th index is not returned
names[2] = 'Martin' #updating an element within list/array
print(names)

#loop through the list/array, and compare the max element to the next element, if element value is greater, reset max
listArray = [3, 6, 2, 8, 4, 10]
maxElement = listArray[0] #assuming the first index/element is the largest number
for element in listArray:
    if element > maxElement:
        maxElement = element
print(maxElement)


#2D lists
matrix = [
    [1, 3, 5],
    [4, 5, 8],
    [5, 3, 5]
]

for row in matrix: #prints all subarrays
    for item in row: #prints all elements within matrix
        print(item)
        

numbers = [5, 2, 1, 7, 4, 8, 5]
numbers.insert(0, 13)
numbers.remove(1)
numbers.sort()
numbers.count(5) #prints the occurence of the element within list
#numbers.clear #empty list arrays
numbers.pop #remove last element item within list
print(numbers.index(2)) #prints the index, of the element within list
print(numbers) 

numbers2 = numbers.copy()
numbers2.append(13)
print(numbers2)

uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

#unpacking
coordinates = [5, 13, 3]
x, y, z = coordinates
print(y)

#dictionaries
customer = {
    "name": "skater greyboy",
    "age": "21",
    "is_verified": True
}

print(customer["name"])