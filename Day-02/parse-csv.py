'''
Load the emps.csv into memory and read all the data from file and remove email column
and remaining data write it another file
Use logging
'''

import csv

with open('C:\\py-tt\\Day-02\\emps.csv','r') as fr:
    csv_data=csv.DictReader(fr)
    with open('C:\\py-tt\\Day-02\\emps_op.csv','w') as fw:
        columns=['fname','lname']
        csvwriter=csv.DictWriter(fw,fieldnames=columns,delimiter=',',lineterminator='\n')
        csvwriter.writeheader()
        for line in csv_data:
            del line['email']
            csvwriter.writerow(line)

print('Processing done !!')            

