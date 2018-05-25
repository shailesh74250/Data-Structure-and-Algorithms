
# coding: utf-8

# In[1]:


# Set datastructure in python
"""
Set is a collection of items not in any particular order.
* The elements in the set cannot be duplicates.
* The elements in the set are immutable (cannot be modified) but the set 
as a whole is mutable.
* There is no index attached to any element in a python set. So they do
not support any indexing or slicing operation.

The sets in python are typically used for mathematical operations like
union, intersection, difference and complement etc.
We can create a set, access it's elements and carry out these mathematical operations as shown below.
"""


# In[2]:


# A set is created by using the set() function or placing all the elements within a pair of curly braces.
Days = set(["mon","Tue","wed","Thu","Fri","Sat","Sun"])
Months = {"Jan","Feb","Mar"}
Dates = {21,22,17}
print(Days)
print(Months)
print(Dates)


# In[3]:


# Accessing values in a set
"""
We cannot access individual values in a set. We can only access all the
elements together as shown above. But we can also get a list of individual elements by looping 
through the set.
"""
Days = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
for d in Days:
    print(d)


# In[4]:


# Adding Items to a set
"""
We can add elements to a set by using add() method. Again as discussed there is no specific index 
attached to the newly added element.
"""
Days = set(["Mon","Tue","Wed","Thu","Fri","Sat"])
Days.add("Sun")
print(Days)


# In[6]:


# Removing item from a set
"""
We can remove elements from a set by using discard() method. Again as discussed
 there is no specific index attached to the newly added element.
"""
Days = {["Mon","Tue","Wed","Thu","Fri","Sat"]}
Days.discard("Sun")


# In[7]:


# Union of Sets
"""
The union operation on two sets produces a new set containing all the distinct
elements from both the sets. In the below example the element "Wed" is present in 
both the sets.
"""
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA|DaysB
print(AllDays)


# In[11]:


# Intersection of Sets
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA & DaysB
print(AllDays)


# In[13]:


# Difference of Sets
AllDays = DaysA - DaysB
print(AllDays)


# In[15]:


# Compare sets
"""
We can check if a given set is a subset or superset of another set. The
result is true or false depending on the elements preset in the sets.
"""
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes)
print(SupersetRes)

