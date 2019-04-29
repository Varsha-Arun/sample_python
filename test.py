import unittest
from app import App

class TestSuite(unittest.TestCase):

    def test(self):
        app = App()
        app.calculate()
        self.failIf(app.retrieve() != 62)

    def test2(self):
        app = App()
        app.calculate2()
        self.failIf(app.retrieve2() != 61)
        
    def test3(self):
        app = App()
        app.calculate3()
        self.failIf(app.retrieve3() != 48)

    def test4(self):
        app = App()
        app.calculate4()
        self.failIf(app.retrieve4() != 20) #29
        
    def test5(self):
        app = App()
        app.calculate5()
        self.failIf(app.retrieve5() != 70)

    def test6(self):
        app = App()
        app.calculate6()
        self.failIf(app.retrieve6() != 120)
        
    def test7(self):
        app = App()
        app.calculate7()
        self.failIf(app.retrieve7() != 88)

    def test8(self):
        app = App()
        app.calculate8()
        self.failIf(app.retrieve8() != 49)
        
    def test9(self):
        app = App()
        app.calculate9()
        self.failIf(app.retrieve9() != 222)

    def test10(self):
        app = App()
        app.calculate10()
        self.failIf(app.retrieve10() != 180) #181
        
    def test11(self):
        app = App()
        app.calculate11()
        self.failIf(app.retrieve11() != 128)

    def test12(self):
        app = App()
        app.calculate12()
        self.failIf(app.retrieve12() != 69)
      
    def test13(self):
        app = App()
        app.calculate13()
        self.failIf(app.retrieve13() != 302)

    def test14(self):
        app = App()
        app.calculate14()
        self.failIf(app.retrieve14() != 241)
        
    def test15(self):
        app = App()
        app.calculate15()
        self.failIf(app.retrieve15() != 16) #168 ll pass
        
def main():
    unittest.main()

if __name__ == "__main__":
    main()
