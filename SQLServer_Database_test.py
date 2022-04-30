import unittest
from sqlalchemy import text


from  SQLServer import sqlserver
from  SQLServer import database

class SQLServerDatabase(unittest.TestCase):
    def test_ShowDatabases(self):
        with sqlserver.SQLServer("DESKTOP-F1E0DKV\SQL2019","master") as engine:
            with engine.connect() as connection:
                with database.Database(connection) as d:
                    result = d.ShowDatabases()
                    self.assertListEqual(result, ['master', 'tempdb', 'model', 'msdb', 'SSISDB', 'ContosoRetailDW', 'Temp'] )


if __name__ == '__main__':
    unittest.main()