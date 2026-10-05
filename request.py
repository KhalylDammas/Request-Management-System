import pyodbc

# Create a class for storing request data
class Request:
    def __init__(self, request_id, title, description, status):
     self.request_id = request_id
     self.title = title
     self.description = description
     self.status = status


# Function for cruting a new requests
def create_request(cursor , conn):
    reqest_id = input("Enter request_Id")
    title = input("Enter request title : ")
    description = input("Enter request description")
    
    cursor.execute(
        "INSERT INTO Requests(ID,Title , Description , Status) VALUES(?,?,?,?)",
        (request_id,title , description , "NEW")
    )
    conn.commit()
    
    print("Request created successfully")


# Function for displaying requests
def view_requests(cursor):
    cursor.execute("SELECT * FROM Requests")
    rows = cursor.fetchall()
    for row in rows:
        print(row)   
    
    if rows == []:
        print("No requests have been created yet.")
    else:
        for row in rows:
            print("Request ID :" , row[0])
            print("Title :" ,row[1])
            print("Description :" ,row[2])
            print("Status :", row[3])

def main():
    conn_string =(
        "DRIVER = {ODBC Driver for SQL Server};"
        "SERVER = 127.0.0.1;"
        "DATABASE = RequestDB;"
        "UID = SARA;"
        "PWD = sa1234"
        "Encrypt =yes;"
        "TrustServerCertificate=yes"
    )

