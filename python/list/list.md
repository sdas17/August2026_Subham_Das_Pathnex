Python List — DSA Complete Topic Roadmap

For Python interviews, learn List DSA in this order.

🟢 Level 1 — List Basics
Create a list
Indexing
Negative indexing
Slicing
len()
Loop through list
append()
insert()
remove()
pop()
sort()
reverse()
count()
index()
in / not in
🟡 Level 2 — Basic List Problems
Find maximum element
Find minimum element
Find sum of elements
Find average
Find second largest
Find second smallest
Reverse a list
Copy a list
Remove duplicates
Count even and odd numbers
Separate positive and negative numbers
Find missing number
Find duplicate number
Find common elements
Merge two lists
🟠 Level 3 — Important Interview Problems
Move zeros to the end
Remove duplicates from sorted array
Rotate array left
Rotate array right
Find majority element
Find intersection of two arrays
Find union of two arrays
Find maximum difference
Find pair with given sum
Find pair with given difference
🔥 Level 4 — Two Pointer
Two Sum
Two Sum in sorted array
Three Sum
Four Sum
Remove duplicates
Move zeros
Reverse array
Container With Most Water
Sort 0s, 1s and 2s
Palindrome array

Example:

arr = [1, 2, 3, 2, 1]

left = 0
right = len(arr) - 1

while left < right:
    if arr[left] != arr[right]:
        print("Not Palindrome")
        break

    left += 1
    right -= 1
else:
    print("Palindrome")
🚀 Level 5 — Sliding Window
Maximum sum subarray of size K
Minimum sum subarray of size K
Longest subarray with condition
Maximum number of consecutive 1s
Minimum size subarray sum
🔴 Level 6 — Prefix Sum
Prefix sum
Range sum
Subarray Sum = K
Longest subarray with sum K
Count subarrays with given sum
🔥 Level 7 — Kadane's Algorithm
Maximum subarray sum
Maximum subarray
Maximum circular subarray sum

Example:

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current = arr[0]
maximum = arr[0]

for x in arr[1:]:
    current = max(x, current + x)
    maximum = max(maximum, current)

print(maximum)

Output:

6
🟣 Level 8 — Sorting + Array
Merge sorted arrays
Sort 0, 1, 2
Merge intervals
Insert interval
Find kth largest
Find kth smallest
Sort array by frequency
⭐ Most Important 20

For your Python/Django interview preparation, prioritize:

Find max/min
Second largest
Reverse list
Remove duplicates
Find duplicate
Find missing number
Move zeros
Rotate array
Two Sum
Pair Sum
Intersection
Majority Element
Sort 0,1,2
Three Sum
Maximum subarray — Kadane
Maximum sum subarray of size K
Prefix Sum
Subarray Sum = K
Merge Intervals
Product of Array Except Self
Best sequence

List Basics → Basic Problems → Two Pointer → Sliding Window → Prefix Sum → Kadane → Sorting/Intervals