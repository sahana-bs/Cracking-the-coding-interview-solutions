#source:pagekeysolutions.com/blog/dsa/hash-table-python/#:~:text=%20How%20to%20Implement%20a%20Hash%20Table%20in,It%20needs%20a%20size%2C%
'''
bucket is the list of linkedlists

This is the hash function, use any efficient hash funciton
Look into the poperties of hash funciton before choosing one
The property focused here is "uniformity"

This basically tells into which bucket the linked list goes (key:value pair)

next is the insert function:
to insert the key:value pair into the hash table
'''
class HashTable:
    def __init__(self):
        self.size = 0 #initial size
        self.capacity = 5 # the size of our internal array.
        self.buckets = [None]*self.capacity #this is the internal array, storing each inserted value in a “bucket” based on the provided key.

    def hash(self, key):
        hashsum=0
        for index, c in enumerate(key):
            hashsum+=(index+len(key))**ord(c)
            hashsum=hashsum%self.capacity
        #print("The hash value is ", hashsum)
        return hashsum

    def insert(self, key, value):
        self.size+=1
        index=self.hash(key)   #return the bucket
        node=self.buckets[index]

        if node is None:
            self.buckets[index]=Node(key, value)
            return

        #else traverse to the end of the LL and append the node
        prev=node
        while node is not None:
            prev=node
            node=node.next
        prev.next=Node(key,value)

    def find(self, key):
        index=self.hash(key)
        node=self.buckets[index]   #this is the linked list
        while node is not None and node.key!=key:
            node=node.next

        if node is None:
            return None
        return node.value

    def remove(self, key):
        index=self.hash(key)
        node=self.buckets[index]
        #now it is just removing an element from a linkedlist
        prev=None
        while node.next is not None and node.key!=key:
            prev=node
            node=node.next

        if node is None:
            print("Key not found!")
            return None
        #key found
        #self.find-=1-not using this since I've hardcoded the value of self.size
        res=node.value
        if prev is None: #last node
            node=None
        else:
            prev.next=prev.next.next
        print("The removed element is ",res)
        return res

    def PrintTable(self):
        for i in range(self.capacity):
            node=self.buckets[i]
            while node.next is not None:
                print("Key,value ", node.key," ",node.value)
                node=node.next
            print("Key,value ", node.key," ",node.value)


'''
Node is part of a linked list.
Each bucket will contain a linkedlist of nodes containing the objects stored at index
'''
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = next


ht = HashTable()
phone_numbers = ["555-555-5555", "444-444-4444"]  #this is the data
names=["John","Doe"]
ht.insert("phoneDirectory", phone_numbers)    #key is "phoneDirectory"
ht.insert("Names",names)
# Do whatever we need with the phone_numbers variable
phone_numbers = ht.find("phoneDirectory")
print(ht.PrintTable())
ht.remove("Names")
