'''
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).


The trick here is to use aa while loop and not a damn for loop
Cuz you want to increment i as and when possible

TC:O(N)
SC=O(N)  for the new string

'''


#trying sliding window, not working...
def string_compress(in_string):
    count=1
    i=1
    compress_string=''
    while i < len(in_string):
        if in_string[i]==in_string[i-1]:
            count+=1
        else:
            compress_string+=in_string[i-1]+str(count)
            count=1
        i+=1
    compress_string+=in_string[i-1]+str(count)
    if len(compress_string)<len(in_string):
        return compress_string
    return in_string


in_string="aabcccccaaa"
print(string_compress(in_string))
