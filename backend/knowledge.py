import json


def load_json(path):

    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)



def load_major():

    return load_json("../data/major.json")


def load_school():

    return load_json("../data/school.json")