import json
# read in JSON from MOCK_DATA.json
# Note: JSON file generated at mockaroo.com
with open('MOCK_DATA.json','rb') as mock_json:
    my_clients_json_string = mock_json.read()
    my_clients_py_obj= json.loads(my_clients_json_string)
    print('Len of my object: ' + str(len(my_clients_py_obj)))
    for client in my_clients_py_obj:
        print(client)