#this is a pythonic implementation of the singleton pattern
class singleton(object):
    new_instance = None


    def __new__(cls):
        if cls.new_instance is None:
            print("Creating an object")

            cls.new_instance = super(cls).__new__(cls)
        return cls.new_instance


obj = singleton()
obj3 = singleton()
print(obj is obj3)
