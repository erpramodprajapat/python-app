import random
import time

names = ['Murthy', 'Kiran', 'Arun', 'Sita', 'Raj', 'Thomas']
majors = ['Math', 'Engineering', 'CompSci', 'Arts', 'Business']


def people_list(num_people):
    result = []
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        result.append(person)
    return result

def people_generator(num_people):
    for i in range(num_people):
        person = {
                    'id': i,
                    'name': random.choice(names),
                    'major': random.choice(majors)
                }
        yield person


t1 = time.process_time()
people = people_list(10000)
t2 = time.process_time()     
print("Time taken  with list :{} secs".format(t2-t1))


import gc
del people
gc.collect()
t1 = time.process_time()
people = people_generator(10000)
t2 = time.process_time()
print("Time taken with Generator :{} secs ".format(t2-t1))



