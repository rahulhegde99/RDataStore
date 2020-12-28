import sys
import json
import time
import threading

ds = dict()
class RDataStore():
    # CREATE OPERATION
    def create(self, key, value, ttl = 0):
        value = str(value)
        key = str(key)

        # dictionary should be under 1GB and value should be under 16KB
        if int(sys.getsizeof(ds)) >= (1024 * 1024 * 1024) or len(value) >= (16 * 1024):
            return "MEMORY_ERROR: Either value is over 16KB or the data store is over a 1GB"

        if key in ds:
            return "KEY_ERROR: Key already exists"

        if not RDataStore.is_json(value):
            return "VALUE_ERROR: Not a valid value. Value should be in JSON format"

        # key string should be capped at 32 chars
        key = key[:32]

        # add value pair to key
        value_pair = list()
        value_pair.append(value)
        value_pair.append(time.time() + ttl)
        ds[key] = value_pair
        return "Key sucessfully created"
    
    # READ OPERATION
    def read(self, key):
        key = str(key)
        if key not in ds:
            return "KEY_ERROR: Key does not exist"
        
        if time.time() > ds[key][1]:
            return "TTL_ERROR: You cannot read after Time-To-Live"

        return ds[key][0]

    # DELETE OPERATION
    def delete(self, key):
        key = str(key)
        if key not in ds:
            return "KEY_ERROR: Key does not exist"
        
        if time.time() > ds[key][1]:
            return "TTL_ERROR: You cannot delete after Time-To-Live"

        ds.pop(key)
        return "Key successfully deleted"

    # PRINT OPERATION
    def print_data(self):
        with open("data_store.json", "w") as outfile:
            json.dump(ds, outfile)

    def is_json(myjson):
        try:
            json_object = json.loads(myjson)
        except:
            return False
        return True       