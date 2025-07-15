import json


def load_data(file_path):
    """ Loads a JSON file """
    with open(file_path, "r") as handle:
        return json.load(handle)


def find_names(data):
    return [animal["name"] for animal in data]


def find_diet(data):
    return [animal["characteristics"].get("diet", None) for animal in data]


def find_location(data):
    return [animal["locations"][0] if animal["locations"] else None for animal in data]


def find_type(data):
    return [animal["characteristics"].get("type", None) for animal in data]


def main():
    data = load_data("animals_data.json")

    names = find_names(data)
    diets = find_diet(data)
    locations = find_location(data)
    types = find_type(data)

    for name, diet, location, animal_type in zip(names, diets, locations, types):
        print(f"Name: {name}")
        if diet:
            print(f"Diet: {diet}")
        if location:
            print(f"Location: {location}")
        if animal_type:
            print(f"Type: {animal_type}")
        print()


if __name__ == "__main__":
    main()
