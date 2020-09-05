import math
import numpy.matlib
import numpy as np
#Global variable ; list
x = [[0] * 2 for i in range(2)]
y = [[0] * 3 for j in range(3)]
list = []
L = [] 
f = 0

#Function to create 2x2 Matrix
def mat2():
    import numpy.matlib
    import numpy as np

    for i in range(2):
        for j in range(2):
            x[i][j] = int(input())
        
    print(np.matrix(x))
    
    
#Function to create 3x3 Matrix
def mat3():
    import numpy.matlib
    import numpy as np

    for i in range(3):
        for j in range(3):
            y[i][j] = int(input())
        
    print(np.matrix(y))
    
    
#Function to find characterstic equation
def equation(x,y,n):
    #2x2 Matrix
    if n==2:
        s1 = x[0][0]+x[1][1]
        s2 = (x[0][0]*x[1][1]) - (x[0][1]*x[1][0])

        
        if s1==0:
            if s2>0:
                print("The Characterstic equation of given matrix is A^2 + {} = 0".format(s2))
            elif s2<0:
                s2=-s2
                print("The Characterstic equation of given matrix is A^2 - {} = 0".format(s2))
                
        elif s2==0:
            if s1>0:
                print("The Characterstic equation of given matrix is A^2 - {}A = 0".format(s1))
            elif s1<0:
                s1=-s1
                print("The Characterstic equation of given matrix is A^2 + {}A = 0".format(s1))
                
                
    
        elif s1<0 and s2>0:
            s1=-s1
            print("The Characterstic equation of given matrix is A^2 + {}A + {} = 0".format(s1,s2))
        elif s1>0 and s2>0:
            print("The Characterstic equation of given matrix is A^2 - {}A + {} = 0".format(s1,s2))
        elif s1>0 and s2<0:
            s2=-s2
            print("The Characterstic equation of given matrix is A^2 - {}A - {} = 0".format(s1,s2))
        elif s1<0 and s2<0:
            s1=-s1
            s2=-s2
            print("The Characterstic equation of given matrix is A^2 + {}A - {} = 0".format(s1,s2))
            
        
     
    #3x3 Matrix
    elif n==3:
        s1 = y[0][0]+y[1][1]+y[2][2]
        a = (y[1][1]*y[2][2]) - (y[1][2]*y[2][1])
        b = (y[0][0]*y[2][2]) - (y[0][2]*y[2][0])
        c = (y[0][0]*y[1][1]) - (y[0][1]*y[1][0])
        A = (y[1][1]*y[2][2]) - (y[1][2]*y[2][1])
        B = (y[1][0]*y[2][2]) - (y[1][2]*y[2][0])
        C = (y[1][0]*y[2][1]) - (y[1][1]*y[2][0])
        
        s2 = a + b + c
        s3 = y[0][0]*A - y[0][1]*B + y[0][2]*C
        
        if s1==0:
            if s2>0 and s3>0:
                print("The Characterstic equation of given Matrix is A^3 + {}A - {} = 0".format(s2,s3))
            elif s2<0 and s3<0:
                s2=-s2
                s3=-s3
                print("The Characterstic equation of given Matrix is A^3 - {}A + {} = 0".format(s2,s3))
            elif s2>0 and s3<0:
                s3=-s3
                print("The Characterstic equation of given Matrix is A^3 + {}A + {} = 0".format(s2,s3))
            elif s2<0 and s3>0:
                s2=-s2
                print("The Characterstic equation of given Matrix is A^3 - {}A - {} = 0".format(s2,s3))
        
        elif s2==0:
            if s1>0 and s3>0:
                print("The Characterstic equation of given Matrix is A^3 - {}A^2 - {} = 0".format(s1,s3))
            elif s1<0 and s3<0:
                s1=-s1
                s3=-s3
                print("The Characterstic equation of given Matrix is A^3 + {}A^2 + {} = 0".format(s1,s3))
            elif s1>0 and s3<0:
                s3=-s3
                print("The Characterstic equation of given Matrix is A^3 - {}A^2 + {} = 0".format(s1,s3))
            elif s1<0 and s3>0:
                s1=-s1
                print("The Characterstic equation of given Matrix is A^3 + {}A^2 - {} = 0".format(s1,s3))
                
                
        elif s3==0:
            if s2>0 and s1>0:
                print("The Characterstic equation of given Matrix is A^3 - {}A^2 + {}A = 0".format(s1,s2))
            elif s2<0 and s1<0:
                s2=-s2
                s1=-s1
                print("The Characterstic equation of given Matrix is A^3 + {}A^2 - {}A = 0".format(s1,s2))
            elif s2>0 and s1<0:
                s1=-s1
                print("The Characterstic equation of given Matrix is A^3 + {}A^2 + {}A = 0".format(s1,s2))
            elif s2<0 and s1>0:
                s2=-s2
                print("The Characterstic equation of given Matrix is A^3 - {}A^2 + {}A = 0".format(s1,s2))
            
        
        elif s1>0 and s2>0 and s3>0:
            print("The Characterstic equation of given Matrix is A^3 - {}A^2 + {}A - {} = 0".format(s1,s2,s3))
        elif s1<0 and s2<0 and s3<0:
            s1=-s1
            s2=-s2
            s3=-s3
            print("The Characterstic equation of given Matrix is A^3 + {}A^2 - {}A + {} = 0".format(s1,s2,s3))
        elif s1>0 and s2>0 and s3<0:
            s3=-s3
            print("The Characterstic equation of given Matrix is A^3 - {}A^2 + {}A + {} = 0".format(s1,s2,s3))
        elif s1>0 and s2<0 and s3>0:
            s2=-s2
            print("The Characterstic equation of given Matrix is A^3 - {}A^2 - {}A - {} = 0".format(s1,s2,s3))
        elif s1<0 and s2>0 and s3>0:
            s1=-s1
            print("The Characterstic equation of given Matrix is A^3 + {}A^2 + {}A - {} = 0".format(s1,s2,s3))
        elif s1<0 and s2<0 and s3>0:
            s1=-s1
            s2=-s2
            print("The Characterstic equation of given Matrix is A^3 + {}A^2 - {}A - {} = 0".format(s1,s2,s3))
        elif s1<0 and s2>0 and s3<0:
            s1=-s1
            s3=-s3
            print("The Characterstic equation of given Matrix is A^3 + {}A^2 + {}A + {} = 0".format(s1,s2,s3))
        elif s1>0 and s2<0 and s3<0:
            s2=-s2
            s3=-s3
            print("The Characterstic equation of given Matrix is A^3 - {}A^2 - {}A + {} = 0".format(s1,s2,s3))
            
            
