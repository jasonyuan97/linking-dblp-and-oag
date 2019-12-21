import ast

def load_data(oag_path, dblp_path):
    oag_map = {} # venue_name->id
    with open(oag_path, "r") as oag:
        for line in oag:
            dictionary = ast.literal_eval(line)
            oag_map.update({dictionary["name"]: dictionary["id"]})

    dblp_map = {} # venue_name->id
    with open(dblp_path, "r") as dblp:
        for line in dblp:
            dictionary = ast.literal_eval(line)
            dblp_map.update({dictionary["name"]: dictionary["id"]})

    return oag_map, dblp_map

def pair(oag_map, dblp_map):
    with open("linked_venue_pairs.txt", "w") as target:
        # directly compare two names
        for d_venue in list(dblp_map.keys()):
            if d_venue in oag_map:
                dictionary = {"did": dblp_map.pop(d_venue), "oid": oag_map.pop(d_venue)}
                target.write(str(dictionary)+"\n") 

        # to handle abbrevations
        for d_venue in list(dblp_map.keys()):
            d_venue = d_venue.strip().lower()
            for o_venue in list(oag_map.keys()):
                o_venue = o_venue.strip().lower()
                if equals(d_venue, o_venue):
                    dictionary = {"did": dblp_map.pop(d_venue), "oid": oag_map.pop(o_venue)}
                    target.write(str(dictionary)+"\n") 
                    break
                    
def equals(d_venue, o_venue):
    if o_venue[0]!=d_venue[0]:
        return False

    S1 = d_venue.split(" ")
    S2 = o_venue.split(" ")
    if len(S1)!=len(S2):
        return False

    for i in range(len(S1)): 
        first = S1[i]
        second = S2[i]
        if first==second: continue
        first = first.replace(".", "")
        second = second.replace(".", "")
        if first.startswith(second) or second.startswith(first): continue
        return False

    return True

if __name__=='__main__':
    oag_path = "./oag/oag_venues.txt"
    dblp_path = "./dblp/dblp_venues.txt"

    oag_map, dblp_map= load_data(oag_path, dblp_path)
    pair(oag_map, dblp_map)
