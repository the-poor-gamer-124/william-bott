# -*- coding: utf-8 -*-
import json

jokes = {1: "Are you related to yoda because yodalicious",
2: "Are you from Mexico because I think you’re the Juan for me",
3: "Are you Australian because you meet all of my koalafications",
4: "Are you a sea lion because I can sea you lion in my bed later",
5: "Are you a bank loan because you got my interest",
6: "Are you a cigarette because you’ve got a hot butt",
7: "So do you have a name or can I call you mine",
8: "If nothing lasts forever, will you be my nothing",
9: "Are you being a ghost for halloween, or are you just my boo",
10: "I can’t find a costume for halloween, can I just go as your boyfriend instead",
11: "You’re the only treat I want in my sack this halloween",
12: "Are you an archaeologist because I’ve got a large bone for you to examine",
13: "Are you the square root of -1 because you can’t be real",
14: "Are you a cat because you’re purrrfect",
15: "Are you a campfire because you’re hot and I want s’more",
16: "Do you smoke pot because weed be cute together",
17: "Is your dad a preacher cause you’re a blessing",
18: "If I had a star for every time you brightened my day, I’d have a galaxy in my hand",
19: "Do you like raisins cause you’re raisin this dick",
20: "Are you the bottom of my laptop cause you’re hot",
21: "Do you like Mexican beacuse let’s taco bout getting together",
22: "Did you sit in a pile of sugar because that ass is sweet"
}

with open('joke.json', 'w') as outfile:
    json.dump(jokes, outfile, indent=4)
