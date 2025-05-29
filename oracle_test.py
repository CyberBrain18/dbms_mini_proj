import cx_Oracle

# Replace these with your actual credentials
username = "SYSTEM"
password = "tiger"
dsn = cx_Oracle.makedsn("localhost", 1521, service_name="freepdb1")

try:
    print("Connecting to Oracle database...")
    connection = cx_Oracle.connect(user=username, password=password, dsn=dsn)
    print("✅ Connection successful!")
    
    # Optional: Run a test query
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM dual")
    for row in cursor:
        print("Query result:", row)

    # Clean up
    cursor.close()
    connection.close()
    print("Connection closed.")

except cx_Oracle.DatabaseError as e:
    error, = e.args
    print("❌ Database connection failed:")
    print(f"Error code: {error.code}")
    print(f"Message: {error.message}")
