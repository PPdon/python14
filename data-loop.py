student=[
{"name": "Joseph","score":85},
{"name": "James","score":70},
{"name": "Mary","score":90},
{"name": "Tony","score":65},
{"name": "Tuu","score":49},
{"name": "Pom","score":51},
]
for e in student:
    if e["score"] >= 80:
        print(e["name"],e["score"],"grade : 4")
    elif e["score"] >= 70:
         print(e["name"],e["score"],"grade : 3")
    elif e["score"] >= 60:
        print(e["name"],e["score"],"grade : 2")
    elif e["score"] >= 50:
        print(e["name"],e["score"],"grade : 1")
    else:
        print(e["name"],e["score"],"grade : 0")
#Peeradon Lordthong 15 6/14