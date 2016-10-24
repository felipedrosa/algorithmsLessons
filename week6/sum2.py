# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 09:29:17 2016

@author: fn35029
"""

import sys

def make_dict(filename):
    """Read in the data stored in the text file and store them into a hash table (Python's dictionary)
    Input: filename - the name of the text file"""

    try: 
        f = open(filename, 'r')
    except IOError:
        sys.exit("No such file!")
    line_list = f.readlines()
    dic = {(int)(elem) for elem in line_list}
    return dic

def findNumTwoSum(dic):
    """Compute the number of target values t in the interval [2500,4000] (inclusive)
    such that there are distinct numbers x, y in the input file that satisfy x+y=t.
    
    Input: dic - a hash table contains all the numbers in the input file"""
    dic = sorted(dic)
    num_found = 0
    found = set()
    
    low = 0
    high = len(dic)-1
    target_upper = 10000
    target_lower = -10000
    while low<high:
        while low < high and dic[low]+ dic[high] < target_lower:
            low += 1
        while low < high and dic[low]+ dic[high] > target_upper:
            high -= 1
        this_sum = dic[low] + dic[high]
        if low < high and this_sum <= target_upper and this_sum >= target_lower:
            if this_sum not in found:
                found.add(this_sum)
            low += 1
    # for target in range(-10000,10001):
        # print "target: " + str(target)
        # low = 0
        # high = len(dic) - 1
        # while low < high:
            # while low < high and dic[low]+dic[high] < target:
                # low += 1
            # while low < high and dic[low]+dic[high] > target:
                # high -= 1
            # if low<high and dic[low]+dic[high] == target:
                # print "low_i: " + str(low) + "; low: " + str(dic[low])
                # print "high_i : " + str(high) + "; high: " + str(dic[high])
                # print "sum: " + str(dic[low]+dic[high])
                # num_found += 1
                # break
            # #low += 1
            # high -= 1
    print sorted(found)
    return len(found)
    
    # numSatisfied = 0 # the number of target values that passed the requirement
    # return sum(any(n - x in dic and 2*x != n for x in dic)
              # for n in range(-10000, 10001))
    # for target in range(-10000, 10001): # [2500, 4000]
        # print any(((target - x) in dic) and 2*x!=target for x in dic)
        # for x in dic:
            # y = target - x
            # if y in dic: # ensure dictinctness
                # numSatisfied += 1
                # print "found a pair"
    # return numSatisfied
    
def main():
    dic = make_dict("2sum.txt")
    print "finish reading"
    print len(dic)
    print findNumTwoSum(dic)
    
if __name__ == '__main__':
    main()
