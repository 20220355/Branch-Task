import math
class Problem:
    def __init__(self):    
       print("name")
       print("a")

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
        
    


        
