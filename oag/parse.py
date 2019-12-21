import ast

pairs = set()
with open("venue_linking_pairs.txt", "r") as paired_data:
    for line in paired_data:
        dictionary = ast.literal_eval(line)
        pairs.add(dictionary["mid"])

with open("mag_venues.txt", "r") as source:
    with open("oag_venues.txt", "w") as target:
        for line in source:
            dictionary = ast.literal_eval(line)
            if(dictionary["id"] in pairs):
                normalized = {"id": dictionary["id"], "name": dictionary["NormalizedName"].lower()}
                target.write(str(normalized)+"\n")
