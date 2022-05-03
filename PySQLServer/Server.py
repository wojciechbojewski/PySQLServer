from sqlalchemy import create_engine
from sqlalchemy import text

class SQLServer:
    def __init__(self, server):
        self._server = server
        connectionString = f'mssql+pyodbc://{server}/master?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'
        self._engine = create_engine(connectionString)

    def Credentials(self, user, password):
        connectionString = f'mssql+pyodbc://{user}:{password}@{self._server}/master?driver=ODBC+Driver+17+for+SQL+Server'
        self._engine = create_engine(connectionString)
        return self

    def Connect(self):
        self._connection = self._engine.connect()
        return self._connection

    def ShowDatabases(self, availeble=0):
        output = []
        sql = text("SELECT name FROM sys.databases")
        if availeble == 1:
            sql = text("SELECT name FROM sys.databases WHERE HAS_DBACCESS(name) = 1")
        output =  [ row[0] for row in self._connection.execute(sql).fetchall() ] 
        return output

    def __enter__(self):          
        return self      

    def __exit__(self ,type, value, traceback):
        pass