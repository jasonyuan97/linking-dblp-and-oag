with open("dblp_venues.txt", "w") as target:
    id = 0
    with open("raw_dblp_venues.txt", "r") as source:
        for line in source:
            line = line.rstrip('\n')
            dictionary = {"id": id, "name": line} 
            target.write(str(dictionary)+"\n")
            id += 1
