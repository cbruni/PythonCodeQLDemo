import sqlite3

def search_user(username):
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    query = f"SELECT * FROM users WHERE username = '{username}'"

    cursor.execute(query)

    user = cursor.fetchone()
    if user:
        print(f"User found: {user}")
    else:
        print("User not found.")

    conn.close()

search_user("admin' OR '1'='1")  # SQL Injection attempt
