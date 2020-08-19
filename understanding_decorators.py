#Understanding Python Decorators
#Python Decorators Tutorial
# https://www.youtube.com/watch?v=nYDKH9fvlBY
# Video Deiscription
'''In this tutorial, I will explain decorators in a very simple way by going over how to measure the execution time of function using decorators.
They serve as a wrapper to original function but does a wonderful job of avoiding code duplication and not cluttering original code with additional logic.
The video discusses why there is a need of decorators, what is a decorator, how to create decorators and what is call repper function. '''


import time

def time_it (func): 
    def wrapper( *args, **kwargs): 
        start = time.time() 
        result = func ( *args, **kwargs) 
        end = time.time() 
        print (func.__name__ +" took " + str((end-start)*1000) + "mil sec")
        return result
    return wrapper

@time_it 
def calc_square (numbers) : 
    result = []
    for number in numbers : 
        result.append (number*number) 
    return result
               
@time_it 
def calc_cube (numbers) : 
    result = []
    for number in numbers : 
        result.append (number*number*number)
    return result


array = range(1, 100000)
out_square = calc_square(array)
out_cube = calc_cube(array)


