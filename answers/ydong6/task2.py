#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
Created on Mar 1, 2016
Task 2
There are several special types of dictionaries, including ordereddict, defaultdict, and Counter. In fact, Counter is built expressly for tasks similar to the one that I've laid out, above.

Using Counter from the collections module, write a program to count word usage
in the same text as above. Have this program print out, in decreasing order
(most common to least common) the 10 most common words and the count of each
word used. As always, your program should contain a main loop and an ifmain
statement, and it should be formatted correctly. @author: York
'''
'''
Created on Mar 1, 2016

@author: York
'''
from collections import Counter
def histogram(s):
    d=dict()
    for c in s:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    return d


def function1():
    my_string='''Stars burn a very light type of air that is packed very tight in the middle of the star. The tiny pieces of the air join to form a slightly heavier type of air that can't burn in the star without the middle being much hotter and tighter.After a long time, all the very light air in the middle is used up. Then the star gets much hotter and tighter in the middle, so it can burn the slightly heavier air. It also also gets much bigger and cooler outside. But it is still so hot it will burn up any close-in worlds.The sun is a star and will do this after a very long time. It will get so big that it will burn our world all up. This will not happen for at least ten hundred hundred hundred hundred years, so we don't have to worry about it now.Long after that, a star like the sun will burn up all the slightly heavier air, too. Then it will become very tiny and hot and white, but will be so tiny it won't be able to keep its worlds warm. It will keep cooling off over a very very long time. The worlds that are left will be all ice.But stars that are heavier can go on to burn heavier and heavier things, until finally they make the biggest flash we know. That is their end.'''
    lower=(my_string.lower())
    l=lower.split(' ')
    n=histogram(l)
    result=Counter(n).most_common(10)
    return result

    
def main():
    function1()
    print(function1())

         
    
if __name__ == "__main__":
    main()