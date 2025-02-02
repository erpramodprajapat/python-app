class Head:
    def __init__(self,size=5):
        self.num=1

    def __iter__(self):
        return self
    
    def __next__(self):
        #write DB, REST API calls or local CSV (logic)
        if self.num<=5:
            val=self.num
            self.num +=1
            return val
        else:
            raise StopIteration
        

values=Head(6)
for i in values:
    print(i)

print(values.__next__())

