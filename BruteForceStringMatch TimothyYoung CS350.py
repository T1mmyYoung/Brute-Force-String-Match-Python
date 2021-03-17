import matplotlib.pyplot as plt
import numpy as np 
import logging
import random
import time
import timeit
##from timer import timer

##Implements Brute Force String Matching
##Input: An array T[0..n-1] of n characters representing text.
##       An array P[0..m-1] of m characters representing a pattern.
##Output: The index of the first character in the text that starts 
##        a matching substring or -1 if the search is unsuccesful.
def bruteForceStringMatch(t = [], p = []):
    n = len(t)-1
    m = len(p)-1

    diff = (n-m) +1
    

    for i in range(diff):
        j = 0
        while(j<m and p[j] == t[i + j]):
            j = j+1
            if j == m:
                return i
    return -1


##Pattern #1:##############################################
p = ['a','a'] ##pattern
t = ['e','g','b','a','a'] ##/text

n1 = len(p)
m1 = len(t)

total = 0
n = 100000
for i in range(n):
    tick = time.time()
    x = bruteForceStringMatch(t,p)
    tick1 = time.time()
    total += (tick1-tick)
total = total/n
##timeit.timeit(bruteForceStringMatch(t,p),number = 1000)
print(x)
print("Test Case1: %f miliseconds:" ,(total*1000))
print('\n')


##Pattern #2:##############################################
p = ['a','a'] ##pattern
t = ['a','a','b','c','b'] ##/text

n2 = len(p)
m2 = len(t)

total2 = 0
n = 100000
for i in range(n):
    tick = time.time()
    x2 = bruteForceStringMatch(t,p)
    tick1 = time.time()
    total2 += (tick1-tick)
total2 = total2/n
##timeit.timeit(bruteForceStringMatch(t,p),number = 1000)
print(x2)
print("Test Case2: %f miliseconds:" ,(total2*1000))
print('\n')

##Pattern #3:##############################################
p = ['a','a'] ##pattern
t = ['b','a','b','a','a','b'] ##/text

n3 = len(p)
m3 = len(t)

total3 = 0
n = 100000
for i in range(n):
    tick = time.time()
    x3 = bruteForceStringMatch(t,p)
    tick1 = time.time()
    total3 += (tick1-tick)
total3 = total3/n
##timeit.timeit(bruteForceStringMatch(t,p),number = 1000)
print(x3)
print("Test Case3: %f miliseconds:" ,(total3*1000))
print('\n')


##Pattern #4:##############################################
p = ['a','a','a','a'] ##pattern
t = ['c','b','b','c','a','a','a','a'] ##/text

n4 = len(p)
m4 = len(t)

total4 = 0
n = 100000
for i in range(n):
    tick = time.time()
    x4 = bruteForceStringMatch(t,p)
    tick1 = time.time()
    total4 += (tick1-tick)
total4 = total4/n
##timeit.timeit(bruteForceStringMatch(t,p),number = 1000)
print(x4)
print("Test Case4: %f miliseconds:" ,(total4*1000))
print('\n')


##Pattern #5:##############################################
p = ['a','a','a','a'] ##pattern
t = ['a','a','a','a','b','b','c','c'] ##/text

n5 = len(p)
m5 = len(t)

total5 = 0
n = 100000
for i in range(n):
    tick = time.time()
    x5 = bruteForceStringMatch(t,p)
    tick1 = time.time()
    total5 += (tick1-tick)
total5 = total5/n
##timeit.timeit(bruteForceStringMatch(t,p),number = 1000)
print(x5)
print("Test Case5: %f miliseconds:" ,(total5*1000))
print('\n')


##Pattern #6:##############################################
p = ['a','a','a','a'] ##pattern
t = ['b','b','a','a','a','a','c','c'] ##/text

n6 = len(p)
m6 = len(t)

total6 = 0
n = 100000
for i in range(n):
    tick = time.time()
    x6 = bruteForceStringMatch(t,p)
    tick1 = time.time()
    total6 += (tick1-tick)
total6 = total6/n
##timeit.timeit(bruteForceStringMatch(t,p),number = 1000)
print(x6)
print("Test Case6: %f miliseconds:" ,(total6*1000))
print('\n')
############################################################

##Pattern #7:##############################################
p = ['a','a','a','a','a','a','a','a'] ##pattern
t = ['c','b','b','c','a','b','b','a','a','a','a','a','a','a','a','a'] ##/text

n7 = len(p)
m7 = len(t)

total7 = 0
n = 100000
for i in range(n):
    tick = time.time()
    x7 = bruteForceStringMatch(t,p)
    tick1 = time.time()
    total7 += (tick1-tick)
total7 = total7/n
##timeit.timeit(bruteForceStringMatch(t,p),number = 1000)
print(x7)
print("Test Case7: %f miliseconds:" ,(total7*1000))
print('\n')


##Pattern #8:##############################################
p = ['a','a','a','a','a','a','a','a'] ##pattern
t = ['a','a','a','a','a','a','a','a','c','b','b','c','a','b','b','a'] ##/text

n8 = len(p)
m8 = len(t)

total8 = 0
n = 100000
for i in range(n):
    tick = time.time()
    x8 = bruteForceStringMatch(t,p)
    tick1 = time.time()
    total8 += (tick1-tick)
total8 = total8/n
##timeit.timeit(bruteForceStringMatch(t,p),number = 1000)
print(x8)
print("Test Case8: %f miliseconds:" ,(total8*1000))
print('\n')


##Pattern #9:##############################################
p = ['a','a','a','a','a','a','a','a'] ##pattern
t = ['a','b','b','c','a','a','a','a','a','a','a','a','a','b','b','a'] ##/text


n9 = len(p)
m9 = len(t)

total9 = 0
n = 100000
for i in range(n):
    tick = time.time()
    x9 = bruteForceStringMatch(t,p)
    tick1 = time.time()
    total9 += (tick1-tick)
total9 = total9/n
##timeit.timeit(bruteForceStringMatch(t,p),number = 1000)
print(x9)
print("Test Case9: %f miliseconds:" ,(total9*1000))
print('\n')
############################################################
labels = ['1*(mn)','2*(mn)','3*(mn)']
plot1 = [total,total4,total7]
plot2 = [total2,total5,total8]
plot3 = [total3,total6,total9]




x = np.arange(len(labels))
width = 0.35

fig, ax = plt.subplots()
rects1 = ax.bar(x - width/3, plot1, width, label = 'Case1:Worst-Case')
rects2 = ax.bar(x + width/3, plot2, width, label = 'Case2:Best-Case')
rects3 = ax.bar(x + 2*width/3, plot3, width, label = 'Case3:Average-Case')

ax.set_ylabel('Avg. Runtime:')
ax.set_title('Brute Force String Match Time Analysis(mn)')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(('{}'.format(height)),
        xy=(rect.get_x() + rect.get_width()/3,height),
        xytext=(0,3), # 3 points vertical offset
        textcoords = "offset points",
        ha='center',
        va = 'bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
fig.tight_layout()
plt.show()

