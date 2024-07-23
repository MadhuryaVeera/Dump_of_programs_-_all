##a=int(input('Enter a'))
##b=int(input('Enter b'))    #sum of two numbers
##c=a+b
##print(c)
##


##a=10
##print(a+b)
##   

##n=5
##for i in range(1,n+1):
##    for j in range(1,n+1):
##       if i=1 or i==n or j==1 or j==n:    #floyid triangles
##            print('*',end=' ')
##        else:
##            print(' ',end=' ')
##    print()


##n=int(input())
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if i==(n+1)//2 or j==(n+1)//2:  
##            print('*',end=' ')
##        else:
##            print(' ',end=' ')
##    print()


##n=int(input())
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if i==1 or i==3 or i==n or j==1 or j==3 or j==n:
##            print('*',end=' ')
##        else:
##            print(' ',end=' ')
##    print()


##n=int(input())
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        if i==(n//2)+1 or j==(n//2)+1:
##            print('*',end=' ')
##        else:
##            print(' ',end=' ')
##    print()
##        
                                                                                    
##n=int(input())
##i=1
##while i<=n:
##    j=1
##    while j<=n:
##        if i==1 or i==(n//2)+1 or i==n or j==1 or j==(n//2)+1 or j==n:
##            print('*',end=' ')
##        else:
##            print(' ',end=' ')
##        j+=1
##    print()
##    i+=1


##n=5
##for i in range(1,n+1):
##    for k in range(1,n-i+1):
##        print('@',end=' ')
##    for j in range(1,i+1):
##        print('*',end=' ')
##    print()

##n=5
##for i in range(1,n+1):
##    for k in range(1,n-i+1):(j in range 1,n+1)
##        print('@',end=' ')
##    for j in range(1,i+1):
##        print('* ',end=' ')
##    print()

##n=5
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        print(' ',end=' ')
##    for k in range(1,i+1):
##        print('*',end='')
##    print()

##n=5
##for i in range(1,n+1):
##    for j in range(1,n+1):
##        print(' ',end=' ')
##    for k in range(1,i+1):
##        print('a',end='')
##    print()


##n=int(input())
##for i in range (n):
##    for j in range(65,65+i+1):
##        print (chr(j),end=" ")
##
##    print()
##n=int(input())
##for i in range (n,-1,-1):
##    for j in range(65,65+i+1):      #floyid triangles
##        print (chr(j),end=" ")
##
##    print()



##def sample():
##    print(5)
##                                  #functions
##sample()
##print('SM')
##sample()
##print("RIYA")
##sample()

##send  the output functiona call-returns##
##return by default is a break statemen##


##def sample():
##    print(a+b)
##a,b=map(int,input().split())
##sample()



##def sample(a,b):
##    print(a-b)
##
##sample(2,1)#arguments/parameters(a,b)
##sample(3,2)



##def sample(a,b,c):
##    if c==1:
##        print(a+b)
##    elif c==2:
##        print(a-b)
##    elif c==3:
##        print(a*b)
##    elif c==4:
##        print(a/b)
##    else:
##        print("RJ")
##sample(1,2,3)
##
##a==10,b==20,c==30,d==40
##print(a<d)and(b>c)




##def add(a,b):
##    print(a+b)
##def sub(a,b):
##    print(a-b)
##def mul(a,b):
##    print(a*b)               
##def div(a,b):
##    print(a//b)
##
##a,b=map(int,input().split())
##c=int(input('enter choice(1,2,3,4): '))
##if c==1:
##    add(a,b)
##elif c==2:
##    sub(a,b)
##elif c==3:
##    mul(a,b)
##elif c==4:
##    div(a,b)
##else:
##    print('wrong input')
##



##def sample(n):#formal arguments#function definition
##    if n%2==0:
##      print(n,'even')
##    else:
##        print(n,'odd')
##        
##a=int(input())#actual parameters(the parameters which we egiven at)#function call
##sample(a)

        

##def sample(n):#formal parameters
##    if n%2==0:
##      return(n,'even')
##      print('done')
##    else:
##      return(n,'odd')
##
##a=int(input())#actual parameters
##x=sample(a)
##print(x)



##def sample(*s):
##    return s          ##*s which means taking all the elements in the funtion  call##
##d=sample(9,8,7,4)
##print(d)



##def prime(n):
##    for i in range(2,n//2+1):
##        if n%i==0:
##            return(False)
##        
##    else:                             #mega prime#
##       return(True)
##a=int(input())#53
##if prime(a):
##    s=1
##    while a>0:
##        rem=a%10
##        if prime(rem):
##            s=1
##        else:
##            s=0
##            print('Not a mega prime')
##            break
##        a//=10
##    if s:
##        print('mega prime')
##
##                                                                                    



##def sample(a):
##    print('inside 1',a)##inside 1 1
##    a=10#local variable
##    print('inside 2',a)##inside 2 10
##a=1 #global variable#                     #differnce bw global and local variable    
##sample(a)
##print(a,'outside',a)##1 outside 1


##def sample(a):
##    print('inside 1',a)##inside 1 15
##    a=565#local variable(only declared inside of the function)#
##    print('inside 2',a)##inside 2 565
##a=15 #global variable#                         
##sample(a)
##print('outside',b)#not working becausee of the 'b' is the local variablle#

##int- call by value
## string-

##def sample(a):
##    print('inside 1',a)
##    global b
##    a=565
##    print('inside 2',a)
##a=15                       
##sample(a)
##print('outside',b)



##def add(n):
##   if n==1:#
##       return 1
##   else:
##        return n+add(n-1)#5+4+3+2+1
##
##print(add(5))

##d = {0: 'a', 1: 'b', 2: 'c', 3: 'd'}
##d
##{0: 'a', 1: 'b', 2: 'c', 3: 'd'}

##list1=['apple','banana','orange']
##print(list1)
##list2=['apple','[8,4,6]','orange']
##print(list2)
####list1.append('guava')##to add the element
####print(list1)
##list1.extend('banana')
##print(list1)


##n=int(input("enter a value"))
##sum=0
##t=n
##while(t>0):                           ##armstrong number##(407(y),663(n))
##    digit=t%10
##    sum+=digit**3
##    t//=10
##if(n==sum):
## print("armstong")
##else:
## print("not armstrong")



##str=input("enter a string")
##a=list(str)
##temp=a[0]
##a[0]=a[-1]             #first character and last charaacter are interchanged#
##a[-1]=temp             #output:madhu--->uadhm
##print(" ".join(a))

##n=256
##i=2
##while(i<=n):
##     j=1
##     fac=0
##while(j<=i):
##      if(i%j==0):
##        fact=fact+1
##      j=j+1
##      if(fact==2):
##        print(1)
##i=i+1


##lower=1
##upper=256
##print("Prime numbers between",lower,"and",upper,"are:")
##for num in range(lower,upper+1):
##   if num>1:                                        #prime numbers#
##       for i in range(2,num):
##           if (num%i)==0:
##               break
##       else:
##           print(num)


##n=int(input("enter a number"))
##rev=0
##t=n
##while(n>0):
##   r=n%10                                #palindrome program#
##   rev=rev*10+r
##   n//=10
##if(t==rev):
##    print("palindrome")
##else:
##    print("not a palinfdrome")


#######################python built in functions##############################
###create a list
##my_list = [3, 5, 2, 8, 1, 4, 6, 7]
###append an element           ##[3, 5, 2, 8, 1, 4, 6, 7, 9]##
##my_list.append(9)
##print(my_list)


##new_list=[10,11,12]
##my_list=[3,5,2,8,1,4,6,7]   ##[3, 5, 2, 8, 1, 4, 6, 7, 10, 11, 12]##
##my_list.extend(new_list)
##print(my_list)


##my_list=[3,5,2,8,1,4,6,7]
##my_list.insert(0,0)         ##[0, 3, 5, 2, 8, 1, 4, 6, 7]##
##print(my_list)


##my_list=[3,5,2,8,1,4,6,7,]
##my_list.remove(5)                 ##[3, 2, 8, 1, 4, 6, 7]##
##print(my_list)

##popped_element=



























##n=list(map(int,input().split()))
##k=sorted(n)
##k.pop()
##k.pop()
##print(max(k))



##n=int(input())
##a=list(map(int,input().split()))
####s=sorted(a)
##print(s[-3])##
##n=int(input())
##a=list(map(int,input().split()))
##s=sorted(list(set(a)))
##print(s[-3])


##n=list(map(int,input().split()))
##k=max(n)
##n.remove(k)
##e=max(n)
##n.remove(e)
##print(max(n))##
##for i in range(2):
##    a.remove(max(a))
##print(max(a))


##a=list(map(int,input().split()))
##k=sorted(a)
##if k==a:
##  print(True)
##else:
##    print(False)
##      


##n=int(input())
##a=list(map(int,input().split()))
##i=a.index(max(a))
##if a[:i+1]==sorted(a[:i+1]) and a[i: ]==sorted(a[i:]),reverse=True):
##    print(True)
##else:
##    print(False)



##n=int(input())
##a=list(map(int,input()split()))
##o=[]
##e=[]
##for i in a:   
##    if i%2==0:
##      e.append(i)
##    else:
##        o.aappend(i)
##if len(o)>len(e):
##    print(o[-1])
##else:
##    print(e[-1])
##
##

##n=int(input())
##a=list(map(int,input().split()))
##o=[]
##e=[]
##for i in a:   
##    if i%2==0:
##      e.append(i)
##    else:
##        o.append(i)
##for i in range(n//2):
##    print(e[i],o[i])



##with open(r','r')as f:
##    a=f.read()
##    print(a)

##d=open(r'C:\Users\hari\OneDrive\Desktop\SM\carsweight.csv','r')
##s=d.readlines()
##a=[]
##for i in s:
##    a.append(i.split(','))
##d.close()
##
##c=0
##for i in a:
##    if i[2]>='5':
##        c+=1
##print(c)

##a=10
##a+b

##10+'x'


#################try###########
##try:
##    a=10
##    print(a)
##except:
##    print("hi")

##try:
##    a=10
##    print(a+'j')
##except:
##    print("hi")
##else:
##    print("BY")
##finally:
##    print("done")



a=int(input())
try:
    if a>=0 and a<100:
        if a<40:
            print("fail")
        else:
            print("pass")
    else:
        raise NameError
except NameError:
    print('not valid marks')
finally:
    print("all themarks")



#######################################oops####################################

##class car():
##    pass
##
##a=car()
##print(a)
##
##b=car()
##print(b)



##class car():
##    def __init__(self):
##        print('Hello')
##a=car()
##print(a)




##class car():
##    def __init__(self,name,model):##constructor##
##        print('hi')
##        self.name=name
##        self.model=model
##    def display(self):
##        print(self.name,self.model)
##a=car('kia',3112)
##a.display()
##
##b=car('sm',2113)
##b.display()




##class student():
##    def __init__(self,name,roll,sub1,sub2):
##        self.name=name
##        self.roll=roll###self.name as we call as the instance(change from obj to obj)###
##        self.sub1=sub1
##        self.sub2=sub2
##    def display(self):
##        print(self.name,self.roll,(self.sub1+self.sub2)/2)
##a=student('sm',20,1,1)
##a.display()
##b=student('ms',21,2,2)
##b.display()


##class student():
##    college="Aditya"## that it can be execute every  object####class variable####static varbile is college##
##    def __init__(self,name,roll,sub1,sub2,college):
##        self.name=name
##        self.roll=roll
##        self.sub1=sub1
##        self.sub2=sub2
##        self.college=college
##    def display(self):
##        print(self.name,self.roll,(self.sub1+self.sub2)/2,self.college)
##a=student('sm',20,1,1,'acet')
##a.display()
####b=student('ms',21,2,2)
####b.display()


##class student():
##    college="Aditya"
##    def __init__(self,name,roll,sub1,sub2,college):
##        self.name=name
##        self.roll=roll
##        self.sub1=sub1
##        self.sub2=sub2
##        self.college=college
##    def display(self):
##        print(self.name,self.roll,(self.sub1+self.sub2)/2,self.college)
##
##    @classmethod
##    def classm(cls):
##        cls.college='ACET'
##        print(cls.college)
##
##    @staticmethod
##    def sample():
##        print('hi')
##        
##a=student('sm',20,1,1,'acet')
##a.display()
##a.classm()
##a.sample()






##class student():
##    def __init__(self,name,roll,sub1,sub2):
##        self.name=name
##        self.roll=roll
##        self.sub1=sub1
##        self.sub2=sub2
##    def display(self):    #sep#--replace comma with given character##
##        print(self.name,self.roll,(self.sub1+self.sub2)/2,sep='*',end='')
##a=student('sm',20,1,1)   ##end##--next line lo print avutadi##
##a.display()
##b=student('ms',21,2,2)
##b.display()

 
##try:
##    raise Exception (1,2,3)
##except Exception as e:
##    print(len(e.args))

##my_string = 'abcdef'
##def fun(s):
##   del s[2]
##   return s
##print(fun(my_string))

##def fun(d, k, v):
##    d[k] = v
##my_dictionary = {} #None##output#
##print(fun(my_dictionary, '1', 'v'))

##x = """"""
##print(len(x))##acquire the prperties from the parent####super##


##x="\\\\\\\\\\"
##print(len(x))  #only used for the even nos##

##class person():
##    def __init__(self,name,aadhar):
##             self.name=name
##             self.aadhar=aadhar
##    def display(self):
##             print(self.name,self.aadhar)
##
##
##class student(person):
##    def __init__(self,roll,branch,name,aadhar):
##              self.roll=roll
##              self.branch=branch
##              super().__init__(name,aadhar)
##    def display(self):
##              print(self.name,self.aadhar,self.roll,self.branch)
##
##
##a=student("xyz",123456,"2203","cse")
##a.display()





##class person():
##    def __init__(self,name,aadhar):
##             self.name=name
##             self.aadhar=aadhar
##    def display(self):
##             print(self.name,self.aadhar)
##
##
##class student(person):
##    college='AECT'
##    def __init__(self,roll,branch,name,aadhar,college):
##              self.roll=roll
##              self.branch=branch
##              self.college=college
##              super().__init__(name,aadhar)
##    def display(self):
##              print(self.name,self.aadhar,self.roll,self.branch,self.college)
##
##output:::aec
##a=student("xyz",123456,"2203","cse","aec")
##a.display()




##class person():
##    college="ACET"
##    def __init__(self,name,aadhar):
##             self.name=name
##             self.aadhar=aadhar
##    def display(self):
##             print(self.name,self.aadhar)
##
##
##class student(person):
##    college="ACOE"
##    def __init__(self,roll,branch,name,aadhar,college):
##              self.roll=roll
##              self.branch=branch
##              
##              super().__init__(name,aadhar)
##    def display(self):
##              print(self.name,self.aadhar,self.roll,self.branch,self.college)
##
##output::ACOE
##a=student("xyz",123456,"2203","cse","aec")
##a.display()


##class person():
##    def __init__(self,name,aadhar,college):
##             self.name=name
##             self.aadhar=aadhar
##             self.college=college
##    def display(self):
##             print(self.name,self.aadhar,self.college)
##


##class student(person):
##    def __init__(self,roll,branch,name,aadhar,college):
##              self.roll=roll
##              self.branch=branch
##              self.college=college
##              super().__init__(name,aadhar,college)
##    def display(self):
##              print(self.name,self.aadhar,self.roll,self.branch,self.college)
##
##
##a=student("xyz",123456,"2203","cse","aec")
##a.display()



##n=int(input())
##l=list(map(int,input().split()))
##if n%2==0:
##    print(*l)


##n=int(input())
##l=list(map(int,input().split()))
##f=[]
##for i in l:
##    d=str(i)
##    print(len(d))


##n=int(input())
##l=list(map(int,input().split()))
##d=sorted(l,reverse=True)
##if l==d:
##    print(True)
##else:
##    print(False)


##n=str(input())
##for i in n:
##    print(*i[::-1])






















   

##import tkinter as tk
##from tkinter import messagebox
##a=tk.Tk()
##a.title('sample')
##def example():
##    messagebox.showinfo('hi','login successful')
##
##b=tk.Button(a,text='submit',bg='red',fg='blue',command=example)
##b.grid(row=0,column=0)
##a.mainloop()
####
####




##import tkinter as tk
##from tkinter import messagebox
##a=tk.Tk()
##a.title('sample')
##def example():
##    messagebox.askquestion('hi','login successful')
##
##b=tk.Button(a,text='submit',bg='red',fg='blue',command=example)
##b.grid(row=0,column=0)
##a.mainloop()



##import tkinter as tk
##from tkinter import messagebox
##a=tk.Tk()
##a.title('sample')
##def example():
##    x=int(c.get())
##    y=int(b.get())
##    print(x+y)
##
##b=tk.Entry()
##b.grid(row=0,column=0)
##c=tk.Entry()
##c.grid(row=0,column=2)
##d=tk.Button(a,text='submit',bg='red',fg='blue',command=example)
##d.grid(row=0,column=4)
##a.mainloop()
##


##from tkinter import *
##import tkinter as tk
##import calendar
##r=tk.Tk()
##r.geometry('400x300')
##r.title('Calender')
##
##def show():
##    m=int(month.get())
##    y=int(year.get())
##    output=calendar.month(y,m)
##    cal.insert('end',output)
##def clear():
##    cal.delete(1.0,'end')
##def exit():
##    r.destroy()
##
##m_label=Label(r,text="Month",font=('veranda','10','bold'))
##m_label.place(x=70,y=80)
##
##month=Spinbox(r,from_=1, to = 12,width="5")
##month.place(x=140,y=80)
##
##y_label=Label(r,text="Year")
##y_label.place(x=210,y=80)
##
##year=Spinbox(r,from_=2000, to =2020,width="8")
##year.place(x=260,y=80)
##
##cal=Text(r,width=33,height=8,relief=RIDGE,borderwidth=2)
##cal.place(x=70,y=110)
##
##show=Button(r,text="Show",command=show)
##show.place(x=140,y=250)
##
##clear=Button(r,text="clear",command=clear)
##clear.place(x=200,y=250)
##
##ex=Button(r,text="Exit",command=exit)
##ex.place(x=270,y=250)
##
##r.mainloop()


