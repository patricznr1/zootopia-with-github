"""
Animals Web Generator
Reads animals from animals_data.json and generates animals.html
by replacing the __REPLACE_ANIMALS_INFO__ placeholder in animals_template.html
with HTML cards for each animal.
"""
import json


def load_data(file_path):
    """Loads a JSON file and returns the parsed content."""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """Serializes a single animal dict into one <li class="cards__item"> block."""
    output = '        <li class="cards__item">\n'
    name = animal.get("name", "Unknown")
    output += f'            <div class="card__title">{name}</div>\n'
    output += '            <p class="card__text">\n'
    characteristics = animal.get("characteristics", {}) or {}
    diet = characteristics.get("diet")
    if diet:
        output += f'                <strong>Diet:</strong> {diet}<br/>\n'
    locations = animal.get("locations") or []
    if locations:
        output += f'                <strong>Location:</strong> {locations[0]}<br/>\n'
    a_type = characteristics.get("type")
    if a_type:
        output += f'                <strong>Type:</strong> {a_type}<br/>\n'
    output += '            </p>\n'
    output += '        </li>\n'
    return output


def main():
    animals = load_data("animals_data.json")

    with open("animals_template.html", "r", encoding="utf-8") as handle:
        template = handle.read()

    cards = ""
    for animal in animals:
        cards += serialize_animal(animal)

    final_html = template.replace("__REPLACE_ANIMALS_INFO__", cards)

    with open("animals.html", "w", encoding="utf-8") as handle:
        handle.write(final_html)

    print("animals.html generated with " + str(len(animals)) + " animals.")


if __name__ == "__main__":
    main()
