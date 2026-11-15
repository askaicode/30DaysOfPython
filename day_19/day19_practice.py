# Day 19 practice: JSON + CSV + first DSA problem
# Run: python day19_practice.py
# Files are saved next to this script, so it works from any folder.

import csv
import json
from pathlib import Path

HERE = Path(__file__).parent


# ---------------------------------------------------------------
# PART 1: JSON (save and load a dict)
# ---------------------------------------------------------------
person = {"name": "Asabeneh", "country": "Finland", "skills": ["Python", "React"]}

json_path = HERE / "person.json"

with open(json_path, "w", encoding="utf-8") as f:
    json.dump(person, f, ensure_ascii=False, indent=4)    # dict -> file

with open(json_path, encoding="utf-8") as f:
    loaded = json.load(f)                                 # file -> dict

print("JSON round trip works:", loaded == person)         # True


# ---------------------------------------------------------------
# PART 2: CSV (a table saved as text, one row per line)
# ---------------------------------------------------------------
students = [
    {"name": "Asabeneh", "age": 30, "city": "Helsinki"},
    {"name": "Lidiya", "age": 25, "city": "Tallinn"},
    {"name": "Ermias", "age": 28, "city": "Oslo"},
]

csv_path = HERE / "students.csv"

# newline="" is needed on Windows, or you get blank lines between rows
with open(csv_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "age", "city"])
    writer.writeheader()          # first line: name,age,city
    writer.writerows(students)    # one line per dictionary

with open(csv_path, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))    # each row comes back as a dict

print("Rows read from CSV:", len(rows))
print("First row:", rows[0])
# Careful: CSV gives everything back as TEXT, so age is '30', not 30
print("Age type:", type(rows[0]["age"]))
total_age = sum(int(row["age"]) for row in rows)
print("Total age:", total_age)                              # 83


# ---------------------------------------------------------------
# PART 3: First DSA problem, "Two Sum"
# ---------------------------------------------------------------
# Given a list of numbers and a target, return the positions of the
# two numbers that add up to the target.
#   two_sum([2, 7, 11, 15], 9)  ->  [0, 1]   because 2 + 7 = 9
#
# Idea: walk through the list once. For each number, ask:
# "Have I already seen the number that completes the target?"
# A dictionary answers that question instantly.

def two_sum(numbers, target):
    seen = {}                          # number -> its position
    for i, n in enumerate(numbers):
        missing = target - n           # the partner we need
        if missing in seen:
            return [seen[missing], i]
        seen[n] = i
    return None                        # no pair found

assert two_sum([2, 7, 11, 15], 9) == [0, 1]
assert two_sum([3, 2, 4], 6) == [1, 2]
assert two_sum([1, 2, 3], 100) is None
print("Two Sum: all tests pass")


# ---------------------------------------------------------------
# YOUR TURN
# ---------------------------------------------------------------
# 1. Add a 4th student to the list and save the CSV again.
# 2. Read students.csv and print only the names of students older than 26.
# 3. Save the list of students as students.json, then load it back.
# 4. Two Sum, brute force: write two_sum_slow using two nested for loops.
#    Compare it with the dictionary version. Which one is shorter? Faster?
