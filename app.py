from database import get_connection

try:
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SHOW TABLES")

    tables = cursor.fetchall()

    print("Database Tables:")
    for table in tables:
        print(table[0])

    cursor.close()
    conn.close()

except Exception as e:
    print("Error:", e)


    from database import get_connection

question = input("Ask your question: ")

print("You asked:", question)