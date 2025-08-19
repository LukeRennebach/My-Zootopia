import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("NINJAS_API_KEY")


def call_api(name):
    """Call the API with the given animal name."""
    api_url = (
        "https://api.api-ninjas.com/v1/animals?name={}".format(name)
    )
    response = requests.get(api_url, headers={"X-Api-Key": API_KEY})
    if response.status_code == requests.codes.ok:
        return response.json()
    print("Error:", response.status_code, response.text)
    return []


def load_template():
    """Read the HTML template file."""
    with open("animals_template.html", "r", encoding="utf-8") as fileobj:
        return fileobj.read()


def find_names(animals):
    """Return a list of animal names."""
    return [animal.get("name") for animal in animals]


def find_diet(animals):
    """Return a list of diets for the animals."""
    return [animal["characteristics"].get("diet") for animal in animals]


def find_location(animals):
    """Return a list of locations for the animals."""
    return [
        animal["locations"][0] if animal["locations"] else None
        for animal in animals
    ]


def find_type(animals):
    """Return a list of types for the animals."""
    return [animal["characteristics"].get("type") for animal in animals]


def write_new_html(html, output):
    """Write the modified HTML content to a new file."""
    new_html = html.replace("__REPLACE_ANIMALS_INFO__", output)
    output_path = "animals.html"
    with open(output_path, "w", encoding="utf-8") as handle:
        handle.write(new_html)
    print(f"Website was successfully generated to the file {output_path}.")


def create_new_html(animals):
    """Generate HTML list items for each animal."""
    names = find_names(animals)
    diets = find_diet(animals)
    locations = find_location(animals)
    types = find_type(animals)

    output = []
    for name, diet, location, animal_type in zip(
        names, diets, locations, types
    ):
        item = [
            '<li class="cards__item">',
            f'  <div class="card__title">{name}</div>',
            '  <p class="card__text">'
        ]
        if diet:
            item.append(f'    <strong>Diet:</strong> {diet}<br/>')
        if location:
            item.append(f'    <strong>Location:</strong> {location}<br/>')
        if animal_type:
            item.append(f'    <strong>Type:</strong> {animal_type}<br/>')
        item += ['  </p>', '</li>']
        output.append("\n".join(item))
    return "\n".join(output)


def main():
    """Process animal data and generate HTML."""
    name = input("Enter a name of an animal: ").strip().lower()
    if not name:
        print("No input provided.")
        return

    animals = call_api(name)
    html = load_template()
    output = create_new_html(animals)
    write_new_html(html, output)


if __name__ == "__main__":
    main()
