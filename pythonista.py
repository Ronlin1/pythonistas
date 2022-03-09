my_blog = "blog.octachart.com"

blog_len = len(my_blog)
if blog_len > 10:
    print(True)


my_blog = "blog.octachart.com"
if (blog_len := len(my_blog) > 10):
    print(True)

# The dir()
import pip
print(dir(pip))

# The * and ** operators
num_1 = [1,2,3,4,5]
print(*num_1)

# You can merge two lists;
num_2 = [6,7,8,9,10]
print([*num_1, *num_2])

new = []
for n1 in num_1:
    new.append(n1)

for n2 in num_2:
    new.append(n2)
print(new)


def names(*args):
    return args
print(names("Ronnie", "Atuhaire", "John"))

def names_(**kwargs):
    return kwargs
print(names_(first = "Ronnie", last = "Atuhaire"))

# The breakpoint()
x = 10
y = 'Hi'
z = 'Hello'

print(y)
breakpoint()
print(z)

# Zip
string_ = ["one", "two", "three"]
number_ = [1,2,3]

for string, number in zip(string_ , number_):
    print(string, "-->" ,number)


mat = [[1, 2, 3], [1000, 2000, 3000]]
print([n for n in zip(*mat)])

for _, idx in enumerate(range(2,10)):
    print(idx)

first_name = input("Enter your first name [+]: ")
last_name = input("Enter your last name [+]: ")

print(f"So you are {first_name} {last_name} all along!")

first_name_ , last_name_ = input("Enter your full name [+]: ").split()
print(f"So you are {first_name_} {last_name_} all along!")



# PPP
import requests
import json
import pprint

# IP address to test
ip_address = '200.229.2.90'

# Our Endpoint (API) URL
request_url = f"https://geolocation-db.com/jsonp/{ip_address}"

# Send request and decode the result
response = requests.get(request_url)
result = response.content.decode()

# Clean the returned string so it just contains the JSON String
result = result.split("(")[1].strip(")")

# Convert this data into dictionary
result  = json.loads(result)
print(result)

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(result)

from keyword import kwlist

def all_keywords():
    print(kwlist, end="\n\n")
    return f"And they are {len(kwlist)} keywords in Python 3.10.0"

print(all_keywords())
