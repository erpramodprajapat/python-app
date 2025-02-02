import time

def profiler(func):
    ''''Print the runtiume of a function'''
    def wrapper_timer(*args,**kwargs):
        start_time=time.perf_counter()
        value=func(*args,**kwargs)
        end_time=time.perf_counter()
        run_time=end_time-start_time
        print(f"Finised {func.__name__} in {run_time:.4f} seconds") #f-string
        return value
    return wrapper_timer



@profiler
def alogrithm(num_times):
    for _ in range(num_times): #throw away variables
        sum([i**2 for i in range(10000)]) #compreshension


alogrithm(1)
alogrithm(999)