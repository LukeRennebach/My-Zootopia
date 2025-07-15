import json

# Read the HTML template file
with open("animals_template.html", "r") as fileobj:
    html = fileobj.read()

def load_data(file_path):
    """Load and return the JSON data from a file."""
    with open(file_path, "r") as handle:
        return json.load(handle)

def find_names(data):
    """Return a list of animal names."""
    return [animal["name"] for animal in data]

def find_diet(data):
    """Return a list of diets for the animals."""
    return [animal["characteristics"].get("diet", None) for animal in data]

def find_location(data):
    """Return a list of locations for the animals."""
    return [animal["locations"][0] if animal["locations"] else None for animal in data]

def find_type(data):
    """Return a list of types for the animals."""
    return [animal["characteristics"].get("type", None) for animal in data]

def write_new_html(html, output):
    """Write the modified HTML content to a new file."""
    new_html = html.replace("__REPLACE_ANIMALS_INFO__", output)
    output_path = "animals.html"
    with open(output_path, "w") as handle:
        handle.write(new_html)
    print(f"New HTML written to {output_path}.")

def main():
    """Main function to process animal data and generate HTML."""
    data = load_data("animals_data.json")

    # Extract data
    names = find_names(data)
    diets = find_diet(data)
    locations = find_location(data)
    types = find_type(data)

    # Prepare output HTML
    output = ""
    for name, diet, location, animal_type in zip(names, diets, locations, types):
        output += f'<li class="cards__item">\n'
        output += f'  <div class="card__title">{name}</div>\n'
        output += f'  <p class="card__text">\n'
        if diet:
            output += f'    <strong>Diet:</strong> {diet}<br/>\n'
        if location:
            output += f'    <strong>Location:</strong> {location}<br/>\n'
        if animal_type:
            output += f'    <strong>Type:</strong> {animal_type}<br/>\n'
        output += f'  </p>\n'
        output += f'</li>\n'

    # Write to the new HTML file
    write_new_html(html, output)

if __name__ == "__main__":
    main()
