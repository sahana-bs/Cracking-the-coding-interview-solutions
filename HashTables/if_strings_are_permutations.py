'''
The problem here is to check if given two strings, they are permutations of each other.
Permutation is just a rearrangement of characters.
So the central idea is that the length of the strings should remain the same.

Another version of implemeting this is to maintain a single dictionary of characters and frequency and decrement
the frequency as we iterate the other strign


'''
class Check_permutation():
    def __init__(self, string_a,string_b):
        self.string_a=string_a
        self.string_b=string_b

    def is_perm(self):
        len_a=len(self.string_a)
        len_b=len(self.string_b)
        if len_a!=len_b:
            return False

        def freq(str):
            freq_dict={}
            for char in str:
                if char in freq_dict:
                    freq[dict]+=1
                else:
                    freq_dict[char]=1
            return freq_dict

        dict1=freq(self.string_a)
        dict2=freq(self.string_b)
        for keys in dict1.keys():
            if dict1[keys]!=dict2[keys]:
                return False
        return True

'''
python one-liner:

from collections import Counter
return True if Counter(string_a) == Counter(string_b) else return False
'''

s1="abc"
s2="dcab"
obj=Check_permutation(s1,s2)
print(obj.is_perm())
