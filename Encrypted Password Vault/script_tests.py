import unittest
import script

class TestStringMethods(unittest.TestCase):

    def test_basics(self):
        password = "129vhxve4gef8$3B*B&"
        path = "/Users/alexluu/Documents/GitHub/Encrypted Password Vault/Encrypted Password Vault"
        script.initialize(path)
        script.create_csv(path, password)

        # Part 1 - Basics
        script.write(path, password, ["Xnew!1", "xx@fr.com", "!@#aA1$"])
        self.assertEqual(script.read(path, password), "\r\nXnew!1,xx@fr.com,!@#aA1$")
        script.write(path, password, ["crvr", "Axx@fr.", "!swceaA1$"])
        self.assertEqual(script.read(path, password), "\r\nXnew!1,xx@fr.com,!@#aA1$\r\ncrvr,Axx@fr.,!swceaA1$")
        script.write(path, password, ["!rvr", "Axx@fr.", "!swceaA1$"])
        script.write(path, password, ["Ynew!1", "xx@fr.com", "!@#aA1$"])
        self.assertEqual(script.read(path, password), "\r\nXnew!1,xx@fr.com,!@#aA1$\r\ncrvr,Axx@fr.,!swceaA1$\r\n!rvr,Axx@fr.,!swceaA1$\r\nYnew!1,xx@fr.com,!@#aA1$")

        script.delete(path, password, "!rvr")
        self.assertEqual(script.read(path, password), "\r\nXnew!1,xx@fr.com,!@#aA1$\r\ncrvr,Axx@fr.,!swceaA1$\r\nYnew!1,xx@fr.com,!@#aA1$")
        script.delete(path, password, "Xnew!1")
        self.assertEqual(script.read(path, password), "\r\ncrvr,Axx@fr.,!swceaA1$\r\nYnew!1,xx@fr.com,!@#aA1$")
        script.delete(path, password, "Ynew!1")
        self.assertEqual(script.read(path, password), "\r\ncrvr,Axx@fr.,!swceaA1$")
        script.delete(path, password, "crvr")
        self.assertEqual(script.read(path, password), "")

        # Part 2: changePassword
        script.write(path, password, ["Xnew!1", "xx@fr.com", "!@#aA1$"])
        self.assertEqual(script.read(path, password), "\r\nXnew!1,xx@fr.com,!@#aA1$")
        script.write(path, password, ["crvr", "Axx@fr.", "!swceaA1$"])
        self.assertEqual(script.read(path, password), "\r\nXnew!1,xx@fr.com,!@#aA1$\r\ncrvr,Axx@fr.,!swceaA1$")
        script.write(path, password, ["!rvr", "Axx@fr.", "!swceaA1$"])
        script.write(path, password, ["Ynew!1", "xx@fr.com", "!@#aA1$"])
        self.assertEqual(script.read(path, password), "\r\nXnew!1,xx@fr.com,!@#aA1$\r\ncrvr,Axx@fr.,!swceaA1$\r\n!rvr,Axx@fr.,!swceaA1$\r\nYnew!1,xx@fr.com,!@#aA1$")

        newPassword = "c!&*HEhf38cnu3"
        script.changePassword(path, password, newPassword)
        self.assertEqual(script.read(path, newPassword), "\r\nXnew!1,xx@fr.com,!@#aA1$\r\ncrvr,Axx@fr.,!swceaA1$\r\n!rvr,Axx@fr.,!swceaA1$\r\nYnew!1,xx@fr.com,!@#aA1$")
        script.delete(path, newPassword, "!rvr")
        self.assertEqual(script.read(path, newPassword), "\r\nXnew!1,xx@fr.com,!@#aA1$\r\ncrvr,Axx@fr.,!swceaA1$\r\nYnew!1,xx@fr.com,!@#aA1$")


        #os.remove('/Users/alexluu/Documents/GitHub/Encrypted Password Vault/Encrypted Password Vault/EncryptedPasswordVault_UserData')

    def test_edgeCases(self):
        password = "129vhxve4gef8$3B*B&"
        path = "/Users/alexluu/Documents/GitHub/Encrypted Password Vault/Encrypted Password Vault"
        script.initialize(path)
        script.create_csv(path, password)

        # Part 1 - Basics
        script.write(path, password, ["Xnew!1", "xx@fr.com", "!@#aA1$"])
        script.write(path, password, ["crvr", "Axx@fr.", "!swceaA1$"])
        script.write(path, password, ["!rvr", "Axx@fr.", "!swceaA1$"])
        script.write(path, password, ["Ynew!1", "xx@fr.com", "!@#aA1$"])
        self.assertEqual(script.read(path, password), "\r\nXnew!1,xx@fr.com,!@#aA1$\r\ncrvr,Axx@fr.,!swceaA1$\r\n!rvr,Axx@fr.,!swceaA1$\r\nYnew!1,xx@fr.com,!@#aA1$")

        script.delete(path, password, "!rvr")
        self.assertEqual(script.read(path, password), "\r\nXnew!1,xx@fr.com,!@#aA1$\r\ncrvr,Axx@fr.,!swceaA1$\r\nYnew!1,xx@fr.com,!@#aA1$")
        script.delete(path, password, "!rvr")
        self.assertEqual(script.read(path, password), "\r\nXnew!1,xx@fr.com,!@#aA1$\r\ncrvr,Axx@fr.,!swceaA1$\r\nYnew!1,xx@fr.com,!@#aA1$")

        script.delete(path, password, "Xnew!1")
        self.assertEqual(script.read(path, password), "\r\ncrvr,Axx@fr.,!swceaA1$\r\nYnew!1,xx@fr.com,!@#aA1$")
        script.delete(path, password, "Xnew!1")
        self.assertEqual(script.read(path, password), "\r\ncrvr,Axx@fr.,!swceaA1$\r\nYnew!1,xx@fr.com,!@#aA1$")

        script.delete(path, password, "Ynew!1")
        self.assertEqual(script.read(path, password), "\r\ncrvr,Axx@fr.,!swceaA1$")
        script.delete(path, password, "Ynew!1")
        self.assertEqual(script.read(path, password), "\r\ncrvr,Axx@fr.,!swceaA1$")

        script.delete(path, password, "crvr")
        self.assertEqual(script.read(path, password), "")
        script.delete(path, password, "crvr")
        self.assertEqual(script.read(path, password), "")

        # Part 2: changePassword
        script.write(path, password, ["Xnew!1", "xx@fr.com", "!@#aA1$"])
        self.assertEqual(script.read(path, password), "\r\nXnew!1,xx@fr.com,!@#aA1$")
        script.write(path, password, ["crvr", "Axx@fr.", "!swceaA1$"])
        self.assertEqual(script.read(path, password), "\r\nXnew!1,xx@fr.com,!@#aA1$\r\ncrvr,Axx@fr.,!swceaA1$")
        script.write(path, password, ["!rvr", "Axx@fr.", "!swceaA1$"])
        script.write(path, password, ["Ynew!1", "xx@fr.com", "!@#aA1$"])
        self.assertEqual(script.read(path, password), "\r\nXnew!1,xx@fr.com,!@#aA1$\r\ncrvr,Axx@fr.,!swceaA1$\r\n!rvr,Axx@fr.,!swceaA1$\r\nYnew!1,xx@fr.com,!@#aA1$")

        newPassword = "c!&*HEhf38cnu3"
        script.changePassword(path, password, newPassword)
        self.assertEqual(script.read(path, newPassword), "\r\nXnew!1,xx@fr.com,!@#aA1$\r\ncrvr,Axx@fr.,!swceaA1$\r\n!rvr,Axx@fr.,!swceaA1$\r\nYnew!1,xx@fr.com,!@#aA1$")
        script.delete(path, newPassword, "!rvr")
        self.assertEqual(script.read(path, newPassword), "\r\nXnew!1,xx@fr.com,!@#aA1$\r\ncrvr,Axx@fr.,!swceaA1$\r\nYnew!1,xx@fr.com,!@#aA1$")


        #os.remove('/Users/alexluu/Documents/GitHub/Encrypted Password Vault/Encrypted Password Vault/EncryptedPasswordVault_UserData')


if __name__ == '__main__':
    unittest.main()