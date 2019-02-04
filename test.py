import unittest
from app import App

class TestSuite(unittest.TestCase):

    def test1(self):
        app = App()
        app.calculate()
        self.failIf(app.retrieve() != 62)
    
    def test2(self):
        app = App()
        app.calculate2()
        self.failIf(app.retrieve2() != 62)

    def test3(self):
        app = App()
        app.calculate3()
        self.failIf(app.retrieve3() != 72)
    
    def test4(self):
        app = App()
        app.calculate4()
        self.failIf(app.retrieve4() != 68)
    
    def test5(self):
        app = App()
        app.calculate5()
        self.failIf(app.retrieve5() != 73)
    
    def test6(self):
        app = App()
        app.calculate6()
        self.failIf(app.retrieve6() != 77)
        
def main():
    unittest.main()

if __name__ == "__main__":
    main()
