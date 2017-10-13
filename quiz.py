import random
opt = ["Q: ","a: ","b: ","c: ","d: ","Correct Option: "]
qt = []
quest = {}

class m:
    count = 0
    def __init__(self,q,a,b,c,d,corrans):
        
        self.q = q
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.corrans =  corrans
        m.count = m.count +1

    def add(self):
        quest[m.count] = [self.q,self.a,self.b,self.c,self.d,self.corrans]

    def show(self):
        
        for i in quest:
            k = 0
            print("Question {}".format(i))
            for j  in quest[i]:
                
                print('{} {}'.format(opt[k],j))
                k+=1
            print('\n')    
    def quiz(self):
        corrcount = 0
        s = random.sample(range(1,m.count+1),m.count)
        totque = int(input("Enter the no. of questions needed: "))
        for i in range(1,totque+1):
            print("Question {}".format(i))
            q1 = quest[s[i-1]]
            print('{}\na: {}\nb: {}\nc: {}\nd: {}'.format(q1[0],q1[1],q1[2],q1[3],q1[4]))
            choice  = input("Enter The correct option: ")
            
            if choice == q1[5]:
                corrcount = corrcount + 1
        print("Your Total Score is {}/{}".format(corrcount,totque))
              

while True:
    
    print("1.Add Question\n2.Show Questions\n3.Start Quiz")
    a = int(input("Enter Your Choice: "))
    if a == 1:
        
        quest1 = input("Question Description: ")
        a = input("Option a: ")
        b = input("Option b: ")
        c = input("Option c: ")
        d = input("Option d: ")
        corans = input("Enter The correct option: ")
        obj1 = m(quest1,a,b,c,d,corans)
        obj1.add()
    
    elif a == 2:
        obj1.show()
    elif a == 3:
        obj1.quiz()

    
         
         
        
    
        
        
    
        
        
        
        
