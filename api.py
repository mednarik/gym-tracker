import json

def write(filename: str, exercise: str, weight: int, reps: int) -> None:
    with open(filename, "r") as file:
        data = json.load(file)

    data[exercise] = {
        "weight": weight,
        "reps": reps,
    }

    
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def read(filename: str, exercise: str | None = None) -> dict:
    with open(filename, "r") as file:
        data = json.load(file)

    if exercise == None:
        return data
    else:
        output = data.get(exercise)

        if output is None:
            return {}
        else:
            return output