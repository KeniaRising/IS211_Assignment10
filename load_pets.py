import sqlite3

conn = sqlite3.connect("pets.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS person (
    id INTEGER PRIMARY KEY,
    first_name TEXT,
    last_name TEXT,
    age INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS pet (
    id INTEGER PRIMARY KEY,
    name TEXT,
    breed TEXT,
    age INTEGER,
    dead INTEGER
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS person_pet (
    person_id INTEGER,
    pet_id INTEGER
)
""")
# Add people
cursor.executemany("""
INSERT OR REPLACE INTO person
(id, first_name, last_name, age)
VALUES (?, ?, ?, ?)
""", [
    (1, "James", "Smith", 41),
    (2, "Diana", "Greene", 23),
    (3, "Sara", "White", 27),
    (4, "William", "Gibson", 23)
])

# Add pets
cursor.executemany("""
INSERT OR REPLACE INTO pet
(id, name, breed, age, dead)
VALUES (?, ?, ?, ?, ?)
""", [
    (1, "Rusty", "Dalmation", 4, 1),
    (2, "Bella", "Alaskan Malamute", 3, 0),
    (3, "Max", "Cocker Spaniel", 1, 0),
    (4, "Rocky", "Beagle", 7, 0),
    (5, "Rufus", "Cocker Spaniel", 1, 0),
    (6, "Spot", "Bloodhound", 2, 1)
])

# Connect people to their pets
cursor.execute("DELETE FROM person_pet")

cursor.executemany("""
INSERT INTO person_pet (person_id, pet_id)
VALUES (?, ?)
""", [
    (1, 1),
    (1, 2),
    (2, 3),
    (2, 4),
    (3, 5),
    (4, 6)
])
conn.commit()
conn.close()

print("Pets database tables created successfully!")