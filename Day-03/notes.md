
working with JSON data

REST API
Package: http calls
    requests
    urllib3
    httplib2

Json modules
    json.load()
    json.dump()
    json.dumps()

Serilazation and Deserrialization
    process of stroing the data from memory into file/DB or other
    Presisting the data

    Deserrialization
    reverse of Serilazation

Binary Serilazation/flattening/marshalling
    data will be in bits and bytes(0/1)
    for security, no can read
    size of file will be less
    transfer will be fast
    buildin pickle
    easy to use
    Disadnantage:pickling is the process of Serilzing python objects(listmdickt,tupple,custom type) by converting into bits and bytes
    Disadnantage: another process cannot be read

    pickle: pickledException , unpickleException

Databases connection
    python can connect any DB
    2 way to conenct
        SQL way
        ORM way: Object Relation mapping(Table- class of python)
            sqlalchemy -orm tool - save ,update,delete,fetch
