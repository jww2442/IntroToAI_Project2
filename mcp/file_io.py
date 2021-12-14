import json
import os


def cmd_create_file(num_nodes):
    command = 'python .\problem_generator.py ' + str(num_nodes)
    os.system(command)

def open_gcp(filepath):
    
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data

cmd_create_file(50) #creates new gcp.json file of size = x nodes