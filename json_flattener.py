
import json
from pprint import pprint

data = json.load(open('restaurants.json'))

#pprint(data)

example_dict = { 'key1' : 'value1',
                 'key2' : 'value2',
                 'key3' : { 'key3a': 'value3a' },
                 'key4' : { 'key4a': { 'key4aa': 'value4aa',
                                       'key4ab': 'value4ab',
                                       'key4ac': 'value4ac'},
                            'key4b': 'value4b'}
                }

def find_keys(d, value):
    for k,v in d.items():
        if isinstance(v, dict):
            p = find_keys(v, value)
            if p:
                return [k] + p
        elif v == value:
            return [k]


def nested_keys(d):
    yield d.keys()
    #print(d.values())
    for value in d.values():
        if isinstance(value, dict):
            for res in nested_keys(value):
                yield res


def flatten_json_immutable(d):

    for k,v in d.items():

        if isinstance(v, dict):

            p = flatten_json_immutable(d)

            if p:

                return [k]
        else:

            return [k]



#for keys in nested_keys(example_dict):
#	print (keys)


#print(example_dict['key4'])
#print(find_keys(example_dict,'value4ac'))
#print(flatten_json_immutable(example_dict))
#print(example_dict.keys())



d = {'abc':'abc','def':{'ghi':'ghi','jkl':'jkl'}}
for ele in d.values():
    if isinstance(ele,dict):
       for k, v in ele.items():
           print(k,' ',v)





