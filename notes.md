OPP
===============
custom itreator 

=====Genrator=====
1. genrator usages itreator internally
2. To improve peformance for big data(memory)
3. itreator will process all the data than it will give output
4. double the memory , one for storing the data and second for processing in itreator

====Decorator=========
1. attaching additional responsiblites to existing function/method/calls for different behviour
2. Extensibilites
3. cross cutting concer:
PAL(presenation access layer): client view
BAL (business access layer): BL
DAL(data access layer): DB access by defaul sqllite3
IAL(infrastruture access layer): Security, caching, logging, profiling , tracing ....

AOP(aspect oriented programming): 

====logging================
import logging

serverity level

DEBUG
INFO
WARNINGS
ERROR
CRITICAL    

===========
File system
POSIX program
w,w+,a,r,r+,bwbbr

fp=open('salves.txt')
    ------
fp.close()

Memory Leasks file, db,socket,process

context manager :with
with open(sales.txt,r) as fp
    ----
    ---------

Memory leaks will be handeled by context manager    

reader adn write reads or write line by line
dictReader and dictWrite : 