#Function to find the eigen values of given Matrix        
def eigen(x,y,n,f):
    import math
    #2x2 Matrix
    #Eigen Values
    if n==2:
        s1 = x[0][0]+x[1][1]
        s2 = (x[0][0]*x[1][1]) - (x[0][1]*x[1][0])
        a = 1
        b = s1
        c = s2
        
        x = b*b - 4*a*c
        y = math.sqrt(x)
        
        val1 = (-b + y)/2*a
        val2 = (-b - y)/2*a
        
        if f==0:
            print("The eigen values of given matrix are {} and {} ".format(int(val1),int(val2)))
          
        
    #3x3 Matrix
    #Eigen values
    
    elif n==3:
        Li = []
        flag = 0
        s1 = y[0][0]+y[1][1]+y[2][2]
        a = (y[1][1]*y[2][2]) - (y[1][2]*y[2][1])
        b = (y[0][0]*y[2][2]) - (y[0][2]*y[2][0])
        c = (y[0][0]*y[1][1]) - (y[0][1]*y[1][0])
        A = (y[1][1]*y[2][2]) - (y[1][2]*y[2][1])
        B = (y[1][0]*y[2][2]) - (y[1][2]*y[2][0])
        C = (y[1][0]*y[2][1]) - (y[1][1]*y[2][0])
        
        s2 = a + b + c
        s3 = y[0][0]*A - y[0][1]*B + y[0][2]*C
        
        w = 1
        x = s1
        y = s2
        z = s3
        
        list.append(w)
        list.append(x)
        list.append(y)
        list.append(z)
        
        L = [-1,1,-2,2,-3,3]
        
        val = 0
        for i in L:
            ch = i**3 - x*i**2 + y*i - z
            if ch==0:
                flag = 1
                val = i
                break
            else:
                continue 
        x=-x
        z=-z
        
        list.clear()
        L.clear()
        
        list.append(w)
        list.append(x)
        list.append(y)
        list.append(z)
        j=0
        
        for i in list:
            j = val*j + i
            L.append(j)
            
        A = L[0]
        B = L[1]
        C = L[2]
        
        X = B*B - 4*A*C
        Y = math.sqrt(X)
        
        val1 = (-B + Y)/2*A
        val2 = (-B - Y)/2*A
        
        if f==0:
            print("The eigen values of given matrix are {} , {} and {} ".format(int(val),int(val1),int(val2)))
        elif f==1:
            Li.append(val)
            Li.append(val1)
            Li.append(val2)
            Li.sort()
            print("The Diagonalized Matrix looks as follows:")
            print("----------")
            print("{}  0  0".format(int(Li[0])))
            print("0  {}  0".format(int(Li[1])))
            print("0  0  {}".format(int(Li[2])))
            print("----------")
            
            
#Function to find A^n Matrix
def power(x,y,N,n):
    #2x2 Matrix
    if n==2:
        N=N-1
        import numpy.matlib
        import numpy as np
        new = np.asarray(x)
        
        for i in range(N):
            new = numpy.dot(new,x)
            
        print("The Martix is :")
        print (np.matrix(new))
    
    #3x3 Matrix
    elif n==3:
        import numpy.matlib
        import numpy as np
        N = N-1
        new = np.asarray(y)

        for i in range(N):
            new = numpy.dot(new,y)
            
        print("The Martix is :")
        print (np.matrix(new))
        
        
