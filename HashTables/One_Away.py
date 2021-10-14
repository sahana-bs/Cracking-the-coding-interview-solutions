'''
Three types of edits can be performed on a string. Insert, remote, replace.
Given a string, write a function to check if they are one edit(or zero edit) away


eg, pale,ple->true

Complexity:
Time: O(N)
Space: O(1) for all the varaibles declared. O(N) for the additional strings that we use

'''
class check_edits():
    def __init__(self,s1,s2):
        self.s1=s1
        self.s2=s2

    def is_same(self,str1,str2):
        if len(str1)!=len(str2):
            return False
        for i in range(len(str1)):
            if str1[i]!=str2[i]:
                return False
        return True

    def is_one_edit(self):
        count=0
        len1=len(self.s1)
        len2=len(self.s2)
        ss1=self.s1
        ss2=self.s2
        if (len1-len2)>1:
            return False
        elif (len1-len2)==0:   #strings are of same length, the only edit is replace
            for i in range(len(self.s1)):
                if self.s1[i]!=self.s2[i]:
                    count+=1
                    if count>1:
                        return False  #no point processing furthur
            if count<=1:
                return True #there is only one character difference or they are the same strings
        elif abs(len1-len2)==1:    #the insert edit can be performed
            longer_str=self.s1 if len(self.s1)>len(self.s2) else self.s2
            for i in range(len(longer_str)):   #don't have to check the lst one
                if i==len(longer_str)-1:
                    return True
                if self.s1[i]!=self.s2[i]:
                    if len1>len2:
                        ss2=self.s2[:i]+self.s1[i]+self.s2[i:]   #cause I don;t think there is an insert string and strings are immutable
                    else:
                        ss1=self.s1[:i]+self.s2[i]+self.s1[i:]
                    break
            return(is_same(self,ss1,ss2))


        else:    #to use remove edit here
            smaller_str=s1 if len1>len2 else self.s2
            for i in range(len(smaller_str)):
                if self.s1[i]!=self.s2[i]:
                    if len1<len2:
                        ss2=self.s2[:i]+self.s2[i+1:]   #cause I don;t think there is an insert string
                    else:
                        ss1=self.s1[:i]+self.s1[i+1:]
                    break
            return(is_same(self,ss1,ss2))

s1="palo"
s2="bale"
obj=check_edits(s1,s2)
print(obj.is_one_edit())
