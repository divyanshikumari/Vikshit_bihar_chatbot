import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="divyanshi@11",
        database="bihar_chatbot"
    )
    return conn