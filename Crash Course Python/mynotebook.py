#!/usr/bin/env python
# coding: utf-8

# # **Basic numbers and arithmatic**
# 1. Addition +
# 2. Subtraction -
# 3. Multiplication *
# 4. Division / ( version python > 2.7, returns floating point as result)
# 5. Raised to **
# 6. Mod %
# 7. Follows BODMAS/ PEMDAS rule

# In[5]:


1/1


# In[2]:


2**4


# In[3]:


2+2*5+5


# In[4]:


4%4


# # Variable declaration and definition 
# 1. Variable name cannot start with numbers
# 2. Variable name cannot start with special characters 
# 3. Variable name should start with lower case letters
# 4. Use underscore for name separation

# In[6]:


var =2


# In[7]:


var


# In[8]:


x=2
y=3


# In[9]:


x+y


# In[10]:


x=x+x


# In[11]:


x


# # Strings 
# 1. Single quote strings
# 2. Double quote strings
# 3. Double quote strings used for strings containing single quotes 
# 4. While declaring a variable with string value and printing the variable using print function, the 'out' symbol does not appear on the right hand side 
# 5. .format function used to format the string using variable names and then print function to print the formatted string
# 6. .format(one=num, two=name) style allows to add more variables without worrying about the order of the variables
# 7. Indexing in the string is done using [] brackets and indexing starts at 0
# 8. Slice notation [n:m] grabs slices of the string starting from n index upto m index, [:] gets the whole string, [:m] gets the string from start index i.e 0 upto m, [n:] gets the string starting at n index upto the last index

# In[12]:


'single quote string'


# In[13]:


"double quote string"


# In[15]:


"I can't go"


# In[16]:


x = 'My name is suman'


# In[17]:


print(x)


# In[19]:


num = 12
name= 'suman'
print('My number is {} and my name is {}' .format(num, name))


# In[21]:


'My number is {one} and my name is {two}' .format(two=name,one=num)


# In[22]:


s = 'hello'


# In[23]:


s[0]


# In[24]:


s[4]


# In[25]:


s[0:3]


# In[26]:


s[:]


# # Lists
# 1. Lists contains values separated by commas in square brackets
# 2. .append method to append value to list
# 3. indexing used to get value at a index from the list
# 4. slicing works for lists as well 
# 5. reassignment done using the indexing 
# 6. nested lists allowed [1,2,[3,4]]
# 7. indexing for nested list works as follows nest[2][1] 
# 8. lists can contain multiple types of data i.e. number, strings, characters etc

# In[27]:


mylist= [1,2,3]
mylist[0]


# In[28]:


mylist[2] =4


# In[31]:


mylist[1:4]


# In[33]:


nest_list= [1,2,3,['word','mine']]
nest_list[3][1]


# # Dictionaries
# 1. Created specifying d = {'key':value}, non-sequential, hold values using keys
# 2. indexing done using keys d['key']
# 3. value assigned to key could be list, strings, numbers etc. 
# 4. fetching list assigned to the key using key as an index and then using actual indexing to get values from the list assigned to the key.  example: d = {'key1':[1,2,3]} d['key1'][2] => should give us 3
# 5. nested dictionaries are possible where the value for the key is another key of the nested dictionary example: d{'key':{'inkey':'secret weapon'}}, fetching the value would be done by  d['key']['inkey'] 

# In[35]:


d = {'key1':[1,2,3]}
d['key1'][2]


# In[37]:


d= {'key':{'inkey':'secret weapon'}}
d['key']['inkey']


# In[39]:


d1= {'key':{'inkey':[2,3,4,5]}}
d1['key']['inkey'][3]


# # Booleans
# 1. Binary values, **T**rue or **F**alse 

# In[40]:


True


# In[41]:


False


# # Tuples
# 1. Tuple is similar to list, but instead of square brackets we use paranthesis 
# 2. Indexing in Tuples done using [] brackets like in lists
# 3. List reassignment works but in Tuple reassignment does not work 
# 4. Tuple is immutable and therefore items cannot be reassigned in Tuples. If tried the following error msg is shows **'tuple' object does not support item assignment**

# In[43]:


tup = (1,2,3)


# In[44]:


tup[2]


# In[45]:


tup[2]= [3,4,5]


# # Sets
# 1. Collection of unqiue elements, similar to dictionary i.e {} brackets
# 2. Duplicates are reduced to unqiue set of the elements 
# 3. set([1,1,1,1,3,3,3,3,4,4,4,5]) => returns list of unqiue elements 
# 4. .add method appends the element to exists list. Incase the same element is added again, no error message is displayed but only one entry of the duplicate element is retained in the set

# In[46]:


s ={1,3,4,4,4,5}
s


# In[47]:


s.add(6)
s


# In[48]:


s.add(6)


# In[49]:


s


# # Comparison operators <, >, ==, <=,>= , != 
# 1. comparison operators allow to compare two variables, number, strings
# 2. return boolean value 
# 3. == for comparison of equality 
# 
# 
# # Logic operators 'and' as well as 'or'
# 1. and => both conditions true for result to be true
# 2. or => one of the conditions true for result to be true
# 

# In[50]:


x=1
y=2
x>y


# In[51]:


x<y


# In[52]:


x==y


# In[53]:


x!=y


# In[54]:


x<y and x!=y


# In[55]:


x>y and x!=y


# In[56]:


x<y or x==y


