import pickle

jokes = {1: "",
2: "",
3: "",
4: "",
5: "",
6: "",
7: "",
8: "",
9: "",
10: ""
}


with open('joke.json', 'w') as outfile:
    json.dump(jokes, outfile, indent=4)