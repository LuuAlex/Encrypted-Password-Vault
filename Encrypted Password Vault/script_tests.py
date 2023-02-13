import unittest
import script
import random

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
    
    def test_random(self):
        password = "129vhxve4gef8$3B*B&"
        path = "/Users/alexluu/Documents/GitHub/Encrypted Password Vault/Encrypted Password Vault"
        script.initialize(path)
        script.create_csv(path, password)

        ans = ""
        randomChar = "1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*"
        for _ in range(200):
            string1 = ""
            string2 = ""
            string3 = ""
            num = random.randrange(1, 25)
            for i in range(num):
                string1 += randomChar[random.randrange(len(randomChar))]
            num = random.randrange(1, 25)
            for i in range(num):
                string2 += randomChar[random.randrange(len(randomChar))]
            num = random.randrange(1, 25)
            for i in range(num):
                string3 += randomChar[random.randrange(len(randomChar))]
            
            script.write(path, password, [string1, string2, string3])
            ans += f"\r\n{string1},{string2},{string3}"
            self.assertEqual(script.read(path, password), ans)





if __name__ == '__main__':
    unittest.main()