PROBLEM STATEMENT: 

Consider telephone book database of N clients. Make use of a hash table implementation to quickly look up client‘s telephone number. 
Make use of two collision handling techniques and compare them using number of comparisons required to find a set of telephone numbers.

INPUT:

class hashtable:
	def __init__(self): //constructor of the hashtable class
		self.m=(int(input("enter the size of hash table")))
		self.hashTable=[none]*self.m
		self.elecount=0
		self.comparision=0
		print(self.hashTable)

#hash function
	def hashfunction(self,key):
		return key%self.m

#hash tableFull
	def isfull (self):
		if self.elecount==self.m:
		return True
	else:
		return False

#linear probing insert method(linearprobr)
	def linearprobr(self,key,data):
		index = self.hashFunction(key)
		compare=0
	while(self.hashFunction[index]!=none):
		index=index+1
		compare=compare+1
		if(index==self.m):
			index=0
	self.hashTable[index]=[key,data]
	self.elecount+=1
	print("data inserted at",index)
	print(self.hashTable)
	print("no. of comparisms=",compare)

#linear probing search method(getlinear)
	def getlinear(self,key,data):
		index = self.hashFunction(key)
	while self.hashTable[index] is not None:
		if self.hashTable[index]==[key,data]:
			return index
#key not found
	return None

#Quadratic probing insert method(quadraticprobr)
	def quadraticprobr(self,key,data):
		index = self.hashFunction(key)
		compare=0
		i=0
		while(self.hashTable[index]!=None):
			index=(index+i*i)%self.m
			compare=compare+1
			i=i+1
		self.hashTable[index]=[key,data]
		self.elecount+=1
		print("data inserted at ",index)
		print(self.hashTable)
		print("no of comparisms=",compare)

#qudratic probing search method (getQudratic)
	def getQudratic(self,key,data):
		index = self.hashTable[index] is not None
		i=0
		while self.hashTable[index]==[key,data]:
			if self.hashTable
			return index

#quadratic probing to search for the key 
	i=i+1
	index=(index+i*i)%self.m
#key not found
	return None

	def insertvialinear(self,key,data):
		if self.isfull():
			print("table is full")
		return False
		index = self.hashTable(key)
		
		if self.hashTable[index]=None
		self.hashTable[index]==[key,data]
		self.elecount+=1
		print("data inserted at",index)
		else:
			print("collision occured apply linear method")
			self.linear(key,data)

#insert using quadratic probing (insertQuadratic)
	def insertviaQuadratic(self,key,data):
		if self.isfull():
		print("table is full")
		return False
		index = self.hashTable(key)

		if self.hashTable[index]=None
		self.hashTable[index]=[key,data]
		self.elecount+=1
		print("data inserted at",index)
		print(self.hashTable)
		else:
			print("collision occured apply quadratic method")
			self.quadraticprobr(key,data)

def menu():
    obj=hashtable()
    
    ch=0
    while( ch!=3):
        print("********")
        print("1. Linear Probe    *")
        print("2. Quadratic Probe  *")
        print("3.Exit")
        print("********")

        ch = int(input("Enter Choice"))
        
        if ch==1:
        	
            ch2=0
            while(ch2!=3):
            	print("* Insert *")
            	print("* Search *")
            	print("* Exit *")
            	ch2=int(input("enter your choice"))
            	if ch2==1:
            		a=int(input("enter phone number"))
            		b=str(input("enter name"))
            		obj.insertvialinear(a,b) # Corrected line
            	elif ch2==2:
            		k=int(input("enter key to be searched"))
            		b=str(input("enter name"))
            		f=obj.getlinear(k,b)
            		if (f==None):
            			print("Key not found")
            		else:
            			print("key found at",f)
        elif ch==2:
            ch2=0
            obj1=hashtable()
            while(ch2!=3):
            	print("* Insert *")
            	print("* Search *")
            	print("* Exit *")
            	ch2=int(input("enter your choice"))
            	if ch2==1:
            		a=int(input("enter phone number"))
            		b=str(input("enter name"))
            		obj1.insertviaQuadratic(a,b) # Corrected line
            	elif ch2==2:
            		k=int(input("enter key to be searched"))
            		b=str(input("enter name"))
            		f=obj1.getQuadratic(k,b)
            		if (f==None):
            			print("Key not found")
            		else:
            			print("key found at",f)
																																										
menu()

