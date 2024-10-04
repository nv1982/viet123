import mysql.connector

# Kết nối tới MySQL
def connect_db():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",        # Thay bằng username MySQL của bạn
        password="123456",  # Thay bằng password MySQL của bạn
        database="employees"  # Thay bằng tên database của bạn
    )
    return conn
