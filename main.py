import sqlite3

# Function to search for a user in the database
def search_user(username):
    # Create a database connection
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # Vulnerable query
    query = f"SELECT * FROM users WHERE username = '{username}'"

    # Execute the query
    cursor.execute(query)

    # Fetch and print the result
    user = cursor.fetchone()
    if user:
        print(f"User found: {user}")
    else:
        print("User not found.")

    # Close the connection
    conn.close()

# Simulate a user search with unsafe input
search_user("admin' OR '1'='1")  # SQL Injection attempt
