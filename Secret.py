import json

jokes = {1: "Q. What did the penis say to the condom? A:\"Cover me. I'm going in.\"",
2: "Q: Why doesn't Santa have any children? A: He only comes once a year -- and when he does, it's down a chimney.",
3: "Q: Why can't a blonde count to 70? A: Because 69 is a bit of a mouthful.",
4: "Q: What is the definition of disgusting? A: Buying condoms from a secondhand shop.",
5: "Q: Why did the man put condoms on his ears during sex? A: He didn't want to get hearing aids.",
6: "Q: What should you do if you come across an elephant? A: Apologize and wipe it off.",
7: "Q: What's the best time to fake an orgasm? A: When a Rottweiler is humping your leg.",
8: "A woman wearing a strapless gown and sporting a necklace with an airplane on it spotted a young man staring at her. She asked him, \"Were you admiring my airplane?\" He replied, \"No, I was admiring the landing field.\"",
9: "Q: What do you call a guy with a blue penis? A: A tight-fisted wanker.",
10: "Q: Why do elephants have four feet? A: In the animal kingdom, six inches just doesn't cut it."
}

with open('secret.txt', 'w') as outfile:
    json.dump(jokes, outfile, indent=4)

