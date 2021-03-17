#!/usr/bin/env python
# coding: utf-8

# # ASSIGNMENT_1_Sushant_Kumbhar

# In[14]:


#1.1
str = 'python'       #1.1 Print string variable and print it
print(str)


# In[16]:


#1.2
str = 'I am a student'     #1.2 Define a string (I’m a student), print it.
print(str)


# In[17]:


#1.3  Defining a string
str = '''how do you think of this course?      
describe your feeling of this course'''         

print(str)


# In[18]:


#2.1
a = 100
b = 9
c = a + b
print(c)


# In[19]:


#2.2
print(a/b)


# In[20]:


#2.3
print(int(a/b)) #int function gives just the integer part


# In[23]:


#2.4
print(a%b) # % Arithmatic operator gives the remainder 


# In[24]:


#2.5

print(a**b)  # ** gives raised to the power of


# In[25]:


# 2.6
a == b  # == comparison operator compares if two are equal


# In[ ]:


# 2.7
a > b  # > comparison operator compares the two numbers


# In[26]:


#3.1
List_A = [100, 99.99, 'hello', 'world', 0, 0.1]  #Defining List_A
len(List_A)                   # Checking length of List_A


# In[27]:


# Using extend function to add elements in the list
List_B = ['hi', 'python', 3]

List_A.extend(List_B)    # Extinding List_A with List_B
print(List_A)


# In[35]:


# Usine append function to add a list as an element
List_A = [100, 99.99, 'hello', 'world', 0, 0.1]
List_B = ['hi', 'python', 3]
List_A.append(List_B)    # Appendign List_A with List_B
print(List_A)


# In[36]:


List_A.insert(1,'FE520')  # insert function inserts an element at given index
print(List_A)


# In[37]:


del List_A[1]  # del deletes an item from the list
print(List_A)


# In[38]:


#3.4
List_A


# In[39]:


List_A[-1] # gives the last value of list


# In[40]:


del List_A[-1]
List_A


# In[46]:


#3.5
List_C = List_A[2:] #slicing the list from third place 
List_C


# In[47]:


List_C = List_C*2 # Doubling the list
List_C


# In[48]:


#3.7
List_C[::-1] # Reversing the sequence from list starting from -1 index means last element


# In[50]:


# 4.1  Difining list A
A = [1,2,3,2,1,7]


# In[51]:


#4.2
counts = {}  # Creating empty dictionary
for i in A:  # Create for loop to iterate through List A
    if i in counts:  #Check if the element is present in count
        counts[i] = counts[i] + 1
    else:
        counts[i] = 1
print(counts)


# In[59]:


#5
A = [1,2,3,4,5,6,7,8,9]
avg = ()    # create an empty variable with integer value

count = 0   # set a counter eqlal to 0
for i in A:
    count+=1  
    avg = sum(A)/count  # Calculate average
print(avg)


# In[60]:


#6   For 1 iteration
x = [0.18, 1.0, 0.92, 0.07, 0.85, 0.99, 0.87]

y = [109.85, 155.72, 137.66, 76.17, 139.75, 162.6, 151.77]

m = 0
c = 0
L = 0.001

Dm = []       # creating emppty list for storing new values of Dm
Dc = []       # creating emp[ty lisr for storing new values of Dc

for i,z in zip(x,y):  # using zip function to iterate through pairs of values x and y
    y_pred = (m * i) + c
    Dm.append((i*(y_pred-z)))  # appending new values of Dm for every iteration
    Dc.append((y_pred-z))      ## appending new values of Dm for every iteration
              
dm = sum(Dm)/len(Dm)    #Taking average of Dm 
dc = sum(Dc)/len(Dc)    ##Taking average of Dc

m = m-(L*dm)
c = c-(L*dc)

print('m:',m)
print('c:',c)


# In[63]:


# For 200 iterations (Bonus question)

x = [0.18, 1.0, 0.92, 0.07, 0.85, 0.99, 0.87]

y = [109.85, 155.72, 137.66, 76.17, 139.75, 162.6, 151.77]

m = 0
c = 0
L = 0.001

for it in range(0,200):
    Dm = []
    Dc = []
    for i,z in zip(x,y):
        y_pred = (m * i) + c
        Dm.append((i*(y_pred-z)))
        Dc.append((y_pred-z))
    
    dm = sum(Dm)/len(Dm)
    dc = sum(Dc)/len(Dc)    

    m = m-(L*dm)
    c = c-(L*dc)
    
print('m after 200 iterations:',m)
print('c after 200 iterations:',c)


# In[ ]:




