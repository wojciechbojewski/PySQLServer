from sqlalchemy import create_engine

class SQLServer:
    def __init__(self, server, database):
        self._server = server
        self._database = database
        self._engine = create_engine('mssql+pyodbc://' + self._server + '/' + self._database + '?trusted_connection=yes&driver=ODBC+Driver+17+for+SQL+Server')

    def __enter__(self):          
        return self._engine      

    def __exit__(self ,type, value, traceback):
        pass