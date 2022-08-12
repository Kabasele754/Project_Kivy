import sqlite3

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        blobData = file.read()
    return blobData

def insertBLOB(nom, image):
    try:
        sqliteConnection = sqlite3.connect('formulaire_etudiant.db')
        cursor = sqliteConnection.cursor()
        print("Connected to SQLite")
        sqlite_insert_blob_query = """ INSERT INTO etudiant
                                  (nom, image) VALUES (?, ?,)"""

        empImage = convertToBinaryData(image)
        # Convert data into tuple format
        data_tuple = (nom, empImage)
        cursor.execute(sqlite_insert_blob_query, data_tuple)
        sqliteConnection.commit()
        print("Image and file inserted successfully as a BLOB into a table")
        cursor.close()

    except sqlite3.Error as error:
        print("Failed to insert blob data into sqlite table", error)
    finally:
        if sqliteConnection:
            sqliteConnection.close()
            print("the sqlite connection is closed")

insertBLOB("Achille", "images/enfant1.jpg")
insertBLOB("Charles", "images/enfant2.jpg")
