#!/usr/bin/env python
# coding: utf-8

# In[3]:


flavors = ['vanilla', 'chocolate', 'cookie dough']
toppings = ['hot fudge', 'oroes', 'marshmallows']


# In[5]:


for first in flavors:
    for second in toppings:
        print(first, 'topped with some spicy', second)


# In[17]:


numbers = [0,1,2,3,4,5,6,7,8,9]
numbers2 = [1,2,3,4,5,6,7,8,9,0]
alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


# In[8]:


print(numbers)


# In[9]:


print(alphabets)


# In[20]:


#alphanumberic passwords can be hacked this way.

for figures in numbers:
    for figures2 in numbers2:
        for letters in alphabets:
            print(figures,figures2,letters)


# In[ ]:





# In[ ]:




