import pymysql

try:
    # Connect to MySQL with the correct password
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Raditya@2004',  # Ensure this is the correct password
        db='manually_fill_attendance'
    )
    cursor = connection.cursor()
except pymysql.MySQLError as e:
    print(f"Error: {e}")
    connection.close()
