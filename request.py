import pyodbc

# Create a class for storing request data
class Request:
    def __init__(self, request_id, title, description, status):
     self.request_id = request_id
     self.title = title
     self.description = description
     self.status = status


# Function to  create a new request
def create_request(cursor , conn):
    title = input("Enter request title : ")
    description = input("Enter request description")

#Start request ID from 1
    request_id = 1
    cursor.execute("SELECT ID FROM Requests")
    rows = cursor.fetchall()

    #find the next request id
    for row in rows: 
         request_id +=1

    #Add the request to the database
    cursor.execute(
        "INSERT INTO Requests(ID,Title , Description , Status) VALUES(?,?,?,?)",
        (request_id,title , description , "NEW")
    )
    conn.commit()#sava the changes
    
    print("Request created successfully")


# Function to view requests
def view_requests(cursor):
    #get requests from the database
    cursor.execute("SELECT * FROM Requests")
    rows = cursor.fetchall()
    if rows == []:
        print("No requests have been created yet.")
    else:
        for row in rows:
            print("Request ID :" , row[0])
            print("Title :" ,row[1])
            print("Description :" ,row[2])
            print("Status :", row[3])

def main(): 
    conn_string =(#database connection
        "DRIVER={ODBC Driver 18 for SQL Server};"
        "SERVER=127.0.0.1;"
        "DATABASE=RequestDB;"
        "UID=SARA;"
        "PWD=sa1234;"
        "Encrypt=yes;"
        "TrustServerCertificate=yes"
    )
    try:    #connect to the database
        with pyodbc.connect(conn_string) as conn:
            with conn.cursor() as cursor:
                #Show the menu
                choice = "1"

                while choice != "3":
                    print("Request Management System")
                    print()
                    print("1. Create Request")
                    print("2. View Requests")
                    print("3. Exit")

                    choice = input("Choose an option: ")

                    if choice == "1":
                     create_request(cursor, conn)
                    elif choice == "2":
                     view_requests(cursor)
                    elif choice == "3":
                     print("Goodbye.")
                    else:
                     print("Invalid choice.")
    #Handle database errors
    except pyodbc.Error as error:
     print("Database error:", error)

if __name__ == "__main__":
   main()

