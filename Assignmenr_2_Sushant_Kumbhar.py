#!/usr/bin/env python
# coding: utf-8

# ## Assignment 2_Sushant Kumbhar

# In[22]:


#Question 1

def is_palindrome(x):
    pass
    b = [] # Creating empty list b
    c = [] # creating empty list c
    a = list(str(x)) # storing input x in list a
    b = a[:len(a)//2]  # storing half of the list in b
    if len(a)% 2 == 0:  # using if condition to check if half of the string is same as the other half
        c = a[len(a)//2:] 
    else:
        c = a[len(a)//2+1:][::-1]
    if b == c:
        return True
    else: 
        return False   


# In[23]:


# Question 2

def is_anagrams(s, t):
    string_list1 = [] # creating empty list for string s
    for i in s.lower():
        string_list1.append(i) #storing string s in list
        
    string_list2 = [] # creating empty list for string t
    for j in t.lower():
        string_list2.append(j) #storing string t in list

    string_dict1 = {} # Creating empty dictionary
    for j in string_list1: # storing the elements of string s in empty dictionary and calculating the frequency as value
        if j not in string_dict1:
            string_dict1[j] = 1
        else:
            string_dict1[j] = string_dict1[j] + 1
    
    string_dict2 = {} # Creating empty dictionary
    for k in string_list2:  # storing the elements of string t in empty dictionary and calculating the frequency as value
        if k not in string_dict2:
            string_dict2[k] = 1
        else:
            string_dict2[k] = string_dict2[k] + 1
 
    if string_dict1 == string_dict2: # Checking if two dictionaries are equal
        return True
    else:
        return False
    
    pass


# In[24]:


# Question 3

def top_k_words(s,k):
    extra = [',',';','.'] # Creating list of special characters that could be present in the input string
    for i in s: # creating for loop to replace special characters to replace them with empty space
        if i in extra:
            s = s.replace(i, '')
    
    s = s.rstrip() # rstrip is used to remove spaces from the trailing of string

    s = " ".join(s.split()) # join function is used to remove consecutive spaces in middle of the input string
    
    ls = list(s.split(' '))

    d = {} # creating empty dictionary
    for j in ls: # Counting the frequency of the words and storing it in the dictionary
        if j not in d:
            d[j] = 1
        else:
            d[j] = d[j] + 1

    d = sorted(d, key = d.get, reverse = True) # sorting the dictionary in descending order of the frequency
    
    k_words = d[:k] # using k argument to slice the k required elements
    return k_words
    pass

#top_k_words("   i love python, he    love coding python. the course is about python. ", 2)


# In[25]:


# Question 4

def gradient_descent(x, y, m, c, epochs, L=0.001):
    
    for it in range(0,epochs):
        Dm = []
        Dc = []
        for i in range(len(x)):  # creating for loop to iterate through length of list x
            y_pred = (m * x[i][0]) + c
            Dm.append((x[i][0]*(y_pred-y[i])))  # appending new values of Dm for every iteration
            Dc.append((y_pred-y[i]))

        dm = sum(Dm)/len(Dm)
        dc = sum(Dc)/len(Dc)    

        m = m-(L*dm)
        c = c-(L*dc)

    return (m,c)

#gradient_descent([[0.18], [1.0], [0.92], [0.07], [0.85], [0.99], [0.87]], [[109.85], [155.72], 
#                   [137.66], [76.17], [139.75], [162.6], [151.77]],
#                   0,0,1)


# In[26]:


# Testing block

if __name__ == "__main__":  
    
    # Test Question 1
    
    print("\nQ1")
    q1_test1 = 121
    q1_test2 = -121
    q1_test3 = 0
    q1_answer1 = is_palindrome(q1_test1)
    q1_answer2 = is_palindrome(q1_test2)
    q1_answer3 = is_palindrome(q1_test3)
    print(q1_answer1 )
    print("right answer: True")
    print("--------------")
    print(q1_answer2)
    print("right answer: False")
    print("--------------")
    print(q1_answer3)
    print("right answer: True")

    
    print("\nQ2")
    q2_test1_s = "anagram"
    q2_test1_t = "nagaram"
    q2_answer1 =  is_anagrams(q2_test1_s, q2_test1_t)
    print(q2_answer1)
    print("right answer: True")

    print("--------------")
    q2_test2_s = "python"
    q2_test2_t = "py"
    q2_answer2 =  is_anagrams(q2_test2_s, q2_test2_t)
    print(q2_answer2)
    print("right answer: False")
    print("--------------")

    # test question 3
    print("\nQ3")
    q3_test1_s = "   i love python, he    love coding python. the course is about python. "
    q3_test1_k = 2
    q3_answer = top_k_words(q3_test1_s, q3_test1_k)
    print(q3_answer)
    print("right: answer:")
    print("['python', 'love']")

    print ("\nQ4")

    x = [[0.18], [1.0], [0.92], [0.07], [0.85], [0.99], [0.87]]
    y = [109.85, 155.72, 137.66, 76.17, 139.75, 162.6, 151.77]
    m = 0
    c = 0
    q4_epochs200 = 200
    q4_epochs500 = 500
    q4_epochs1000 = 1000
    q4_epochs2000 = 2000
    q4_epochs3000 = 3000
    q4_answer1 = gradient_descent(x,y,m,c,q4_epochs200)
    q4_answer2 = gradient_descent(x,y,m,c,q4_epochs500)
    q4_answer3 = gradient_descent(x,y,m,c,q4_epochs1000)
    q4_answer4 = gradient_descent(x,y,m,c,q4_epochs2000)
    q4_answer5 = gradient_descent(x,y,m,c,q4_epochs3000)
    print(q4_answer1)
    print("right answer:")
    print("17.724810647355827, 22.97599012903927")
    print("--------------")
    print(q4_answer2)
    print("right answer:")
    print("35.97890301691016, 46.54235227399102")
    print("--------------")
    print(q4_answer3)
    print("right answer:")
    print("52.816639894324545, 68.05971340716786")
    print("--------------")
    print(q4_answer4)
    print("right answer:")
    print("64.56549666509812, 82.46678636085996")
    print("--------------")
    print(q4_answer5)
    print("right answer:")
    print("67.42648874428104, 85.32444456113602")
    print("--------------")

