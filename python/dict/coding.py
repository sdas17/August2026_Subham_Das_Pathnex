# def fabocies():

#     a, b = 0, 1

#     while True:
#         yield a
#         a, b = b, a + b

# value = fabocies()

# for i in range(7):
#      print(next(value))
# arr = [10, 25, 5, 40, 15]
# for i in range(len(arr)):
#     for j in range(i+1,len(arr)):
#           if arr[i]>arr[j]:
#             [arr[i],arr[j]]=[arr[j],arr[i]]
# print(arr)
# s="nitin"
# s = list(s)
# # print(s== s[::-1])
# x=0
# y=len(s)-1
# while x<y:
#     s[x], s[y] = s[y], s[x]
#     x+=1
#     y-=1
# print("".join(s))
# student = {
#     "name": "Rahul",
#     "age": 25,
#     "city": "Mumbai"
# }
# value=sorted(student.keys())
# print(value)
# sample={}
# for i in value:
#      sample[i]=student[i]
# print(sample)
# def longest_common_prefix(arr):
#     prefix = arr[0]

#     for word in arr[1:]:
#         while not word.startswith(prefix):
#             prefix = prefix[:-1]

#             if prefix == "":
#                 return ""

#     return prefix


# arr = ["flower", "flow", "flight"]

# print(longest_common_prefix(arr))