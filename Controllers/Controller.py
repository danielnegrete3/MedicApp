import sqlite3

class Controller:
    def __init__(self, database, table, columns) -> None:
        self.database = database
        self.table = table
        self.columns = columns
        self.conexion = sqlite3.connect(database)
        self.columns_string = ""
        for column in self.columns:
            self.columns_string += column
            if (self.columns[-1] != column):
                self.columns_string += ","
        
    def insert(self,data):
        inserts = "NULL,"
        for insert in data:
            inserts += insert
            if (data[-1] != insert):
                inserts += ","
        self.conexion.execute(
            "INSERT INTO"+
            self.table +
            "("+self.columns_string+")"+
            "VALUES "+
            "("+inserts+")")
        
    def where(self, column, value):
        return self.conexion.execute(
            "SELECT * "+
            " FROM " +
            self.table+
            "WHERE "+
            column +
            " = '"+
            value +"'"
        )
        
    def where_id(self, id):
        return self.conexion.execute(
            "SELECT * "+
            " FROM " +
            self.table+
            "WHERE id = "+
            id
        )
        
    
    