from jsonschema import validate
# from json_schema import location
import json
from pprint import pprint

schema = {
     "type" : "object",
     "properties" : {
         "price" : {"type" : "number"},
         "name" : {"type" : "string"},
     },
 }

instance={
    "name":"eggs",
    "price":'12'
}


res=validate(instance=instance, schema=schema)
1==1