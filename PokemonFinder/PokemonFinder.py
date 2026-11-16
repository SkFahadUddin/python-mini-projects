import requests

API = "https://pokeapi.co/api/v2/"


def get_data(endpoint):
    response = requests.get(f"{API}{endpoint}", timeout=15)
    response.raise_for_status()
    return response.json()


def title(value):
    return value.replace("-", " ").title() if value else "Unknown"


def evolution_names(link):
    names = [title(link["species"]["name"])]
    for next_link in link["evolves_to"]:
        names.extend(evolution_names(next_link))
    return names


def print_pokemon(pokemon):
    species = get_data(f"pokemon-species/{pokemon['species']['name']}")
    types = [entry["type"]["name"] for entry in pokemon["types"]]
    type_names = ", ".join(map(title, types))
    genus = next((entry["genus"] for entry in species["genera"]
                  if entry["language"]["name"] == "en"), "Unknown")
    generation = species["generation"]["name"]
    region = get_data(f"generation/{generation}")["main_region"]["name"]
    stats = {entry["stat"]["name"]: entry["base_stat"] for entry in pokemon["stats"]}
    stat_labels = {
        "hp": "HP", "attack": "ATK", "defense": "DEF",
        "special-attack": "SP. ATK", "special-defense": "SP. DEF", "speed": "SPD",
    }
    total = sum(stats.values())

    normal_abilities = [title(entry["ability"]["name"]) for entry in pokemon["abilities"]
                        if not entry["is_hidden"]]
    hidden_abilities = [title(entry["ability"]["name"]) for entry in pokemon["abilities"]
                        if entry["is_hidden"]]

    # Combine each type's defensive multipliers, including dual-type effects.
    multipliers = {}
    for type_name in types:
        relations = get_data(f"type/{type_name}")["damage_relations"]
        for key, factor in (("double_damage_from", 2), ("half_damage_from", .5),
                            ("no_damage_from", 0)):
            for defending_type in relations[key]:
                name = defending_type["name"]
                multipliers[name] = multipliers.get(name, 1) * factor
    weaknesses = [title(name) for name, factor in multipliers.items() if factor > 1]
    resistances = [title(name) for name, factor in multipliers.items() if 0 < factor < 1]
    immunities = [title(name) for name, factor in multipliers.items() if factor == 0]

    chain = get_data(species["evolution_chain"]["url"].replace(API, ""))
    evolution = " → ".join(evolution_names(chain["chain"]))
    varieties = ", ".join(title(item["pokemon"]["name"]) for item in species["varieties"])
    shiny_available = bool(pokemon.get("sprites", {}).get("front_shiny"))

    # Compare a bounded set of recent level-up moves using their power and accuracy.
    candidates = []
    for entry in pokemon["moves"]:
        level_moves = [detail for detail in entry["version_group_details"]
                       if detail["move_learn_method"]["name"] == "level-up"]
        if level_moves:
            candidates.append((max(d["level_learned_at"] for d in level_moves), entry["move"]))
    candidates.sort(reverse=True, key=lambda item: item[0])
    move_options = []
    seen = set()
    for _, move_ref in candidates[:15]:
        if move_ref["name"] in seen:
            continue
        seen.add(move_ref["name"])
        move = get_data(move_ref["url"].replace(API, ""))
        if move["power"] is not None:
            move_options.append(move)
    move_options.sort(key=lambda move: (move["power"], move["accuracy"] or 0), reverse=True)
    move_rows = [
        f"{title(move['name'])} (Power {move['power']}, Accuracy {move['accuracy'] or '—'})"
        for move in move_options[:5]
    ]

    highest = max(stats, key=stats.get)
    lowest = min(stats, key=stats.get)
    effort = ", ".join(f"{entry['effort']} {stat_labels.get(entry['stat']['name'], title(entry['stat']['name']))}"
                        for entry in pokemon["stats"] if entry["effort"])

    sections = [
        ("Identity", [f"Name: {title(pokemon['name'])}", f"ID: {pokemon['id']}",
                      f"Generation: {title(generation)}"]),
        ("Classification", [f"Type: {type_names}", f"Species: {genus}", f"Region: {title(region)}"]),
        ("Physical", [f"Height: {pokemon['height'] / 10:.1f} m",
                       f"Weight: {pokemon['weight'] / 10:.1f} kg"]),
        ("Stats", [f"{stat_labels.get(name, title(name))}: {value}" for name, value in stats.items()]),
        ("Overall", [f"Base Stat Total: {total}"]),
        ("Abilities", [f"Normal: {', '.join(normal_abilities) or 'None'}",
                       f"Hidden: {', '.join(hidden_abilities) or 'None'}"]),
        ("Type Matchups", [f"Weaknesses: {', '.join(weaknesses) or 'None'}",
                           f"Resistances: {', '.join(resistances) or 'None'}",
                           f"Immunities: {', '.join(immunities) or 'None'}"]),
        ("Battle", [f"Role: {title(highest)} focused (inferred from its highest base stat)",
                    f"Strength: Highest base stat is {stat_labels.get(highest, title(highest))} ({stats[highest]})",
                    f"Weak point: Lowest base stat is {stat_labels.get(lowest, title(lowest))} ({stats[lowest]})"]),
        ("Moves", move_rows or ["No damaging level-up moves with power data found"]),
        ("Training", [f"EV yield: {effort or 'None'}",
                       "IVs and Nature: Depend on the individual Pokémon; not species-wide values"]),
        ("Evolution", [evolution]),
        ("Special", [f"Legendary: {'Yes' if species['is_legendary'] else 'No'}",
                     f"Mythical: {'Yes' if species['is_mythical'] else 'No'}",
                     f"Shiny sprite available: {'Yes' if shiny_available else 'No'}",
                     f"Forms/varieties: {varieties}"]),
    ]

    for heading, lines in sections:
        print(f"\n{heading}")
        for line in lines:
            print(f"  {line}")


if __name__ == "__main__":
    name = input("Enter your Pokemon: ").strip().lower()
    try:
        print_pokemon(get_data(f"pokemon/{name}"))
    except requests.HTTPError as error:
        if error.response is not None and error.response.status_code == 404:
            print(f"Pokemon '{name}' was not found.")
        else:
            print(f"Pokemon API request failed: {error}")
    except requests.RequestException as error:
        print(f"Could not reach the Pokemon API: {error}")
