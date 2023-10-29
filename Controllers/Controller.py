import sqlite3

class Controller:  
    database = ""
    table = ""
    columns = []
    columns_string = ""
    
    def __init__(self):
        self.conexion = sqlite3.connect(self.database)
        
    def insert(self,data):
        inserts = "NULL,"
        for i in range(len(data)):
            inserts +="'" + data[i] + "'"
            if (len(data)-1 != i):
                inserts += ","  
        self.conexion.execute(
            "INSERT INTO "+
            self.table +
            "("+self.columns_string+")"+
            " VALUES "+
            "("+inserts+");"
        )
        self.conexion.commit() 
        
    def where(self, columns, values):
        search = ""
        for i in range(len(columns)):
            search += " " + columns[i] + " = '" + values[i] + "'"
            if(len(columns)-1 != i):
                search += " AND"              
        return self.conexion.execute(
            "SELECT *"+
            " FROM " +
            self.table +
            " WHERE "+
            search
        )
        
    def where_id(self, id):
        return self.conexion.execute(
            "SELECT *"+
            " FROM " +
            self.table+
            "WHERE id = "+
            id
        )
        
    def all(self):
        return self.conexion.execute(
            "SELECT *"+
            " FROM " +
            self.table
        )
    
    def getid(self, data):
        search = ""
        for i in range(1,len(self.columns)):
            search += " " + self.columns[i] + " = '" + data[i-1] + "'"
            if(len(self.columns)-1 != i):
                search += " AND"
        return self.conexion.execute(
            "SELECT id"+
            " FROM " +
            self.table +
            " WHERE"+
            search
        )
    