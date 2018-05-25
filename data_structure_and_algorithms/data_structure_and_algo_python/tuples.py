
# coding: utf-8

# In[1]:


# Tuples
"""
A tuple is a sequence of immutable Python objects. 
Tuples are sequences, just like lists. The differences between tuples and lists are,
the tuples cannot be changed unlike lists and tuples use parentheses,
whereas lists use square brackets.
"""


# In[2]:


# creating tuples
tup = ('hi','hello',1,2,5.67)
print tup


# In[3]:


# creating empty tuple
tup = ()


# In[5]:


# to write a tuple containing a single value you have to include a comma, even though there is only one value
tup = (20,)
print tup


# In[6]:


# Accessing value in tuple in as same as list
print tup[0]


# In[7]:


# updating tuples is not valid
tup[0] = 49 # gives error


# In[14]:


# we can append element in tuple
#tup.append(23)
# but we can add two or more tuples and assign into diff tuple
tup2 = (1,2,3)
tup3 = tup + tup2
print tup3


# In[17]:


# delete 
# removing individual tuple elements is not possible. 
tup1 = (1,2,3,4)
del tup1
print tup1

