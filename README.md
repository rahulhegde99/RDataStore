# RDataStore
This is a complete Data Store with Create, Read, Delete and Print operations. It is implemented using Python.

## How to run?
- Clone this repository and use the `RData.py` module to use the CRD data store <pre>python RData.py</pre>
- Alternatively for checking this code, I have made an interactive program called `app.py` <pre>python app.py</pre>
- Unit tests are available in the `tests.py` module <pre>python -m unittest tests</pre>

## About the Data Store
Uses the python dictionary to store the key value pairs. However this process is complicated by the presence of Time-To-Live(TTL). Thus the data store skeleton looks like below.
<pre>
{
  key: [value, time_to_live],
}
</pre>

## Characteristic of the Data Store
### Creation Characteristics
- The data store throws an error when a duplicate key is created.
- The data store throws an error when the memory limit is exceeded.
- The data store throws an error when a non-JSON value is paired with a key.

### Read/Delete Characteristics
- The data store throws an error when a non-existent key is tried to be read/deleted.
- The data store throws an error when the Time-To-Live has expired and the key is tried to be read/deleted.

### Print Characteristics
- The data dictionary is printed in a JSON format in `data_store.json` when the print operation is called.

### You can reach me on:
[2]: https://www.linkedin.com/in/rahul-hegde-0955391a5/
[3]: https://rahulhegde.ml/
[5]: https://medium.com/@rahulhegde97

 [![linkedin](https://img.icons8.com/color/48/000000/linkedin.png)][2]
 [![website](https://img.icons8.com/fluent/48/000000/domain.png)][3]
 [![medium](https://img.icons8.com/color/48/000000/medium-monogram.png)][5]
 <a href="https://auth.geeksforgeeks.org/user/rahulhegde97/articles/"><img src="https://raw.githubusercontent.com/rahulhegde99/rahulhegde99/master/QNHrwL2q_400x400.jpg" width="40"></a>
