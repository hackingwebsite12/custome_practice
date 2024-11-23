

class Test_good:
    @staticmethod
    def add(a,b):
        return a+b

    def fin(self):
       a =  Test_good.add(2,4)
       print(a)

tg = Test_good()
tg.fin()
