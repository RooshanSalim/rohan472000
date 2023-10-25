country_capitals = {
    "United States": "Washington, D.C.",
    "Canada": "Ottawa",
    "Mexico": "Mexico City",
}

# Get the capital of the United States.
capital = country_capitals.get("United States")

# Add a new key-value pair to the dictionary.
country_capitals["Brazil"] = "Brasilia"

# Remove the key-value pair for Canada.
country_capitals.pop("Canada")

# Print all of the key-value pairs in the dictionary.
for country, capital in country_capitals.items():
    print(country, capital)
