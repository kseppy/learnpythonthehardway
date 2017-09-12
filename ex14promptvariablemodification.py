from sys import argv

script, user_name, user_name_2, user_name_3 = argv
prompt = ' *  '

print(f"Hi {user_name}, I'm the {script} script.")
print(f"I'd like to ask {user_name_2} a few questions.")
print(f"Do you like {user_name_3}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"What kind of computer do you have, {user_name}?")
computer = input(prompt)

print(f"""
All right, so {user_name_2} said {likes} about liking {user_name_3}.
{user_name} lives in {lives}. 
And {user_name} has a {computer} computer. Nice.
""")