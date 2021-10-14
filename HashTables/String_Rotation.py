'''
String Rotation:Assumeyou have a method isSubstringwhich checks if one word is a substring
of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
call to isSubstring(e.g.,"waterbottle"is a rotation of"erbottlewat").

Things I learnt coding this: not to use return to break from loops, use quit()


Complexities:
Time:O(N)  #to find the characters
Space:O(N)   #when length of substrin gis same as the actual string, in this case it will since we are checking for the rotation.

'''
def isSubstring(sub,super):
    #the simplest way to do this is to use the "in" operator---
    c=sub[0]
    i=0
    while super.find(c,i):
        index=super.find(c,i)
        sub_str=super[index:len(super)]
            #this if case if the substring  is in one piece of the super string
        if len(sub_str)==len(sub):
            if sub_str==sub:
                return True
                quit()
            return False
            quit()

            #else we need to rotate the suerstrin
        else:
            sub_str=super[0:index]+sub_str
            if sub_str==super:
                return True
                quit()
            return False
            quit()
        i=i+1

sub="rsupe"
super="super"
print(isSubstring(sub,super))
