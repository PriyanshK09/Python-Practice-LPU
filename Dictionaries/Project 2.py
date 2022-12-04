# Nested Dictionary in Python : A dictionary can also contain another dictionary. This is called nested dictionary.
myDictionary = {
    "class":{
        "student":{
            "name" : "abc",
            "marks" : {
                "python" : 90,
                "web" : 95
            }
        }
    }
}

a=myDictionary["class"]["student"]["marks"]["web"]
print("Marks in Web is: ", a)