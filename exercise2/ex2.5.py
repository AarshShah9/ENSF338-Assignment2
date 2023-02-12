import urllib.request
import json
import random

with urllib.request.urlopen('https://raw.githubusercontent.com/ldklab/ensf338w23/main/assignments/assignment2/ex2.json') as inUrl:
    content = json.load(inUrl)
    
    randomized_arrays = []
    for array in content:
        random.shuffle(array)
        randomized_arrays.append(array)
    
    with open("randomized_arrays.json", "w") as file:
        json.dump(randomized_arrays, file)
    




