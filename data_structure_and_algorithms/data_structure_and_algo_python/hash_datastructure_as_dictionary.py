
# coding: utf-8

# In[1]:


# Hash Table in Python
"""
Hash table stores Key-Value pairs but the key is generated through a hashing function.
So the Search and Insertion function of a data element becomes much faster as the key values
themselves becomes the index of the array which stores th data.
In Python, the Dictionary data types represent the implementation of hash tables.
"""


# In[3]:


# Declare a dictionary
dict = {'Name':'shailesh', 'Age':23, 'Class':'First'}

# Accessing the dictionary with its key
print "dict['Name']:",dict['Name']
print "dict['Age']:",dict['Age']


# In[4]:


# updating dictionary
dict['Age'] = 24
print "dict['Age']:",dict['Age']


# In[5]:


# delecte dictionary elements
del dict['Name'] # remove entry with key 'Name'
dict.clear() # remove all entries in dict
del dict # delete entire dictionary
print dict['Age']
print dict['Name']

