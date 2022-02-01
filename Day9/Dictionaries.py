# Some complex example of Dictionaries # nested dictionaries
# sample dictionary
capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a list of dictionary

travel_vlog = {
    "France": ["Paris", "Lille", "Dijon"],
    "German": ["Berlin", "Hamburg", "Stuttgart"]
}

# Nesting dictionary in an dictionary
travel_vlog = {
    "France": {
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    "Germany": {
        "cities_visited":
            ["Berlin",
             "Hamburg",
             "Stuttgart"
             ],
        "total_budget": 12000
    }

}

print(travel_vlog.values())

# Item of dictionaries or Nesting dictionary in a list

travel_vlog = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited":
            ["Berlin",
             "Hamburg",
             "Stuttgart"
             ],
        "total_budget": 12000
    }

]
for items in travel_vlog:
    print(f"Travel vlog list : {items}")
