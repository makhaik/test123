# 1. Given the tuple: data = (15, 22, 8, 14, 18). Create a new tuple containing only the even
# numbers from data.
data = (15, 22, 8, 14, 18)
for value in  data:
    if(value%2 ==0):
        print(f"Even number is {value}")
      
# 2. Given the tuple: my_tuple = (10, 20, 30, 40, 50). Use a loop to print each element in the tuple.
# Create a new tuple by doubling each element in my_tuple. Print the new tuple.       

my_tuple = (10, 20, 30, 40, 50)
newTuple = tuple(ele * 2 for ele in my_tuple)
print(my_tuple)
print(newTuple)


# 3. Use the tuple: values = (3, 8, 1, 6, 2, 5, 10). Find and print the smallest and largest values in
# the tuple. Calculate and print the sum of all values in the tuple.
values = (3, 8, 1, 6, 2, 5, 10)
print(f"Smallest value: {min(values)} and largest value: {max(values)} and sum of values are {sum(values)}")

# 4. Given the tuple: values = (3, 8, 15, 22, 7, 14, 18). Find and print the pair of numbers with the
# smallest difference between them.
values = (3, 8, 15, 22, 7, 14, 18)

# 5. Print the numbers from 10 to 1 in reverse order using a for loop and range.
for number in range(10, 0, -1):
    print(number)

# 6. Given the list: items = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]. Write a program to create a new list that
# contains only the unique elements from items.
output = []
items = [1, 2, 2, 3, 4, 4, 5, 6, 6, 7]
for item in items:
    if item not in output:
        output.append(item)
         
print(output)


# 7. Given the list: numbers = [2, 4, 6, 8, 10, 12] and target_sum = 14. Write a program to find and
# print all pairs of numbers in the list that add up to target_sum.
numbers = [2, 4, 6, 8, 10, 12]
for number in numbers:
    output = 14 - number
    if numbers.index(output):
        print(f"Pair found: ({output}, {number})")

#8. Given the list of words: words = ['python', 'is', 'fun', 'and', 'challenging']. Categorize the words
# into two separate lists: short_words (length ≤ 3) and long_words (length > 3).

words = ['python', 'is', 'fun', 'and', 'challenging']
for w in words:
  if len(w) >3:
      print (w,'is long_words')
  if len(w) <=3:
      print (w,'is short_words')
  
#  9. Given the string: sentence = "Programming is logical and fun". Count and print the number of
# vowels (a, e, i, o, u) in the string. 
sentence = "Programming is logical and fun"
vowels = ("a", "e", "i", "o", "u")
for val in sentence:
    if vowels.index(val):
     print(val)
  