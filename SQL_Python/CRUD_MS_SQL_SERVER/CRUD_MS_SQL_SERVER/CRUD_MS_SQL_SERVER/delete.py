
import db_connection as dbConn;

class Delete:
    def func_DeleteData(self):
        # Get the sql connection
        connection = dbConn.getConnection()

        MACS = input('Nhap ma co so = ')
    
        try:
           # Get record which needs to be deleted
           sql = "Select * From CoSo Where MACS = ?" 
           cursor = connection.cursor()
           cursor.execute(sql, [MACS])
           item = cursor.fetchone()
           print('Data Fetched for Id = ', id)
           print('MACS\t\t TENCS\t\t\t DIACHI')
           print('-------------------------------------------')       
           print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2]))
           print('-------------------------------------------')
           confirm = input('Are you sure to delete this record (Y/N)?')

           # Delete after confirmation
           if confirm == 'Y':
               deleteQuery = "Delete From CoSo Where MACS = ?"
               cursor.execute(deleteQuery,[MACS])
               connection.commit()
               print('Data deleted successfully!')
           else:
                print('Wrong Entry')
        except:
            print('Somethng worng, please check')
        finally:
            connection.close()
