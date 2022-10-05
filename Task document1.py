import math
class Problem:
    def __init__(self):    
        self.x = [41,32,30,23,24,32,11,39,24,46,50,18,41,14,33,50,38,25,32,16,43,19,35,22,46,43,10,22,17,47,66,48,25,43,28,31,12,25,12,48]
        self.x1 = []
        self.x2 = []
        self.x3 = []
        self.x4 = []
        self.x5 = []
        self.x6 = []

        self.mark= math.ceil((max(self.x)-min(self.x))/6)
        self.mark1= min(self.x)
        self.mark2= min(self.x) + self.mark
        self.mark3= self.mark2 + self.mark
        self.mark4= self.mark3 + self.mark
        self.mark5= self.mark4 + self.mark
        self.mark6= self.mark5 + self.mark
        self.mark7= self.mark6 + self.mark

    def class6(self):
       print("Task KIT")
            
    def table(self):
        print("don't exacts.")
           
    def graph(self):
        longmax = max([len(self.x1),len(self.x2),len(self.x3),len(self.x4),len(self.x5),len(self.x6)])
        for i in range(longmax):
            a=longmax-i
            b= round(longmax/len(self.x) - i/len(self.x),3)
            print('%.3f'%b,end='')
            if len(self.x1) >= a:
                print(' |*|',end='')
            else:
                print('    ',end='')
            if len(self.x2) >=a:
                print('   |*|',end='')
            else:
                print('      ',end='')
            if len(self.x3) >= a:
                print('   |*|',end='')
            else:
                print('      ',end='')
            if len(self.x4) >= a:
                print('   |*|',end='')
            else:
                print('      ',end='')
            if len(self.x5) >= a:
                print('   |*|',end='')
            else:
                print('      ',end='')
            if len(self.x6) >= a:
                print('   |*|')
            else:
                print()
        print('    ',(self.mark1+self.mark2)/2,end='  ')
        print((self.mark2+self.mark3)/2,end='  ')
        print((self.mark3+self.mark4)/2,end='  ')
        print((self.mark4+self.mark5)/2,end='  ')
        print((self.mark5+self.mark6)/2,end='  ')
        print((self.mark6+self.mark7)/2,end='  ')
pm=Problem()
pm.class6()
pm.table()
pm.graph()
        
    


        
