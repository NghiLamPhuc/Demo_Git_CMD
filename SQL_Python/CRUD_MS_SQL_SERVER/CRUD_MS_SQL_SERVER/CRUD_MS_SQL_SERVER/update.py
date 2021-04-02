
import db_connection as dbConn;

class Update:
   def func_UpdateData(self):
      # Ge the sql connection
      connection = dbConn.getConnection()

      MACS = input('Ma co so = ')
   
      try:
         # Fethc the data which needs to be updated
         sql = "Select * From CoSo Where MACS = ?" 
         cursor = connection.cursor()
         cursor.execute(sql, [MACS])
         item = cursor.fetchone()
         print('Data Fetched for Id = ', MACS)
         print('MACS\t\t TENCS\t\t\t DIACHI')
         print('-------------------------------------------')       
         print(' {}\t\t {} \t\t\t{} '.format(item[0], item[1], item[2]))
         print('-------------------------------------------')
         print('Enter New Data To Update Co so Record ')

         TENCS = input('Nhap ten co so = ')
         DIACHI = input('Nhap dia chi = ')
         query = "Update CoSo Set TENCS = ?, DIACHI =? Where MACS =?" 
      
         # Execute the update query
         cursor.execute(query, [TENCS, DIACHI])
         connection.commit()
         print('Data Updated Successfully')

      except:
            print('Somethng worng, please check')

      finally:
         # Close the connection
         connection.close()
