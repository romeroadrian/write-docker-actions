import requests
import random
import sys

# Make an HTTP GET request to the cat-fact API
cat_url = "https://catfact.ninja/fact"
r = requests.get(cat_url)
r_obj = r.json()

random_fact = r_obj["fact"]

# Print the individual randomly returned cat-fact
print(random_fact)

# Set the fact-output of the action as the value of random_fact
print(f"::set-output name=fact::{random_fact}")
