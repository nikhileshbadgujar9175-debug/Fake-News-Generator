# 1 - Import the random module 
import random

# 2 - Create Subjects
subjects = [
    "The Prime Minister",
    "A famous Bollywood actor",
    "A group of scientists",
    "The school principal",
    "A mysterious billionaire",
    "A team of students",
    "The city mayor",
    "A popular YouTuber",
    "An unknown inventor",
    "A famous cricketer"
]

actions= [
    "announces a surprising discovery about",
    "accidentally invents",
    "plans to launch",
    "claims to have discovered",
    "organizes a secret event involving",
    "introduces a new technology for",
    "mysteriously disappears while investigating",
    "reveals a strange story about",
    "proposes an unusual project involving",
    "creates a record by experimenting with"
]

places_or_things = [
    "a smart city on the Moon",
    "a robot that can cook food",
    "an underwater research station",
    "a flying electric car",
    "a hidden laboratory in Mumbai",
    "a machine that predicts the weather",
    "a futuristic school in Pune",
    "a self-cleaning house",
    "a new planet beyond the solar system",
    "a fully automated village"
]

# 3 - start the headline genrator loop 

 
while True:
     subject = random.choice(subjects)
     action = random.choice(actions)
     place_or_thing = random.choice(places_or_things)

     headline = f"BREAKING NEWS: {subject} {action} {place_or_thing}"
     print("\n" + headline)
    
     user_input = input(
        "\nDo you want another headline? (yes/no): "
    ).strip().lower()

     if user_input == "no":
        print("Thank you for using the Fake News Generator!")
        break


#print goodbye meassage 
print("\nThanks for using the Fake News Headline Generator. Have a fun day")
#dir
#python .\Fake_News_Generator_2.py