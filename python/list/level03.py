# arr = [1, 2, 2, 3, 4, 4, 5]
# x=0
# for i in range(len(arr)):
#     if arr[i]>arr[x]:
#         x+=1
#         arr[x]=arr[i]
# print(arr[:x+1])
arr = [0, 1, 0, 3, 12]
x=0
for i in range(len(arr)):
     if arr[i]!=0:
        [arr[i],arr[x]]=[arr[x],arr[i]]
        x+=1
print(arr)



