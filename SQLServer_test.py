import unittest
from sqlalchemy import text


from  SQLServer import sqlserver

class SQLServer(unittest.TestCase):
    def test_DeclareSQLServerInWithStyle(self):
        with sqlserver.SQLServer.Login("DESKTOP-F1E0DKV\SQL2019","master") as engine:
            self.assertEqual(engine.driver, "pyodbc")
            self.assertEqual(engine.name, "mssql")
            with engine.connect() as connection:
                result = connection.execute(text("select LEFT(@@version, 20)"))
                self.assertEqual(result.first()[0], "Microsoft SQL Server")

        with sqlserver.SQLServer.Login("DESKTOP-F1E0DKV\SQL2019","master", "PublicUser", "PublicUser") as engine:
            self.assertEqual(engine.driver, "pyodbc")
            self.assertEqual(engine.name, "mssql")
            with engine.connect() as connection:
                result = connection.execute(text("select LEFT(@@version, 20)"))
                self.assertEqual(result.first()[0], "Microsoft SQL Server")
       


if __name__ == '__main__':
    unittest.main()