#Function to find Inverse of given Matrix
def inverse(x,y,n):
    #2x2 Matrix
    if n==2:
        dd = x[0][0]*x[1][1] - x[0][1]*x[1][1]
        d = 1/dd
        l1 =-x[0][1]*d
        l2 =-x[1][0]*d
        l0 = x[0][0]*d
        l3 = x[1][1]*d
        
        if d==0:
            print("Inverse doesn't exist :(")
        else:
            print("The Inverse of given Matrix is :")
            print("|  {}  {}  |".format(l3,l1))
            print("|  {}  {}  |".format(l2,l0))
            
    #3x3 Matrix
    elif n==3:
        A = (y[1][1]*y[2][2]) - (y[1][2]*y[2][1])
        B = (y[1][0]*y[2][2]) - (y[1][2]*y[2][0])
        C = (y[1][0]*y[2][1]) - (y[1][1]*y[2][0])
        d = y[0][0]*A - y[0][1]*B + y[0][2]*C
        
        if d==0:
            print("Inverse doesn't exist :(")
        else:
            L0 = y[1][1]*y[2][2] - y[2][1]*y[1][2]
            L1 = -(y[0][1]*y[2][2] - y[0][2]*y[2][1])
            L2 = y[0][1]*y[1][2] - y[1][1]*y[0][2]
            L3 = -(y[1][0]*y[2][2] - y[1][2]*y[2][0])
            L4 = y[0][0]*y[2][2] - y[0][2]*y[2][0]
            L5 = -(y[0][0]*y[1][2] - y[0][2]*y[1][0])
            L6 = y[1][0]*y[2][1] - y[2][0]*y[1][1]
            L7 = -(y[0][0]*y[2][1] - y[0][1]*y[2][0])
            L8 = y[0][0]*y[1][1] - y[0][1]*y[1][0]
            
            print("The Inverse of given Matrix is :")
            print("--------------")
            print("|   {}  {}  {}   |".format(L0/d,L1/d,L2/d))
            print("|   {}  {}  {}   |".format(L3/d,L4/d,L5/d))
            print("|   {}  {}  {}   |".format(L6/d,L7/d,L8/d))
            print("---------------")
            
            
        
#function for user choice
def options():
    i =''
    print("What kind of question do you want to solve?")
    print("1.Find characterstic equation")
    print("2.Find eigen values ")
    print("3.Diagonalize given matrix")
    print("4.All of the above")
    print("5.Find A^n Matrix")
    print("6.Find Inverse of Matrix A")
    
    opt = ['1','2','3','4','5','6']
    
    while i not in opt:
        i = input()
        
        if i not in opt:
            print("Ooops ! Try again :(")
            continue
        else:
            return (int(i))
 

#Main function where user choices are executed
def main():
    Flag = 0
    f = 0
    print("\tWelcome to Matrix 'O' Solve :D")
    while Flag!=1:
        print("Tell us what kind of matrix you want to solve?")
        print("1.2x2 Matrix \n2.3x3 Matrix")
        choice = int(input())
    
        if choice==1:
            mat2()
            print("Great! Let's solve the given 2x2 Matrix :)\n\n")
            size = 2
        elif choice==2:
            mat3()
            print("Great! Let's solve the given 3x3 Matrix :)\n\n")
            size = 3
        else:
            print("Oops! Invalid choice, Try again :(\n")
        
        ch = options()
        #characterstic equation
        import time
        start = time.time()
        if ch==1:
            equation(x,y,size)
            print('\n')
            import time
            end = time.time()
            elap_time = end - start
    
            print("Elapsed time : {} ".format(elap_time))
        
        #Eigen values and Eigen vectors
        elif ch==2:
            eigen(x,y,size,f)
            print("\n")
            import time
            end = time.time()
            elap_time = end - start
    
            print("Elapsed time : {} ".format(elap_time))
        
            
        elif ch==3:
            f = 1
            eigen(x,y,size,f)
            print("\n")
            import time
            end = time.time()
            elap_time = end - start
    
            print("Elapsed time : {} ".format(elap_time))
        
            
        elif ch==4:
            equation(x,y,size)
            print("\n")
            eigen(x,y,size,f)
            print("\n")
            f=1
            eigen(x,y,size,f)
            print("\n")
            import time
            end = time.time()
            elap_time = end - start
    
            print("Elapsed time : {} ".format(elap_time))
        
            
        elif ch==5:
            print("Enter n value:")
            no = int(input())
            power(x,y,no,size)
            print("\n")
            import time
            end = time.time()
            elap_time = end - start
    
            print("Elapsed time : {} ".format(elap_time))
        
        
        elif ch==6:
            inverse(x,y,size)
            print("\n")
            import time
            end = time.time()
            elap_time = end - start
    
            print("Elapsed time : {} ".format(elap_time))
        
        
        
        f = 0
        print("Would you like to continue? :)")
        print("Y Or N")
        response = input()
        if response=='Y':
            continue
        else:
            Flag = 1
            print("\tHope you got your answers real quick :D")
            print("\t**************Thank You*************** ")

main()

