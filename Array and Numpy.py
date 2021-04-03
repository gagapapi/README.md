#!/usr/bin/env python
# coding: utf-8

# In[128]:


d = {'k1':10,
     'k2':'stringy',
     'k3':[1,2,3,],
     'k4':{'inside_key':[20,30,40, {"keyinside": [60,20, "thirty"]}]}}


# In[129]:


d["k4"]["inside_key"][3]["keyinside"][1:]


# In[130]:


d['k1']


# In[132]:


d['k3'][0]


# In[133]:


d['k4']


# In[134]:


d['k4']['inside_key']


# In[135]:


short_names = {"AAU": "Ambrose Alli University",
             "OAU": "Obafemi Awolowo University",
             "UNILAG": "University of Lagos",
             "NDA": "National Defence Academy"}


# In[136]:


short_names['AAU']


# In[137]:


pop_in_mil = {"Nigeria": 180,
              "USA":323,
              "Germany": 83,
              "India": 1324}


# In[138]:


pop_in_mil['USA']


# In[141]:


short_names.values()


# In[142]:


short_names.keys()


# In[143]:


short_names.items()


# In[144]:


#Tuples are ordered sequences just like a list, but have one major difference, they are immutable. Meaning you can not change them. So in practice what does this actually mean? It means that you can not reassign an item once its in the tuple, unlike a list, where you can do a reassignment.


# In[145]:


t = (1,2,3)


# In[146]:


type(t)


# In[147]:


# Mixed data types are fine
t = ('a',1)


# In[148]:


t[0]


# In[150]:


mylist = [1,2,3]


# In[151]:


type(mylist)


# In[152]:


mylist[0] = 'new'


# In[153]:


mylist


# In[154]:


t = (1,2,3)


# In[155]:


t[0] = 'new'


# In[156]:


#Sets are an unordered collection of unique elements. We can construct them by using the set() function. Let's go ahead and make a set to see how it works:


# In[157]:


x = set()


# In[159]:


x.add(1)


# In[160]:


x


# In[163]:


x.add(2)


# In[164]:


x


# In[165]:


x.add(1)


# In[166]:


x


# In[167]:


mylist = [1,1,1,2,2,2,3,3,3,4,4,4]


# In[169]:


set(mylist)


# In[171]:


myset = {1,1,2,2,3,3}


# In[210]:


set(myset)


# In[222]:


if 1<2:
    print('1 is less than 2')


# In[223]:


if 1>2:
    print('1 is greater than 2')


# In[224]:


if 1==1:
    print('one is equal to one')
else:
    print('first if not true')


# In[ ]:


saved_password = '12345'
new_password = input("enter your password")

if int(new_password) == saved_password:
    print("password correct")
else:
    print("you are a criminal")


# In[1]:


#Numpy
import numpy as np


# In[3]:


a = [1,2,3,4]


# In[4]:


type(a)


# In[8]:


array_1d = np.array(a)
array_1d


# In[9]:


b = [2,4,6,7]


# In[14]:


array_2d = np.array(a),(b)
array_2d


# In[13]:


array_3d = np.array([[(20,40,60), (80,100,120), (140,160,180)]])
array_3d


# In[18]:


arr_zeros = np.zeros((3,4,5))
arr_zeros


# In[19]:


arr_ones = np.ones ((3,4))
arr_ones


# In[20]:


arr_full = np.full((3,3), 3)
arr_full


# In[21]:


test_array = np.array([(2,4,5), (5,6,7)])
test_array


# In[22]:


test_array.shape


# In[23]:


len(test_array)


# In[24]:


a = np.array([(2,4,5), (3,4,7)])
a


# In[25]:


a.ndim


# In[26]:


test_array.ndim


# In[29]:



temp_arr = np.array([[2,3,4], [3,4,6]])
temp_arr


# In[30]:


temp_arr[1]


# In[32]:


temp_arr[0]


# In[33]:


temp_arr[1,1:3]


# In[34]:


temp_arr[temp_arr == 4]


# In[35]:


temp_arr[temp_arr == 6]


# In[37]:


import numpy as np
np_height = np.array([1.87,  1.87, 1.82, 1.91, 1.90, 1.85])


# In[38]:


np_weight = np.array([81.65, 97.52, 95.25, 92.98, 86.18, 88.45])


# In[39]:


print(type(np_height))


# In[40]:


print(type(np_weight))


# In[45]:


bmi = np_weight / np_height ** 2


# In[46]:


print(bmi)


# In[47]:


bmi > 23


# In[48]:


print(bmi > 23)


# In[49]:


print(bmi[bmi > 23])


# In[50]:


weight_kg = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]


# In[51]:


import numpy as np


# In[52]:


np_weight= np.array([81.65, 97.52, 95.25, 92.98, 86.18, 88.45])


# In[58]:


np_weight_kg = np.array(weight_kg)


# In[59]:


np_weight_lbs = np_weight_kg * 2.2


# In[61]:


print(np_weight_lbs)


# In[6]:


import numpy as np


# In[10]:


from sklearn.model_selection import KFold


# In[1]:


Num_splits = 3


# In[12]:


data = np.array([[1,2], [3,4], [5,6], [7,8], [9,10]])


# In[13]:


kfold = KFold(n_splits=NUM_SPLITS)
split_data = kfold.split(data)


# In[ ]:




