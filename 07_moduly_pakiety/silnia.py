#!/usr/bin/env python3
# Copyright SMAJKO

#Source: https://intel.udemy.com/course/programowanie-w-jezyku-python/learn/lecture/15723394?start=0#overview

import sys

def silnia(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * silnia(n-1)
    
if __name__ == '__main__':
    print('Uruchamiam siebie: {}'.format(silnia(sys.argv[1])))
