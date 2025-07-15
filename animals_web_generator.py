import json

with open("animals_template.html", "r") as fileobj:
    html = fileobj.read()



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

    output = ""
    for name, diet, location, animal_type in zip(names, diets, locations, types):
        output += f"Name: {name}\n"
        if diet:
            output += f"Diet: {diet}\n"
        if location:
            output += f"Location: {location}\n"
        if animal_type:
            output += f"Type: {animal_type}\n"
        output += "\n"


    new_html = html.replace("__REPLACE_ANIMALS_INFO__", output)

if __name__ == "__main__":
    main()
