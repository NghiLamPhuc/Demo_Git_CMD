import pyodbc
import config

# Return the sql connection 
def getConnection():
     connection = pyodbc.connect("Driver={"+config.DATABASE_CONFIG["Driver"]+"};Server=" + config.DATABASE_CONFIG["Server"] + ";Database=" + config.DATABASE_CONFIG["Database"] + ";uid=" + config.DATABASE_CONFIG["UID"] + ";pwd=" + config.DATABASE_CONFIG["Password"])
     return connection

