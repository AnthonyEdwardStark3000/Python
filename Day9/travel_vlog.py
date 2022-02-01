# Travel vlog lists
print("******************* Travel vlog *******************")
travel_vlog = [
    {
        "country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 12
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 1
    }
]

country = input("Enter the country name :")
cities_visited_count = int(input("Enter the cities visited count :"))
cities_visited = []
for i in range(0, cities_visited_count):
    city = input("Enter the visited city name :")
    cities_visited.append(city)
print(cities_visited)
total_visits = int(input("Enter the total number of visits : "))


def insertInto(country_visited, city, total_count):
    city_dictionary = {("country", "cities_visited", "total_visits"): (country_visited, city, total_count)}
    travel_vlog.append(city_dictionary)


insertInto(country_visited=country, city=cities_visited, total_count=total_visits)
print(travel_vlog)
