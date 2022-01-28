#get bit at a position i of a num
#101101, say i is 4
#1<<4 0001&101101
#so if the answer is true, the bit was 1 else 0
def get_bit(num, i):
    return ((num&(1<<i))!=0)

def set_bit(num, i):  #set a bit at position i as 1
    return num|(1<<i)

#1011101
#1011111  ~(1 << i)
#1011101
def clear_bit(num, i):  #clear bit at position i
    mask = ~(1 << i)
    return num & mask
