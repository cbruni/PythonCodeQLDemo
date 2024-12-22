# vulnerable.py

def connect_to_database():
    # Vulnerable: Hardcoded database credentials (BAD PRACTICE)
    db_user = 'admin'
    db_password = 'password123'
    db_host = 'localhost'
    db_name = 'test_db'

    print(f"Connecting to database {db_name} at {db_host} as {db_user}...")

    if db_user == 'admin' and db_password == 'password123':
        print("Successfully connected to the database!")
    else:
        print("Failed to connect to the database.")
        raise ValueError("Database connection failed due to incorrect credentials.")

# Call the function (this will trigger the connection attempt)
connect_to_database()
