from config import collection  # Import the MongoDB collection

# Sample data
data = [
    {"plate_number": "MH12AB1234", "name": "John Doe", "email": "johndoe@example.com"},
    {"plate_number": "MH19 EQ 0001", "name": "Alice Smith", "email": "adnanask19@gmail.com"},
    {"plate_number": "MH19 EQ 0001", "name": "Alice Smith", "email": "adnanask19@gmail.com"},
        {"plate_number": "MH 19 EQ 0001", "name": "Alice Smith", "email": "adnanask19@gmail.com"},


]

# Insert data
collection.insert_many(data)

print("Data inserted successfully!")
