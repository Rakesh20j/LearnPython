#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("a")


# In[2]:


#comment
def function1(x):


# In[3]:


#comment
def function1(x):
    return 2*x
function1(3)


# In[8]:


a=function1(5)
print(a)


# In[9]:


function1()


# In[10]:


def function2(x,y):
    return x+y
function2(2,3)


# In[11]:


import sys
print(sys.version)


# In[12]:


print(sys.argv)


# In[13]:


import os
print(os.version)


# In[15]:


import os
print(os.getcwd())


# In[17]:


os.chdir("E:\homelab\python")


# In[18]:


print(os.getcwd())


# In[24]:


os.mkdir("E:\\homelab\\python\\test")


# In[25]:


os.rmdir("E:\\homelab\\python\\test")


# In[26]:


list 


# In[27]:


list module


# In[28]:


help(os)


# In[29]:


help(module)


# In[30]:


pydoc modules


# In[31]:


os.name


# In[32]:


help('modules')


# In[34]:


import crypto


# In[35]:


import cython


# In[36]:


help(cython)


# In[37]:


dir(cython)


# In[38]:


dir(os)


# In[39]:


os(getcwd())


# In[40]:


os.getcwd()


# In[41]:


os.getlogin()


# In[42]:


os.excel()


# In[43]:


os.execl()


# In[44]:


os.listdir()


# In[47]:


os.rmdir('E:\\homelab\\python\\practice')
os.mkdir('E:\\homelab\\python\\practice')
os.chdir('E:\\homelab\\python\\ptactice')


# In[48]:


os.rmdir('E:\\homelab\\python\\practice')


# In[52]:


os.mkdir('E:\\homelab\\python\\practice')
os.rmdir('E:\\homelab\\python\\practice')
os.mkdir('E:\\homelab\\python\\practice')
os.chdir('E:\\homelab\\python\\practice')


# In[2]:


os.getcwd()


# In[1]:


os.listdir()


# In[3]:


import os


# In[4]:


os.listdir()


# In[5]:


os.getcwd()


# In[7]:


os.chdir('E:\homelab\python\practice')


# In[8]:


os.getcwd()


# In[9]:


os.listdir()


# In[10]:


os.mkdir('practice1')


# In[11]:


os.listdir()


# In[12]:


os.mkdir('/practice2/practice3')


# In[13]:


os.makedirs('/practice2/practice3')


# In[14]:


os.listdir()


# In[15]:


os.getcwd()


# In[16]:


os.makedirs('practice2\\practice3')


# In[17]:


os.removedirs('practice2\\practice3')


# In[18]:


os.rmdir('practice1')


# In[19]:


os.makedirs('practice2//practice3')


# In[20]:


os.stat('test1.txt')


# In[21]:


os.stat('test1.txt').st_size


# In[22]:


import datetime


# In[23]:


os.stat('test1.txt').st_atime


# In[24]:


createtime = os.stat('test1.txt').st_atime


# In[29]:


datetime.fromtimestamp(createtime)


# In[28]:


from datetime import datetime


# In[32]:


for dirpath, dirname, filename in os.walk(os.getcwd()):
    print('current path:',dirpath)
    print('directories:', dirname)
    print('files', filename)


# In[33]:


dir(os)


# In[37]:


print(os.environ.get('HOME'))


# In[38]:


dir(os.path)


# In[42]:


os.path.isdir(os.getcwd())


# In[43]:


os.path.isfile(os.getcwd())


# In[57]:


if os.path.exists('practice\\practice2\\practice3'):
    print('path exist')


# In[58]:


os.getcwd()


# In[59]:


if os.path.exists('practice2\\practice3'):
    print('path exist')


# In[62]:


if os.path.exists('practice2\\practice3'):
    os.removedirs('practice2\\practice3')


# In[64]:


if os.path.exists('practice2\\practice3'):
    os.rmdir('practice2\\practice3')


# In[67]:


os.path.split('practice2\\new text document')


# In[68]:


os.path.dirname('practice2\\new text document')


# In[69]:


os.path.filename('practice2\\new text document')


# In[71]:


os.path.splitext('practice2\\new text document.txt')


# In[72]:


os.sys


# In[73]:


help(os)


# In[74]:


float(1.3)


# In[75]:


int(1.3)


# In[76]:


str(1)


# In[78]:


str(int(1.6))


# In[ ]:


input()


# In[ ]:


myname


# In[ ]:


name=input()


# In[4]:


def fact(x):
    print(x*(x-1))


# In[5]:


fact(3)


# In[1]:


print('2')


# In[8]:


num=input()
fact(int(num))


# In[9]:


a = [1,2,-1]


# In[10]:


a


# In[13]:


a.append('a')


# In[14]:


a


# In[17]:


a.pop()


# In[18]:


a


# In[19]:


a[0]


# In[21]:


b=[a,c,d]
b=[b[2],b[1],b[0]]


# In[22]:


a[2]


# In[23]:


a=["a","b","c"]


# In[25]:


for i in a:
    print(i)


# In[33]:


c=range(1,5) # range include numbers from 1 to 5, not including 5
print(c)
   


# In[34]:


for i in c:
    print(i)


# In[84]:


d=list(range(1,100))
sum=0
for i in d:
    if (i%3 ==0 or i%5==0):
        sum=sum+i
print(sum)


# In[45]:


print(sum)


# In[46]:


3+5+6+9+10+12+15+18


# In[50]:


3%3 #mod


# In[51]:


len(d)


# In[56]:


a=list(range(1,5))
i=1
while i<len(a):
    print(a)
    i+=1


# In[53]:


a


# In[54]:


len(a)


# In[60]:


list1=[1,2,3,-1,-2,2,-4]
sum1 = 0
i = 0
while list1[i] > 0:
    sum1=sum1+list1[i]
    i += 1
print(sum1)
    


# In[61]:


list2=[1,2,3,-1,-2,2,-4]
sum2=0
i=0
for e in list2:
    if e>0:
        sum2=sum2+list2[i]
    print(sum2)


# In[65]:


list2=[1,2,3,-1,-2,2,-4]
sum2=0
sum3=0

for e in list2:
    if e>0:
        sum2=sum2+e
    else:
        sum3=sum3+e
       
print(sum2)
print(sum3)


# In[78]:


def sum4(x,y,z):
    #return(x+y+z)
    print(x+y+z)


# In[81]:


g=sum4(1,2,3)
print(g)


# In[82]:


def sum5(x,y,z):
    return(x+y+z)
    #print(x+y+z)


# In[83]:


h=sum5(1,2,3)
print(h)


# In[ ]:




