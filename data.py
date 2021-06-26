import sqlite3


db_path = 'pa.db'

# Connect to DB and return Conn and Cur Objects

def connect_db(db_path):
    conn = sqlite3.connect(db_path)
    # Convert Tuples to Dictionaries
    conn.row_factory = sqlite3.Row
    return (conn, conn.cursor())

# Read all pet by pet type
def read_pets(pet_type):
    conn, cur = connect_db(db_path)
    query = 'SELECT * FROM pets WHERE type=?'
    results = cur.execute(query, (pet_type,)).fetchall()
    conn.close()
    return results


# Read a pet given its pet id

def read_pet(pet_id):
    conn, cur = connect_db(db_path)
    query = 'SELECT * FROM pets WHERE id=?'
    results = cur.execute(query, (pet_id,)).fetchone()
    conn.close()
    return results

# Insert a Pet to DB
def insert_pet(pet_data):
    conn, cur = connect_db(db_path)
    query = 'INSERT INTO pets (name, age, breed, description, url, type) VALUES (?,?,?,?,?,?)'
    values = (pet_data['name'],
             pet_data['age'],
             pet_data['breed'],
             pet_data['description'],
             pet_data['url'],
             pet_data['type'])

    cur.execute(query, values)
    conn.commit()
    conn.close()

def delete_pet(pet_id):
    conn, cur = connect_db(db_path)
    query = 'DELETE FROM pets WHERE id=?'
    cur.execute(query, (pet_id,))
    conn.commit()
    conn.close()

# Update a Pet to DB
def update_pet(pet_data):
    conn, cur = connect_db(db_path)
    query = 'UPDATE pets SET name=? , age=? , breed=? , description=? , url=? , type=? WHERE id=?'
    values = (pet_data['name'],
             pet_data['age'],
             pet_data['breed'],
             pet_data['description'],
             pet_data['url'],
             pet_data['type'],
             pet_data['id'])

    cur.execute(query, values)
    conn.commit()
    conn.close()