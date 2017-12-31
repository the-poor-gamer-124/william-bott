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

pickle_out = open("joke.pickle", "wb")
pickle.dump(jokes, pickle_out)

