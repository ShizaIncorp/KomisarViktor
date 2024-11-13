import os
import json


# TODO решите задачу
def task() -> float:
    a = os.listdir()
    way_json_obj = 'input.json'
    with open(way_json_obj) as f:
        pyton_obj = json.load(f)

    save_number = []
    for dict in pyton_obj:
        comp = dict["score"] * dict["weight"]
        save_number.append(comp)
    return sum(save_number)


print(f"{task():.3f}")
