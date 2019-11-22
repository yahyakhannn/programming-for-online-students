#!/usr/bin/env python
# coding: utf-8

# In[1]:


print(input("Enter your Name"))
print(input("Enter your Class"))


# In[2]:


daily_list = ["emails", "survey", "complains"]
empty_list = []

print("My Daily List:")
print("**")
print(daily_list)

while (daily_list != []):
    user_input = input(" Enter a task that you have done in day: ")
    
    if user_input in daily_list :
        
        user_input_id = daily_list.index(user_input)
        empty_list.append(daily_list.pop(user_input_id))
        print(f"your remaining task is, {daily_list}")
        print(f"your completed task is, {empty_list}") 
    
    else:
        print('“This task is not in the to do list”')
print('“Now your list is empty”')


# In[3]:


la=(1,2,3,4,5,6)
print("length of list ",len(la))


# In[4]:


print("sum of list",sum(la))


# In[5]:


print("larger Number of List",max(la))


# In[6]:


print("less than 6",min(la))


# In[7]:


num=int(input("Enter Number: "))
print("")
if (num%2==0):
    print(f"{num} is even")
else:
    print(f"{num} is odd")


# In[8]:


num=int(input("Enter Number: "))
print("")
if (num%2==0):
    print(f"{num} is even")
else:
    print(f"{num} is odd")


# In[ ]:




