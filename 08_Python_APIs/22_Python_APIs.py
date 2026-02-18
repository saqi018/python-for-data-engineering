"""
========================================
PYTHON APIs — FULL BEGINNER GUIDE FILE
Level: Beginner → Data Engineer Basics
========================================

What is an API?
- API = bridge between your code and a server
- You request data → server sends JSON

Real world:
- Weather app gets data from weather API
- Payment app sends data to payment API
- Data Engineers fetch data from APIs daily

We use:
requests → call API
json → handle JSON data
csv → save structured data

All output files saved inside:
08/Python/APIs
"""

import requests
import json
import csv
import os

BASE_PATH = "08_Python_APIs"
os.makedirs(BASE_PATH, exist_ok=True)

# =====================================================
# TOPIC 1 — API GET (FETCH DATA)
# =====================================================

"""
GET = fetch data from API
Most used method
Returns JSON data
"""

url = "https://jsonplaceholder.typicode.com/users/1"

res = requests.get(url)

if res.status_code == 200:
    data = res.json()
    print("User name:", data["name"])

    with open(f"{BASE_PATH}/get_user.json", "w") as f:
        json.dump(data, f, indent=2)

# -------------------------------
# SOLVED QUIZ — GET (3)
# -------------------------------

# Q1 — Fetch todos and print title
r = requests.get("https://jsonplaceholder.typicode.com/todos/1")
print("Todo:", r.json()["title"])

# Q2 — Fetch posts and print count
r = requests.get("https://jsonplaceholder.typicode.com/posts")
print("Total posts:", len(r.json()))

# Q3 — Fetch users and save to JSON
r = requests.get("https://jsonplaceholder.typicode.com/users")
with open(f"{BASE_PATH}/users.json", "w") as f:
    json.dump(r.json(), f, indent=2)

# -------------------------------
# UNSOLVED QUIZ — GET (3)
# -------------------------------

"""
1) Fetch comments API and print first email
2) Fetch albums and print total count
3) Fetch users and print all usernames
"""

# =====================================================
# TOPIC 2 — LOOP API RECORDS
# =====================================================

"""
Most APIs return list of records
We loop through them
"""

r = requests.get("https://jsonplaceholder.typicode.com/posts")
posts = r.json()

for p in posts[:5]:
    print("Title:", p["title"])

# -------------------------------
# SOLVED QUIZ — LOOP (3)
# -------------------------------

# Q1 — print first 3 ids
for p in posts[:3]:
    print(p["id"])

# Q2 — save titles to text file
with open(f"{BASE_PATH}/titles.txt", "w") as f:
    for p in posts:
        f.write(p["title"] + "\n")

# Q3 — save posts to CSV
with open(f"{BASE_PATH}/posts.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["id", "title"])
    for p in posts:
        writer.writerow([p["id"], p["title"]])

# -------------------------------
# UNSOLVED QUIZ — LOOP (3)
# -------------------------------

"""
1) Print only titles longer than 30 chars
2) Count posts for userId = 1
3) Save body field to file
"""

# =====================================================
# TOPIC 3 — POST (SEND DATA)
# =====================================================

"""
POST = send data to server
Used for create operations
"""

payload = {
    "title": "hello",
    "body": "data engineer",
    "userId": 1
}

res = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=payload
)

print("POST status:", res.status_code)

if res.status_code == 201:
    with open(f"{BASE_PATH}/post_response.json", "w") as f:
        json.dump(res.json(), f, indent=2)

# -------------------------------
# SOLVED QUIZ — POST (3)
# -------------------------------

# Q1 — send simple user data
requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={"name": "ali"}
)

# Q2 — check success message
r = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={"x": 1}
)
print("Success" if r.status_code == 201 else "Fail")

# Q3 — save POST response
r = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json={"role": "DE"}
)
with open(f"{BASE_PATH}/post_save.json", "w") as f:
    json.dump(r.json(), f, indent=2)

# -------------------------------
# UNSOLVED QUIZ — POST (3)
# -------------------------------

"""
1) Send product data
2) Print returned id
3) Save response to CSV
"""

# =====================================================
# TOPIC 4 — PARAMS (FILTER DATA)
# =====================================================

"""
params = filter results
Like SQL WHERE
"""

params = {"userId": 1}

r = requests.get(
    "https://jsonplaceholder.typicode.com/posts",
    params=params
)

data = r.json()
print("Filtered count:", len(data))

# -------------------------------
# SOLVED QUIZ — PARAMS (3)
# -------------------------------

# Q1 — print titles
for d in data:
    print(d["title"])

# Q2 — save filtered JSON
with open(f"{BASE_PATH}/params.json", "w") as f:
    json.dump(data, f, indent=2)

# Q3 — save filtered CSV
with open(f"{BASE_PATH}/params.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id", "title"])
    for d in data:
        w.writerow([d["id"], d["title"]])

# -------------------------------
# UNSOLVED QUIZ — PARAMS (3)
# -------------------------------

"""
1) Fetch posts userId=2
2) Print only ids
3) Save bodies to file
"""

# =====================================================
# TOPIC 5 — TIMEOUT
# =====================================================

"""
timeout = safety
Stop waiting if server slow
"""

try:
    r = requests.get(
        "https://jsonplaceholder.typicode.com/posts",
        timeout=5
    )
    print("Timeout safe:", len(r.json()))

except requests.exceptions.RequestException:
    print("Timeout error")

# -------------------------------
# SOLVED QUIZ — TIMEOUT (3)
# -------------------------------

requests.get(url, timeout=3)
requests.get(url, timeout=10)
requests.get(url, timeout=1)

# -------------------------------
# UNSOLVED QUIZ — TIMEOUT (3)
# -------------------------------

"""
1) Try timeout=0.5
2) Wrap in try/except
3) Print custom fail message
"""

# =====================================================
# TOPIC 6 — ERROR HANDLING
# =====================================================

"""
Always protect API calls
"""

try:
    bad = requests.get("https://bad-url-example", timeout=3)
    bad.raise_for_status()
except requests.exceptions.RequestException:
    print("API failed safely")

# -------------------------------
# SOLVED QUIZ — ERROR (3)
# -------------------------------

try:
    requests.get("https://x", timeout=1)
except:
    print("Handled")

try:
    r = requests.get(url)
    if r.status_code != 200:
        print("Bad response")
except:
    pass

try:
    requests.get(url).raise_for_status()
except:
    print("Status error")

# -------------------------------
# UNSOLVED QUIZ — ERROR (3)
# -------------------------------

"""
1) Catch timeout only
2) Catch connection error
3) Print error type
"""

# =====================================================
# MINI API PIPELINE EXAMPLE
# =====================================================

"""
Fetch → loop → save CSV
"""

r = requests.get("https://jsonplaceholder.typicode.com/users")
users = r.json()

with open(f"{BASE_PATH}/pipeline_users.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["name", "email"])
    for u in users:
        w.writerow([u["name"], u["email"]])

print("Pipeline finished")

# =====================================================
# INTERVIEW QUESTIONS — APIs
# =====================================================

"""
1) What is an API?
2) Difference GET vs POST?
3) What is status_code?
4) What is JSON?
5) What is params?
6) Why timeout?
7) Why error handling?
8) How to save API data to CSV?
9) What is raise_for_status()?
10) Explain API pipeline flow
"""

print("=== API LEARNING FILE COMPLETE ===")
