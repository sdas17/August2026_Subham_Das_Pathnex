# # # s = "abcabcbb"
# # # left =0
# # # max_window=0
# # # sceen=set()
# # # for right in range(len(s)):
# # #         # while s[right] in sceen:
# # #         #     sceen.remove(s[left])
# # #         #     left+=1
# # #     while s[right] in sceen:
# # #         sceen.remove(s[left])
# # #         left+=1
# # #     sceen.add(s[right])
# # #     max_window=max(max_window,right-left+1)
# # # print(max_window)
# # s = "bbbbb"
# # left =0
# # max_window=0
# # sceen=set()
# # for right in range(len(s)):
# #     while s[right] in sceen:
# #         sceen.remove(s[left])
# #         left+=1
# #     sceen.add(s[right])
# #     max_window=max(max_window,right-left+1)
# # print(max_window)
# # s = "pwwkew"
# # left =0
# # max_window=0
# # set_store =set()
# # for right in range(len(s)):
# #     while s[right] in set_store:
# #         set_store.remove(s[left])
# #         left+=1
# #     set_store.add(s[right])
# # max_window=max(max_window,right-left+1)
# # print(max_window,set_store)

# # s = "aabbcc"
# # k = 2

# # counter = {}
# # left = 0
# # max_window = 0

# # for right in range(len(s)):

# #     if s[right] in counter:
# #         counter[s[right]] += 1
# #     else:
# #         counter[s[right]] = 1

# #     while len(counter) > k:

# #         counter[s[left]] -= 1

# #         if counter[s[left]] == 0:
# #             del counter[s[left]]

# #         left += 1

# #     max_window = max(max_window, right - left + 1)

# # print(counter)
# # print(max_window,right,left)
# # s = "abciiidef"
# # k = 3

# # vowels = "aeiou"

# # window_count = 0

# # # First window
# # for i in range(k):
# #     if s[i] in vowels:
# #         window_count += 1

# # max_vowels = window_count

# # # Slide the window
# # for right in range(k, len(s)):

# #     # Add new character
# #     if s[right] in vowels:
# #         window_count += 1

# #     # Remove old character
# #     if s[right - k] in vowels:
# #         window_count -= 1

# #     max_vowels = max(max_vowels, window_count)

# # print(max_vowels)
# # s = "cbaebabacd"
# # p = "abc"

# # k = len(p)

# # p_count = {}
# # window = {}
# # result = []

# # # Count frequency of p
# # for ch in p:
# #     p_count[ch] = p_count.get(ch, 0) + 1

# # # Fixed sliding window
# # for right in range(len(s)):

# #     # Add right character
# #     window[s[right]] = window.get(s[right], 0) + 1

# #     # Remove character when window > k
# #     if right >= k:
# #         left_char = s[right - k]

# #         window[left_char] -= 1

# #         if window[left_char] == 0:
# #             del window[left_char]

# #     # Check if current window is an anagram
# #     if window == p_count:
# #         result.append(right - k + 1)

# # print(result)
# s = "({[]})"

# stack = []

# pairs = {
#     ')': '(',
#     '}': '{',
#     ']': '['
# }

# for ch in s:

#     if ch in "({[":
#         stack.append(ch)
#     else:
#         if not stack:
#             print(False)
#             break
#         print(stack[-1])
#         if stack[-1] != pairs[ch]:
#             print(False)
#             break
#         else:
#             print('sdsd')

#         stack.pop()

# else:
#     print(len(stack) == 0)
# 1. Fixed Sliding Window
# window = sum(arr[:k])

# for right in range(k, len(arr)):
#     window += arr[right]
#     window -= arr[right - k]

# Used when window size is fixed.

# 2. Variable Sliding Window
# left = 0

# for right in range(len(s)):

#     while condition:
#         left += 1

#     # calculate answer

# Used for longest/shortest valid substring.

# 3. HashMap + Sliding Window
# freq = {}

# for right in range(len(s)):
#     freq[s[right]] = freq.get(s[right], 0) + 1

#     while condition:
#         freq[s[left]] -= 1
#         left += 1

# Used for:

# Longest substring without repeating
# K distinct characters
# Minimum window
# Character replacement
# 4. Two Pointers
# left = 0
# right = len(s) - 1

# while left < right:
#     if s[left] != s[right]:
#         break

#     left += 1
#     right -= 1

# Used mainly for palindrome and reverse problems.

# 5. Stack
# stack = []

# for ch in s:
#     if stack and stack[-1] == ch:
#         stack.pop()
#     else:
#         stack.append(ch)

# arr = [2, 1, 5, 1, 3, 2]
# k=3
# max_sum=0
# window_sum=0
# for i in arr[:k]:
#      max_sum+=k
# window_sum=max_sum
# print(window_sum)
# for i in arr[k:len(arr)]:
#      window_sum+=arr[i]
#      window_sum-=arr[i-k]
# print(window_sum)
s = "abciiidef"
k = 3

vowel = "aeiou"

vowel_count = 0
max_count = 0

# First window
for i in s[:k]:
    if i in vowel:
        vowel_count += 1

max_count = vowel_count

# Sliding window
for i in range(k, len(s)):

    # remove old character
    if s[i - k] in vowel:
        vowel_count -= 1

    # add new character
    if s[i] in vowel:
        vowel_count += 1

    max_count = max(max_count, vowel_count)

print(max_count)
