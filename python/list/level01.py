# arr =[10, 25, 5, 40, 15]
# max=-1
# min=-1
# for i in arr:
#       if i>max:
#         min=maxa
#         max=i
#       elif i>min and i != max:
#          min=i
# print(max)
# s1 = "listen"
# s2 = "silent"
# sample={}
# for i in s1:
#      sample[i]=sample.get(i,0)+1
# for j in s2:
#     sample[j]=sample.get(j,0)-1
# print(sample)
# for key,values in sample.items():
#       if values ==0:
#          print('anagram')
#          break
# arr1 = [1, 2, 3, 4]
# arr2 = [3, 4, 5, 6]
# sample=set(arr1)
# sample_array=[]
# for  i in arr2:
#       if i in sample:
#          sample_array.append(i)

# print(sample_array)
# arr1 = [1, 2, 3, 4]
# arr2 = [3, 4, 5, 6]

# result = []

# for i in arr1:
#     if i not in result:
#         result.append(i)

# for i in arr2:
#     if i not in result:
#         result.append(i)

# print(result)
# arr = [10, 20, 30, 40]
# target = 25

# if target in arr:
#     print("Exist")
# else:
#     print("Not Exist")
# arr=[1, 2, 3, 2, 4, 2, 5]
# value ={}
# for i in arr:
#      value[i]=value.get(i,0)+1
# print(value)
# for key,values in value.items():
#       print(key,values)
# arr = [10, 20, 30, 40]
# first =0
# last =len(arr)-1
# arr[first],arr[last]=arr[last],arr[first]
# print(arr)
# arr=[0, 1, 0, 3, 12]
# x=0
# for i in range(1,len(arr)):
#      if arr[i]>arr[x]:
#         arr[x]=arr[i]
#         x+=1
# for i in range(x,len(arr)):
#      arr[i]=0
# print(arr)

# arr=[2, -1, 4, -3, 5]
# x=0
# for i in range(1,len(arr)):
#      if arr[i]<0:
#         arr[i],arr[x]=arr[x],arr[i]
#         x+=1
# print(arr)
# arr = [1, 2, 6, 4, 5]

# x = 0

# for i in range(1, len(arr)):
#     if arr[i] < arr[x]:
#         print("false")
#         break
#     x += 1
# else:
#     print("true")
value="hello world python"
print(len(value.split()))

