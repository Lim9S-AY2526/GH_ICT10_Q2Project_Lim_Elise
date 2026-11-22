# Meet the creator using python data types
from pyscript import display, document

# String variables
full_name = "Elise Lauren Sevilla Lim"
grade_section = "Grade 10-Sapphire"
favorite_quote = "Believe you can and you're halfway there."

# Integer and float variable
age = 15
height_cm = 160.02

# List variable
hobbies_interests = [
    "Playing Games (Valorant & Roblox)",
    "Listening to Music",
    "Playing Volleyball",
    "Trying New Desserts"
]

# Tuple variable
dream_destinations = ("Maldives", "Italy", "Canada")

# Set variable
favorite_fruits = {"Mango", "Banana", "Dragonfruit", "Grapes", "Strawberry"}

# Dictionary variable
creator_details = {
    "Favorite Color": "Pink",
    "Go-To Snacks": "Nuggets, Taho, and Coffee Jelly",
    "Dream Career": "N/A",
    "Best Friend": "Misha"
}

hobbies_text = ", ".join(hobbies_interests)
destinations_text = ", ".join(dream_destinations)
fruits_text = ", ".join(sorted(favorite_fruits))

document.getElementById("creator_output").innerHTML = f"""
  <h4 class="text-center fw-bold mb-3">Hi! I'm <i>{full_name}</i></h4>
  <hr style="border-color: white;">
  <p><b>Grade & Section:</b> {grade_section}</p>
  <p><b>Age:</b> {age} years old | <b>Height:</b> {height_cm} cm</p>
  <p><b>Hobbies & Interests:</b> {hobbies_text}</p>
  <p><b>Dream Destinations:</b> {destinations_text}</p>
  <p><b>Favorite Fruits:</b> {fruits_text}</p>
  <p><b>Favorite Color:</b> {creator_details['Favorite Color']}</p>
  <p><b>Go-To Snacks:</b> {creator_details['Go-To Snacks']}</p>
  <p><b>Future Dream:</b> {creator_details['Dream Career']}</p>
  <hr style="border-color: white;">
  <p class="text-center fst-italic mb-0">"{favorite_quote}"</p>
"""