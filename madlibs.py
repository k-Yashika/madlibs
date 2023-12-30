# String concatenation (putting strings together)

adj1 = input("Adjective: ")
nationality = input("Nationality: ")
person = input("Person: ")
noun = input("Noun: ")
adj2 = input("Adjective: ")
noun2 = input("Noun: ")
adj3 = input("Adjective: ")
adj4 = input("Adjective: ")
pluralNoun = input("Plural Noun: ")
noun3 = input("Noun: ")
num = input("Number: ")
shapes = input("Shapes: ")
food = input("Food: ")
food2 = input("Food: ")
num2 = input("Number: ")


madlib = f"Pizza was invented by a {adj1} {nationality} \
chef named {person}. To make a pizza, you need to take a \
lump of {noun}, and make a thin, round {adj2} {noun2}. \
Then you cover it with {adj3} sauce, {adj4} cheese, and \
fresh chopped {pluralNoun}. Next you have to bake it in \
a very hot {noun3}. When it is done, cut it into {num} {shapes}. \
Some kids like {food} pizza the best, but my favourite is the {food2} \
pizza. If i could, I would eat pizza {num2} times a day."

print(madlib)
