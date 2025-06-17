# dictionary with profile information 
my_profile = {
    "name": "shivani vyas",
    "age": 21,
    "height": 5.5,
    "hobbies": ["reading", "playing basketball", "travelling"],
    "skills": ["python", "css","html","js", "web development"],

}
# print each key and value using a loop 
print("My Profile Information:")
for key, value in my_profile.items():
    print(f"{key.capitalize()}: {value}")
