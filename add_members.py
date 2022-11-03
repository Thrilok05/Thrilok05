choice=input("1. Add member\
                        2. delete member\
                        3. deposit\
                        ")
while choice=='1':
    a=list()
    name_list=list()

#function
    def rep_member(num):
        for i in range(num):
            b=input("Enter name {}:  ".format(i+1))
            a.append(b)

#to accept number
        for j in a:
             c=int(input("Enter number {} :  ".format(j)))
             if len(str(c))<10:
                 raise Exception("doesn't contain 10 numbers!")
             name_list.append(c)


#to try without errors
    try:
        x=int(input("Enter no.s of members:  "))

        
    except:
        print("Please try again")
        break

#calling a function
    else:
        rep_member(x)

        members=dict(zip(a,name_list))
        print(str(members))

