#Get user input for name, age, and years coding, and store in dictionary d
d = {"Name": input("Name: "), "Age": input("Age: "), "Years Coding": input("Years coding: ")}
langs = [input(f"{i}: Enter your") for i in ["First language", "Second language", "Third language"]]
favs = [input(f"{i} Enter your favorite language: ") for i in ["#1", "#2", "#3"]]
#Store first three programming languages as a tuple in dictionary d
d["first lang learned"] = tuple(langs)
d["favorite langs"] = favs
#Find intersection of first programming languages and favorite programming languages
intersect = set(langs).intersection(favs)
#Store intersection set as a value in dictionary d
d["favorite + first langs"] = intersect
for key, value in d.items():
    print(f"{key}: {value}")