# # Code blocks through If, elif, else 
# 1. code block execution depends on condition, code blocking achieved through use of if, elif and else statements
# 2. indention using space helps to do code blocking, done automatically
# 3. if(cond): 
#     do_something
# 4. if(cond):
#     do_something
#    else: 
#     do_something_else
# 5.  if(cond):
#         do_something
#     elif(cond):
#         do_something_2
#         .
#         .
#         .
#     else: 
#         do_something_else
#         
# 6. only first true condition is executed in a sqeuence of code blocks separated by if, elif, and else

# In[57]:


if 1<3:
    print('yes')


# In[59]:


if 1>3: 
    print('yes')
elif(2<3):
    print('elif 1 executed!')
elif(3<4):
    print('elif 2 executed!')
else:
    print("don't care!")
    


# # Iterators: For & While loop
# 1. for each item in the list/seq , we can repeat an action 
# 2. temp variable in the for statment can be anything but ideally should signfy datatype of the elements of the seq or list
# 3. while loop: perform an action until a condition remains true 

# In[1]:


seq=[1,2,3,4]
for i in seq: 
    print("hello")


# In[2]:


i = 1
while(i<5):
    print(i)
    i=i+1


# # Useful Python Functions
# 
# 1. **Range function**: used to avoid creating a sequence of things manually. Generating function for creating the sequence from the start to end i.e. range(start,end)
# 2. **list() function**: to create list from the given input ex: list(range(start,end))
#     
#     x= [1,2,3,4,5]
#     out=[]
#     for i in x:
#         out.append(i**2)
#     print(out)
#     
#     
# 3. **list comprehension**: way to save sometime in typing [i**2 for i in seq] 
# 4. function: avoid same instructions over and over again. Instead define a function and call it over and over again 
# 5. **Function created** by using keyword 'def':
# 
#     def funtion(param1):
#         print(param1)
#         
#     def my_func(name):
#         print('hello' + name)
#         
# 6. **Default values**: def function(parameter = **default_value**)
# 7. function call without paranthesis returns the type of object and to execute the function we need call the function with the paranthesis
# 
# 8. **Returning the value from function**: 
# 
#     def function(param):
#         return something
#         
# 9. **Documentation** / commenting in the function done using """ quotes at the beginning and at the end of comment. 
#    """
#        this is just a comment section
#    """
# 10. To understand the signature call of the function and the docstring describing the function, use shift + tab 
#              
#     
#                 

# In[6]:


x= [1,2,3,4,5]
out=[]
for i in x:
    out.append(i**2)
print(out)
[i**2 for i in x]


# # Lambda Expressions, Map & Filter 
# 
# 1. **Map function**:  apply some login/operation for every single element of the seq or list 
#     
#     def add_1(param):
#         return param+2
#     
#     x= [1,2,3,4,5]
#     
#     list(map(add_1,x)) """ to generate the list of elements from the map output """
# 
# 2. **Lambda expression** : Could skip the function definition using lambda expression:
#     
#     t= lambda param:param + 2 
#     
#     """ 
#         t is the variable to which the lambda expression is assigned. 
#         lambda expression created by replacing the def function_name with the word lambda. 
#         Passing the parameter as the argument i.e. lambda(param):, 
#         Followed by the: and instead of return, the value that should be returned ex: lambda(param):param*2
#     """
#       
#     list(map(t,x)) """ to generate the list of elements from the map output """
#     
#     **OR**
#     
#     list(map(lambda param:param + 2,x))
# 
# 
# 3. **Filter Function**: It similar structure map but instead of mapping, it function filters out elements from the     sequence 
# 
#     list(filter(lambda param: param%2 ==0, x))
#     
# 4. Lambda expression should always return boolean as return value, when used in Filter function
# 5. Filter function filters out the elements for which the lambda expression returns true

# In[12]:


def add_1(param):
    return param + 2

x= [1,2,3,4]
list(map(add_1,x))


# In[13]:


t= lambda param:param + 2 
list(map(t,x))


# In[14]:


list(map(lambda param:param + 2,x))


# In[15]:


list(filter(lambda param: param%2 ==0, x))


# # Methods
# 
# Methods provided by the object of the certain class which modify the object in some way or return some value 
# 
#    s = 'This is my string object'
#    
#    s.upper() => converts the whole string into upper case
#    
#    s.lower() => converts the whole string into lower case
#    
#    s.split() => splits the string into individual words when no input string give otherwise splits the string into sections before and after the input string 
#    
#    

# In[20]:


s = 'This is my string object and my string'
s.upper()
s.lower()
s.split('my')


# In[22]:


d={'k1': 1, 'k2': 2}
d.keys()


# # In Operator
# 
# 1. Used to check if certain element is present in the data container
#  
#    Example: 'x' in ['x','y','x']
# 
# 2. return true or false i.e. boolean return value

# In[23]:


'x' in ['x','y','x']


# # Tuple Unpacking
# 
# 1. To get elements from the list of tuples 
# 
#     x= [(1,2), (3,4), (5,4)]
# 
#     for item in x: 
#         print(item)
#         
#         
#     """ Tuple unpacking """
#     Instead of the item, extracting the tuple and then using the tuple or element of tuple individually
#     
#     for (a,b) in x: 
#         print(a,b)
#         print(a)
#         print(b)

# In[24]:


x= [(1,2), (3,4), (5,4)]

for item in x: 
    print(item)


# In[25]:


for (a,b) in x: 
    print(a,b)
    print(a)
    print(b)
    

