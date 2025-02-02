#Reader and writer

from csv import writer
from csv import reader


default_test='Some text'

with open('C:\\py-tt\\Day-02\\data.csv','r',) as read_obj:
    with open('C:\\py-tt\\Day-02\\data_op.csv','w',newline='') as write_obj:
        csv_reader=reader(read_obj)
        csv_writer=writer(write_obj)
        for row in csv_reader:
            row.append(default_test)
            csv_writer.writerow(row)