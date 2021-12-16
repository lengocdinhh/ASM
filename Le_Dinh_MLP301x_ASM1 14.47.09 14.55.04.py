#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import numpy as np


# In[2]:


filename = input("Enter a filename: ")
file = 'Documents/MLP301x_asm1_dinhlnFX14191/Data Files/' + filename + '.txt'
try:
    with open(file,'r') as f:
        print('Successfully opened ' + filename +'.txt')
except:
    print('File cannot be found')


# In[3]:


score = 0
list_score = []
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answer_key = answer_key.split(',')
# đếm số dòng
line_count = 0
with open(file,'r') as f:
    for line in f:
        if line != '\n':
            line_count +=1
print('Total line of data:',line_count)


# In[4]:


count_valid = 0
count_invalid = 0
arr1 = ''
arr2 = ''
with open(file,'r') as fclass:
    for line in fclass:
        myList = line.replace('\n','').split(',')
        name = myList[0] # lấy phần tử đầu
        str_name = name[0] # lấy kí tự đầu
        str_id = name[1:len(name)] # lưu chuỗi số
        if len(myList) != 26:
            print('Invalid line of data: does not contain exactly 26 values:')
            count_invalid += 1
            for i in myList:
                arr1 += str(i) + ','
            print(arr1[:-1]) # in ra dòng lỗi
            arr1 = ''
        elif (len(myList) == 26) & (str_name == 'N') & (len(str_id) == 8) & (str_id.isdecimal() == True):
            count_valid += 1
            for j in range(25):
                if (myList[j+1]) == (answer_key[j]): # chấm điểm
                    score += 4
                elif((myList[j+1]) == ''):
                    score += 0
                else:
                    score += -1
            list_score.append(score)
            score = 0      
        else:
            print('Invalid line of data: N# is invalid:')
            count_invalid += 1
            for index in myList:
                arr2 += str(index) + ','
            print(arr2[:-1])# in ra dòng lỗi
            arr2 =''
print('Total valid lines of data:',count_valid)
if (count_invalid == 0):
    print('No errors found!')
else:
    print('Total invalid lines of data:',count_invalid)


# In[5]:


print('Mean (average) score:', sum(list_score)/len(list_score))
print('Highest score:', max(list_score))
print('Lowest score:', min(list_score))
print('Range of scores:', max(list_score)-min(list_score))
n = len(list_score)
newList = sorted(list_score) # sắp xếp 
if (n % 2 == 0):
    median = (newList[n//2 - 1] + newList[n//2])/2
    print('Median score:',median)
else:
    print('Median score:',newList[(n+1)//2])


# In[6]:


index = 0
fileGrades = 'Documents/MLP301x_asm1_dinhlnFX14191/Expected Output/' + filename + '_grades' + '.txt'
with open(file,'r') as fclass:
    with open(fileGrades,'w') as fgrades:
        for line in fclass:
            myList = line.replace('\n','').split(',')
            name = myList[0]
            str_name = name[0] 
            str_id = name[1:len(name)] 
            if(len(myList) == 26) & (str_name == 'N') & (len(str_id) == 8) & (str_id.isdecimal() == True):
                fgrades.write(name + ',' + str(list_score[index]) + '\n')
                index += 1


# In[7]:


with open(fileGrades,'r') as fgrades:
    for line in fgrades:
        print(line)


# In[ ]:




