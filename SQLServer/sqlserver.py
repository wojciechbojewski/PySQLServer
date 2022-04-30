from sqlalchemy import create_engine

class SQLServer:
    def __init__(self, connectionString):
        self._engine = create_engine(connectionString)

    def Login(server, database, user = None, password = None):
        if user==None or password==None:
            connectionString = f'mssql+pyodbc://{server}/{database}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'
        else:
            connectionString = f'mssql+pyodbc://{user}:{password}@{server}/{database}?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server'
        return SQLServer(connectionString)

    def __enter__(self):          
        return self._engine      

    def __exit__(self ,type, value, traceback):
        pass