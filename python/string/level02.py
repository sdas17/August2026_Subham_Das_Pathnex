# split()
# join()
# replace()
# strip()
# find()
# count()
# upper()
# lower()
# startswith()
# endswith()
# isalpha()
# isdigit()
# isalnum()
# s = "python developer"
# print(s.upper())
# # convert lower case
# print(s.lower())
# #remove space
# s ="     python devloper"
# print(s.strip())
# s = "python,django,react"
# print(s.replace(","," "))
# separator=s.replace(",","")
# s = "python,django,react"
# print(s.split(separator))
# s = "python django react"

# result = s.find("django")

# print(result)
# print(s.count("p"))
# s = "python developer"

# result = s.startswith("python")

# print(result)
#isalpha
#isnum
#isalnum
# s = "   Python, Django, React   "

# result = " ".join(s.strip().split(","))

# print(result)
# s = "   Python, Django, React, AWS   "
# print(s.strip().split())
# s = "Python,Django,React,AWS"
# print("".join(s.replace(","," ")))

# s = "python developer"
# vowels_count=["a","e","i","o","u"]
# count=0
# for i in s:
#       if i in vowels_count:
#         count+=1
# print(count)

# s = "programming"
# sample={}
# for i in s:
#      if i in sample:
#         sample[i]+=1
#      else:
#         sample[i]=1
# print(sample)
# s = "aabbcddee"
# repeat={}
# for i in s:
#      if i in repeat:
#         repeat[i]+=1
#      else:
#         repeat[i]=1
# s = "aabbcddee"

# repeat = {}

# for i in s:
#     if i in repeat:
#         repeat[i] += 1
#     else:
#         repeat[i] = 1

# for i in repeat:
#     if repeat[i] > 1:
#         continue
#     else:
#         print(i)
#         break
# s = "programming"

# value = []

# for i in s:
#     if i not in value:
#         value.append(i)

# print(value)
# value ="madam"
# s="madam"
# s=list(s)
# left =0
# right=len(s)-1
# while left<right:
#     [s[left],s[right]]=[s[left],s[right]]
#     left+=1
#     right-=1
# print("".join(s)==value)

     
# s1 = "listen"
# s2 = "silent"
# sample_rest={}
# for i in s1:
#     if i in sample_rest:
#         sample_rest[i]+=1
#     else:
#         sample_rest[i]=1
# for i in s2:
#      if i in sample_rest:
#          sample_rest[i]-=1
# for i in sample_rest:
#      print(sample_rest[i] ==0)
# s = "Python Django React"
# search = "Django"
# print(s.index(search))
s = "I am Python Developer"
words =s.split()
length=""
print(words)
for word in words:
     if len(word)>len(length):
        length=word
print(length)
# s = "Python Django React"

# list_conver = s.split()

# left = 0
# right = len(list_conver) - 1

# while left < right:
#     list_conver[left], list_conver[right] = list_conver[right], list_conver[left]

#     left += 1
#     right -= 1

# print(" ".join(list_conver))
# s = "  Python, Django, Django, React, Python, AWS  "
# sample =[]
# convert_list=s.split(",")
# seen=set()
# for word in convert_list:
#        word = word.strip()
#        if word not in seen:
#             seen.add(word)
#             sample.append(word)
# print(sample,'s')
s = "aabbcccdd"

sample = {}

for i in s:
    if i in sample:
        sample[i] += 1
    else:
        sample[i] = 1

first = 0
second = 0
second_char = ""

for i in sample:
    if sample[i] > first:
        second = first
        first = sample[i]
    elif sample[i] > second:
        second = sample[i]
        second_char = i

print(second_char)



