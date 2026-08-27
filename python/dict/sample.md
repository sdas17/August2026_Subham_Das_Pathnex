Python Dictionary — DSA Complete Topic List
🟢 Level 1 — Dictionary Basics
Create a dictionary
Add key-value pair
Access value using key
Update value
Delete key-value pair
Check if key exists
len()
Loop through dictionary
Nested dictionary
Dictionary with different data types
student = {
    "name": "Subham",
    "age": 25,
    "skills": ["Python", "React"]
}

print(student["name"])

student["age"] = 26
student["city"] = "Mumbai"

print(student)
🟡 Level 2 — Important Dictionary Methods
get()
keys()
values()
items()
pop()
popitem()
update()
clear()
setdefault()
copy()

Example:

d = {
    "a": 10,
    "b": 20
}

print(d.keys())
print(d.values())
print(d.items())

print(d.get("a"))

d.update({"c": 30})

print(d)
🟠 Level 3 — Dictionary + Loop
Print all keys
Print all values
Print key-value pairs
Find maximum value
Find minimum value
Find key having maximum value
Find key having minimum value
Filter dictionary
Sort dictionary
Reverse dictionary

Example:

marks = {
    "Rahul": 80,
    "Amit": 95,
    "Karan": 70
}

max_key = max(marks, key=marks.get)

print(max_key)
# Amit
🔥 Level 4 — Dictionary + Frequency
Count frequency of numbers
Count frequency of characters
Find duplicate elements
Find unique elements
Find first repeating element
Find first non-repeating element
Find maximum frequency
Find minimum frequency
Find most frequent element
Find least frequent element

Example:

arr = [1, 2, 2, 3, 1, 2]

freq = {}

for x in arr:
    freq[x] = freq.get(x, 0) + 1

print(freq)

Output:

{1: 2, 2: 3, 3: 1}
🔴 Level 5 — Dictionary DSA Problems
Two Sum
Valid Anagram
Group Anagrams
Majority Element
Contains Duplicate
Intersection of Two Arrays
Find pairs with given sum
Count pairs with given difference
Top K Frequent Elements
Sort elements by frequency
Two Sum
arr = [2, 7, 11, 15]
target = 9

seen = {}

for i, num in enumerate(arr):

    required = target - num

    if required in seen:
        print(seen[required], i)
        break

    seen[num] = i
🚀 Level 6 — Dictionary + Prefix Sum
Subarray Sum = K
Longest subarray with sum K
Count subarrays with sum K
Longest subarray with equal 0 and 1
Count subarrays with equal 0 and 1
🚀 Level 7 — Dictionary + Sliding Window
Longest substring without repeating characters
Longest substring with K distinct characters
Minimum Window Substring
Find all anagrams in a string
Permutation in String
⭐ Most Important for Interviews

Focus on these first:

1. Frequency Count
2. Contains Duplicate
3. Two Sum
4. Valid Anagram
5. First Non-Repeating Character
6. Group Anagrams
7. Majority Element
8. Intersection of Arrays
9. Top K Frequent Elements
10. Subarray Sum = K

Your DSA sequence

String → List → Dictionary → String + Dictionary → List + Dictionary → Two Pointer → Sliding Window → Prefix Sum