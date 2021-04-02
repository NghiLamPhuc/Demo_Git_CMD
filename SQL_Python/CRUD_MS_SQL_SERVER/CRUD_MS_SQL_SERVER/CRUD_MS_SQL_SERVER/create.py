import db_connection as dbConn

class Create:
    def func_CreateData(self):

        # Get the sql connection
        connection = dbConn.getConnection()
                
        MACS = input('Nhap ma co so = ')
        TENCS = input('Nhap ten co so = ')
        DIACHI = input('Nhap dia chi = ')
        
        try:
           query = "INSERT INTO CoSo(MACS, TENCS, DIACHI) VALUES(?, ?, ?)" 
           cursor = connection.cursor()
           cursor.execute(query, [MACS, TENCS, DIACHI])

           # Commit the data
           connection.commit()
           print('Data Saved Successfully')

        except:
             print('Something wrong, please check')

        finally:
           # Close the connection
           connection.close()
