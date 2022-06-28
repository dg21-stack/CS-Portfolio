# Animal Shelter: In some animal shelter, you can only get the oldest animal, the oldest dog or oldest cat.

import random
class Node:
    def __init__(self, pet = True, val =[['Beagle','French Bulldog','Golden Doodle'], ['Persian','Maine Coon','British Shorthair']] ):
        self.next = None 
        self.prev = None
        self.pet = pet
        if pet:
            self.val = random.choice(val[0])
        else:
            self.val = random.choice(val[1])

# animal shelter class 

class animalShelter:
    def __init__(self):
        self.head = None 
        self.tail = None 
        self.dogfirst = False 

    # create the shelter 

    def createShelter(self,val):
        self.dogfirst = True if val else False
        node = Node(val)
        self.head = node 
        self.tail = node
        node.next = None 
        node.prev = None

    # add a pet 

    def enqueue(self,val):
        node = Node(val)
        self.tail.next = node 
        node.prev = self.tail
        self.tail = node
    
    # adopt a dog! 

    def dequeueDog(self):
        if self.dogfirst:
            self.dogfirst = self.head.next.pet
            breed = self.head.val
            self.head = self.head.next
            self.head.prev = None 
            return breed
        else: 
            curr = self.head
            while curr.pet is False:
                curr = curr.next
            breed = curr.val
            if curr is not self.tail:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                return breed
            else: 
                curr.prev.next = None
                return breed 

    # adopt a cat! 
            
    def dequeueCat(self):
        if self.dogfirst is False:
            self.dogfirst = self.head.next.pet
            breed = self.head.val
            self.head = self.head.next 
            self.head.prev = None 
            return breed
        else:
            curr = self.head
            while curr.pet is True:
                curr = curr.next 
            breed = curr.val
            if curr is not self.tail:
                curr.prev.next = curr.next 
                curr.next.prev = curr.prev
                return breed
            else:
                curr.prev.next = None 
                return breed
    
    # adopt either 

    def dequeueAny(self):
        self.dogfirst = self.head.next.pet 
        breed = self.head.val
        self.head = self.head.next 
        self.head.prev = None
        return breed

__name__ = "__main__"
# Test 

animal = animalShelter()
animal.createShelter(True)
animal.enqueue(False)
animal.enqueue(False)

print(animal.dequeueCat())
            
            

       
           
            