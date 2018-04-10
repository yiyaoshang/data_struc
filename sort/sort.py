#/usr/bin/python3
#encoding=utf-8
__author="heathu"

from random import random
from json import dumps,loads

def dump_random_array(file='numers.json',size=10**4):
    fo = open(file,'w',1024)
    nulst = list()
    for i in range(size):
        nulst.append(int(random()*10**10))
    fo.write(dumps(nulst))
    fo.close()

def load_random_array(file='numers.json'):
    fo = open(file,'r',1024)
    try:
        numlst = fo.read()
    finally:
        fo.close()
    return loads(numlst)

from datetime import datetime

def execute(func):
    def inner(*args,**kwargs):
        begin = datetime.now()
        result = func(*args,**kwargs)
        end = datetime.now()
        inter = end - begin
        print('E-time:{0}.{1}'.format(inter.seconds,inter.microseconds))
        return result
    return inner
@execute
def bubble_sort(li):
    n = len(li)
    for j in range(0,n-1):
        for i in range(0,n-1):
            if li[i] > li[i+1]:
                tmp = li[i]
                li[i] = li[i+1]
                li[i+1] = tmp
    return li
@execute
def insert_sort(li):
    n = len(li)
    for i in range(0,n):
        for j in range(0,i):
            if li[i] < li[j]:
                li.insert(j,li.pop(i))
    return li
@execute    
def select_sort(li):
    n = len(li)
    for i in range(0,n):
        x = i
        for j in range(i,n):
            if li[x] > li[j]:
                x = j
        li[i],li[x] = li[x],li[i]
    return li  
@execute
def shell_sort(li):
    gap = len(li)
    while gap > 1:
        gap = gap // 2
        for i in range(gap,len(li)):
            for j in range(i % gap, i ,gap):
                if li[i] < li[j]:
                    li[i],li[j] = li[j],li[i]
    return li


@execute
def heap_sort(array):
    def heap_adjust(parent):
        child = 2 * parent + 1
        while child < len(heap):
            if child + 1 < len(heap):
                if heap[child+1] > heap[child]:
                    child += 1
            if heap[parent] >= heap[child]:
                break
            heap[parent],heap[child] = heap[child],heap[parent]
            parent,child = child,2*child+1
    heap,array=array.copy(),[]
    for i in range(len(heap)//2,-1,-1):
        heap_adjust(i)
    while len(heap) != 0:
        heap[0],heap[-1]=heap[-1],heap[0]
        array.insert(0,heap.pop())
        heap_adjust(0)
    return array

@execute
def quick_sort(li):
    def resursive(begin,end):
        if begin > end:
            return
        l,r = begin,end
        pivot = li[l]
        while l < r:
            while l < r and li[r] > pivot:
                r -= 1
            while l < r and li[l] <= pivot:
                l += 1
            li[l],li[r]=li[r],li[l]
        li[l],li[begin]=pivot,li[l]
        resursive(begin,l-1)
        resursive(r+1,end)
    resursive(0,len(li)-1)
    return li

@execute
def merge_sort(array):
    def merge_arr(arr_l,arr_r):
        array = []
        while len(arr_l) and len(arr_r):
            if arr_l[0] <= arr_r[0]:
                array.append(arr_l.pop(0))
            elif arr_l[0] > arr_r[0]:
                array.append(arr_r.pop(0))
        if len(arr_l) !=0:
            array += arr_l
        elif len(arr_r) != 0:
            array += arr_r
        return array
    def recursive(array):
        if len(array) == 1:
            return array
        mid = len(array) // 2
        arr_l = recursive(array[:mid])
        arr_r = recursive(array[mid:])
        return merge_arr(arr_l,arr_r)
    return recursive(array)

#dump_random_array(size=10**4)
array = load_random_array()
print(len(array))
print('merge_sort ',merge_sort(array)==sorted(array))
print('quick_sort ',quick_sort(array)==sorted(array))
print('select_sort ',select_sort(array)==sorted(array))
print('bubble_sort ',bubble_sort(array)==sorted(array))
print('heap_sort ',heap_sort(array)==sorted(array))
print('shell_sort ',shell_sort(array)==sorted(array))
print('insert_sort ',insert_sort(array)==sorted(array))










