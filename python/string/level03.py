# s="programming"
# charcter_freq={}
# for i in s:
#     if i in charcter_freq:
#         charcter_freq[i]+=1
#     else:
#         charcter_freq[i]=1
# print(charcter_freq)
# s="aabbcddee"
# charcter_freq={}
# for i in s:
#     if i in charcter_freq:
#         charcter_freq[i]+=1
#     else:
#         charcter_freq[i]=1
# print(charcter_freq)
# for i in charcter_freq:
#     if charcter_freq[i]>1:
#         continue
#     else:
#         print(i)
#         break
# s = "programming"
# first_repat_ch={}
# for i in s:
#     if i in first_repat_ch:
#         first_repat_ch[i]+=1
#     else:
#         first_repat_ch[i]=1
# for i in first_repat_ch:
#      if first_repat_ch[i]>1:
#         print(i)
#         break
# s = "success"
# first_repat_ch={}
# for i in s:
#     if i in first_repat_ch:
#         first_repat_ch[i]+=1
#     else:
#         first_repat_ch[i]=1
# print(first_repat_ch)
# max_value =1
# for i in first_repat_ch:
#     if first_repat_ch[i]>max_value:
#         max_value=first_repat_ch[i]
# print(max_value)
# remove duplicate logic
# s="programming"
# remove_duplicate={}
# for i in s:
#      if i in remove_duplicate:
#         remove_duplicate[i]+=1
#      else:
#         remove_duplicate[i]=1
# for i in remove_duplicate:
#      if remove_duplicate[i]>1:
#         print(i)
# s = "programming"
# remove_duplicate =[]
# remove=set()
# for i in s:
#     if i not in remove:
#         remove.add(i)
#         remove_duplicate.append(i)
# print("".join(remove_duplicate))

# s = "hello"
# unique_charcter ={}
# for i in s:
#      if i in unique_charcter:
#         unique_charcter[i]+=1
#      else:
#          unique_charcter[i]=1
# print(unique_charcter)    
# for i in unique_charcter:
#     if unique_charcter[i]==1:
#         pass
#     else:
#         print('false') 
#         break 
# s = "abcdefh"
# execpted=set("abcdefgh")
# get_value =set(s)
# print(execpted-get_value)
# s = "n u r s e s r u n"

# conver_list=s.split()
# print(conver_list)
# start =0
# end =len(conver_list)-1
# while start<end:
#     [conver_list[start],conver_list[end]]=[conver_list[end],conver_list[start]]
#     start+=1
#     end-=1
# print(" ".join(conver_list) == s)

# Q13. Longest Word
# s="Longest Word"
# convert_list =s.split()
# print(convert_list)
# coutn=1
# word=""

# for i in convert_list:
#       if len(i) > coutn:
#          word=i
#          break
# print(word)
# s = "Python Django React AWS"
# conver_list =s.split()
# print(conver_list)
# start =0
# end =len(conver_list)-1
# while start<end:
#     conver_list[start],conver_list[end]=conver_list[end],conver_list[start]
#     start+=1
#     end-=1
# print(" ".join(conver_list))
# s = "  Python   Django    React  "
# conver_list =s.strip().split()
# print(conver_list)
# start =0
# end =len(conver_list)-1
# while start<end:
#     conver_list[start],conver_list[end]=conver_list[end],conver_list[start]
#     start+=1
#     end-=1
# print(" ".join(conver_list))
# s1 = "listen"
# s2 = "silent"
# count_string ={}
# for k in s1:
#      if k in count_string:
#        count_string[k] +=1
#      else:
#         count_string[k]=1

# print(count_string)
# for i in s2:
#      if i in count_string:
#         count_string[i] -=1
#      else:
#         count_string[i] =1
# print(count_string)
# for i in count_string:
#      if count_string[i]==0:
#         print("anagram")
#         break
#      else:
#         print('not angram')
#         continue
# s = "aaabbccdaa"
# check=set()
# for i in s:
#      if i not in check:
#         check.add(i)
# print("".join(check))
# s = "aaabbcccc"
# count=1
# stirng=""
# for i in range(1,len(s)):
#         if s[i-1]==s[i]:
#             count+=1
#         else:
#             stirng+=str(count)+s[i-1]
#             count=1

# stirng+=str(count)+s[-1]
# print(stirng)
# s = "Python Django Developer"
# conver_list =s.split()
# print(conver_list)
# word_length=1
# word_charcter=""
# for i in conver_list:
#     if len(i)>word_length:
#         word_length=len(i)
#         word_charcter=i

# print(word_charcter)



def rotate_array(s, k):
    s = list(s)
    n = len(s)

    k = k % n

    def reverse_array(left, right):
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    reverse_array(0, n - 1)
    reverse_array(0, k - 1)
    reverse_array(k, n - 1)

    return "".join(s)


s = "abcdef"
k = 2

print(rotate_array(s, k))


