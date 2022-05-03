from  PySQLServer.Server import SQLServer

import unittest
class test_SQLServer(unittest.TestCase):

    def test_TrustedConnection(self):
        with SQLServer("DESKTOP-F1E0DKV\SQL2019") as sql:
            with sql.Connect() as conn:
                result = conn.execute("select suser_sname()")
                self.assertEqual(result.first()[0], "DESKTOP-F1E0DKV\wojci")

    def test_LoginUsingCredencial(self):
        with SQLServer("DESKTOP-F1E0DKV\SQL2019").Credentials("PublicUser","PublicUser") as sql:
            with sql.Connect() as conn:
                result = conn.execute("select suser_sname()")
                self.assertEqual(result.first()[0], "PublicUser")

    def test_ShowDatabases(self):
        with SQLServer("DESKTOP-F1E0DKV\SQL2019").Credentials("PublicUser","PublicUser") as sql:
            with sql.Connect() as conn:
                result = sql.ShowDatabases()
                self.assertListEqual(result, ['master','tempdb','model','msdb','SSISDB','ContosoRetailDW','Temp'])

    def test_ShowDatabasesAvaileble(self):
        with SQLServer("DESKTOP-F1E0DKV\SQL2019").Credentials("PublicUser","PublicUser") as sql:
            with sql.Connect() as conn:
                result = sql.ShowDatabases(1)
                self.assertListEqual(result, ['master','tempdb','msdb'])


if __name__ == '__main__':
    unittest.main()