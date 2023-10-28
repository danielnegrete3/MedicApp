import sqlite3

class Controller:
    def __init__(self, database, table, columns) -> None:
        self.database = database
        self.table = table
        self.columns = columns
        self.conexion = sqlite3.connect(database)
        
    
    