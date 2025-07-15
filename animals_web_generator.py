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

def write_new_html(html, output):
    new_html = html.replace("__REPLACE_ANIMALS_INFO__", output)
    output_path = "animals.html"
    with open(output_path, "w") as handle:
        handle.write(new_html)
    print(f"New HTML written to {output_path}.")

def main():
    data = load_data("animals_data.json")

    names = find_names(data)
    diets = find_diet(data)
    locations = find_location(data)
    types = find_type(data)

    output = ""
    for name, diet, location, animal_type in zip(names, diets, locations, types):
        output += f'<li class="cards__item">\n'
        output += f"Name: {name}<br/>\n"
        if diet:
            output += f"Diet: {diet}<br/>\n"
        if location:
            output += f"Location: {location}<br/>\n"
        if animal_type:
            output += f"Type: {animal_type}<br/>\n"
        output += "</li>\n"

    write_new_html(html, output)

if __name__ == "__main__":
    main()
