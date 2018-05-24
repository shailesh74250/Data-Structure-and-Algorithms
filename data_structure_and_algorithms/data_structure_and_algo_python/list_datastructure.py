
# coding: utf-8

# In[1]:


# List
"""
The list is a most versatile datatype available in python which can be written as a list of comma-separated values (items)
between square brackets. Imortant thing about a list is that items in a list need not be of the same type.
"""


# In[5]:


# creating a list is as simple as putting different comma-separated values b/w square bracket
list1 = ['physics','chemistry','1997','2000']
list2 = [1,2,3,4,5]
list3 = ["a","b","c","d"]
print list1,list2,list3


# In[6]:


# Accessing values in lists
print list1[1]
print list2[2]


# In[7]:


# updating list
list1[1] = 'math'
print list1[1]


# In[8]:


# append element in list
list1.append('history')
print list1


# In[9]:


# delete list element
del list1[2]
print list1


# In[10]:


# delete entire list
del list1
print list1


# In[11]:


# basic operation in list
print len(list2) # length
list1 = [1,2,3,4]
print list1+list2 # concatenation
print list2*2 # repetition
print 3 in list2 # membership
for i in list2:  # Iteration
    print i

