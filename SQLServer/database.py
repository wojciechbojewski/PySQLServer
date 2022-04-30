from sqlalchemy import text

class Database:
    def __init__(self, connection):
        self._connection = connection

    def ShowDatabases(self):
        result = self._connection.execute(text("select name from sys.databases"))
        output = []
        for d in result:
            output.append(d[0])
        return output

    def __enter__(self):          
        return self      

    def __exit__(self ,type, value, traceback):
        pass