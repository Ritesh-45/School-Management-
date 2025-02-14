#starting of code
#connecting to sql
import mysql.connector as sql
mydb=sql.connect(host="localhost",user="root",password="123456")
#creating data base
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS SCHOOL")
mycursor.execute("USE SCHOOL")
mycursor.execute("CREATE TABLE IF NOT EXISTS SIGNUP(USERNAME VARCHAR(20),PASSWORD NUMERIC(20))")
while True:
    print('1:Signup')
    print('2:Login')
    print('3:Exit')
    ch=int(input("Enter Your Choice:"))
    #signup   
    if ch==1:
        while True:
            username=input("USERNAME:")
            mycursor.execute("SELECT USERNAME FROM SIGNUP WHERE USERNAME='{}'".format(username))
            pet=mycursor.fetchone()
            if pet is None:
                password=input("Password:")
                mycursor.execute("INSERT INTO SIGNUP VALUES('{}','{}')".format(username,password))
                break
            else:
                print("Username Exist")
                break
    #login    
    if ch==2:
        username=input("USERNAME:")
        mycursor.execute("SELECT USERNAME FROM SIGNUP WHERE USERNAME='{}'".format(username))
        pot=mycursor.fetchone()
        if pot !=None:
            password=input("PASSWORD:")
            mycursor.execute("SELECT PASSWORD FROM SIGNUP WHERE PASSWORD='{}'".format(password))
            pat=mycursor.fetchall()
            if pat is not None:
                print('*****Login Sucessfull*****')
                mycursor.execute("CREATE TABLE IF NOT EXISTS STUDENT_DETAIL(ADMISSION_NO NUMERIC(10),NAME VARCHAR(20),PHONE_NO NUMERIC(15),DOB DATE,DATE_OF_ADMISSION DATE,GENDER VARCHAR(10),CATEGORY VARCHAR(10),MOTHER_TONGUE VARCHAR(10),RELEGION VARCHAR(10),FATHERS_NAME VARCHAR(20),MOTHERS_NAME VARCHAR(20))")
                mycursor.execute("CREATE TABLE IF NOT EXISTS TEACHERS_DETAIL(TEACHER_ID NUMERIC(10),NAME VARCHAR(20),PHONE_NO NUMERIC(15),GENDER VARCHAR(10),RELIGION VARCHAR(10),DOB DATE,DATE_OF_JOIN DATE,QUALIFICATION VARCHAR(20))")
                mydb.commit()
                #creating menu
                while True:
                    print('1:Add Student Detail')
                    print('2:Add Teacher Detail')
                    print('3:Delete Student Detail')
                    print('4:Delete Teacher Detail')
                    print('5:Edit Student Detail')
                    print('6:Edit Teacher Detail')
                    print('7:Search a Students')
                    print('8:Search a Teachers')
                    print('9:Exit')           
                    a=int(input("Enter Your Choice:"))
                    #adding student detail
                    if a==1:
                        times=int(input("No of students to be entered:"))
                        for i in range(times):
                            adno=int(input("Admission No       :"))
                            name=input("Name               :")
                            ph=int(input("Phone No           :"))
                            dob=input("Date               :")
                            doa=input("Date of Admission  :")
                            sex=input("Gender             :")
                            cat=input("Catagory           :")
                            lan=input("Mother Tongue      :")
                            rel=input("Relegion           :")
                            fname=input("Father's Name      :")
                            mname=input("Mother's Name      :")
                            mycursor.execute("INSERT INTO STUDENT_DETAIL VALUES({},'{}',{},'{}','{}','{}','{}','{}','{}','{}','{}')".format(adno,name,ph,dob,doa,sex,cat,lan,rel,fname,mname))
                            mydb.commit()
                    #adding teachers detail
                    if a==2:
                        times=int(input("No of teachers to be entered:"))
                        for i in range(times):
                            tid=int(input("Teacher Id      :"))
                            name=input("Name            :")
                            ph=int(input("Phone No        :"))
                            sex=input("Gender          :")
                            rel=input("Relegion        :")
                            dob=input("Date of Birth   :")
                            doj=input("Date of Join    :")
                            qua=input("Qualification   :")
                            mycursor.execute("INSERT INTO TEACHERS_DETAIL VALUES({},{}',{},'{}','{}','{}','{}','{}')".format(tid,name,ph,sex,rel,dob,doj,qua))
                            mydb.commit()
                    #Deleting student detail
                    if a==3:
                        adno=int(input("Enter Admission no of student to be deleted:"))
                        mycursor.execute("DELETE FROM STUDENT_DETAIL WHERE ADMISSION_NO={}".format(adno))
                        mydb.commit()
                    #deleting teachers detail
                    if a==4:
                        tid=int(input("Enter Teacher Id to be deleted:"))
                        mycursor.execute("DELETE FROM TEACHER_DETAIL WHERE TEACHER_ID={}".format(tid))
                        mydb.commit()
                    #Edditing student detail
                    if a==5:
                        print('1:Admission No')
                        print('2:Name')
                        print('3:Phone No')
                        print('4:Date Of Birth')
                        print('5:Date of Admission')
                        print('6:Gender')
                        print('7:Category')
                        print('8:Language')
                        print('9:Relegion')
                        print("10:Father's Name")
                        print("11:Mother's Name")
                        b=int(input("What you want to change:"))
                        #changing admission no
                        if b==1:
                            adno=int(input("Old Admission No:"))
                            nadno=int(input("New Admission No:"))
                            mycursor.execute("UPDQATE STUDENT_DETAIL SET ADMISSION_NO={} WHERE ADMISSION_NO={}".format(nadno,adno))
                            mydb.commit()
                        #changing name
                        if b==2:
                            name=input("Current Name:")
                            nname=input("Updated name:")
                            mycursor.execute("UPDATE STUDENT_DETAIL SET NAME='{}' WHERE NAME='{}'",format(nname,name))
                            mydb.commit()
                        #change phone no
                        if b==3:
                            ph=int(input("Current Phone No:"))
                            nph=int(input("New Phone No:"))
                            mycursor.execute("UPDATE STUDENT_DETAIL SET PHONE_NO={} WHERE PHONE_NO={}".format(nph,ph))
                            mydb.commit()
                        #changing dob
                        if b==4:
                            dob=input("Old DOB:")
                            ndob=input("Correct DOB:")
                            mycursor.execute("UPDATE STUDENT_DETAIL SET DOB='{}' WHERE DOB='{}'".format(ndob,dob))
                            mydb.commit()
                        #changing date of admission
                        if b==5:
                            doa=input("current Admission Date:")
                            ndoa=input("Correct Date of Admission:")
                            mycursor.execute("UPDATE STUDENT_DETAIL SET DATE_OF_ADMISSION='{}' WHERE DATE_OF_ADMISSION='{}'".format(ndoa,doa))
                            mydb.commit()
                        #changing gender
                        if b==6:
                            sex=input("Wrong Gender:")
                            nsex=input("Correct Gender:")
                            mycursor.execute("UPDATE STUDENT_DETAIL SET GENDER='{}' WHERE GENDER='{}'".format(nsex,sex))
                            mydb.commit()
                        #changing catagory
                        if b==7:
                            cat=input("Wrong Category:")
                            ncat=input("Correct Catagory:")
                            mycursor.execute("UPDATE STUDENT_DETAIL SET CATAGORY='{}' WHERE CATAGORY='{}'".format(ncat,cat))
                            mydb.commit()
                        #changing language
                        if b==8:
                            lan=input("Current Language:")
                            nlan=input("Updated Language:")                                                                                                                                                                    #code written by Ritesh Tikader
                            mycursor.execute("UPDATE STUDENT_DETAIL SET LANGUAGE='{}' WHERE LANGUSGE='{}'".format(nlan,lan))                                                                                                   # @ritesh.4525
                            mydb.commit()
                        #changing relegion
                        if b==9:
                            rel=input("Current Relegion:")
                            nrel=input("Updated Relegion:")
                            mycursor.execute("UPDATE STUDENT_DETAIL SET RELEGION='{}' WHERE RELEGION='{}'".format(nrel,rel))
                            mydb.commit()
                        #changing father name
                        if b==10:
                            fname=input("Present Father's Name:")
                            nfname=input("Updated Father's name:")
                            mycursor.execute("UPDATE STUDENT_DETAIL SET FATHERS_NAME='{}' WHERE FATHERS_NAME='{}'".format(nfname,fname))
                            mydb.commit()
                        #changing mothers name
                        if b==11:
                            mname=input("Present Mother's Name:")
                            nmname=input("Updated Mother's Name:")
                            mycursor.execute("UPDATE STUDENT_DETAIL SET MOTHERS_NAME='{}' WHERE MOTHERS_NAME='{}'".format(nmname,mname))
                            mydb.commit()
                    #edditing teachers detail
                    if a==6:
                        print("1:Teacher's ID")
                        print('2:Name')
                        print('3:Phone No')
                        print('4:Gender')
                        print('5:Relegion')
                        print('6:Date of Birth')
                        print('7:Date of Join')
                        print('8:Qualification')
                        c=int("What you want to change:")
                        #changing teachers id
                        if c==1:
                            tid=int(input("Old Teacher's ID:"))
                            ntid=int(input("New Teacher's ID:"))
                            mycursor.execute("UPDATE TEACHERS_DETAIL SET TEACCHER_ID={} WHERE TEACHER_ID={}".format(ntid,tid))
                            mydb.commit()
                        #changing name
                        if c==2:
                            name=input("Current Name:")
                            nname=input("Updated Name:")
                            mycursor.execute("UPDATE TEACHERS_DETAIL SER NAME='{}' WHERE NAME='{}'".format(nname,name))
                            mydb.commit()
                        #changing phone no
                        if c==3:
                            ph=int(input("Current Phone No:"))
                            nph=int(input("Updated Phone No:"))
                            mycursor.execute("UPDATE TEACHERS_DETAIL SET PHONE_NO={} WHERE PHONE_NO={}".format(nph,ph))
                            mydb.commit()
                        #changing gender
                        if c==4:
                            sex=input("Current Gender:")
                            nsex=input("Updated Gender:")
                            mycursor.execute("UPDATE TEACHERS_DETAIL SET GENDER='{}' WHERE GENDER='{}'".format(nsex,sex))
                            mydb.commit()
                        #changing relegion
                        if c==5:
                            rel=input("Current Relegion:")
                            nrel=input("Updated Relegion:")
                            mycursor.execute("UPDATE TEACHERS_DETAIL SET RELEGION='{}' WHERE RELEGION='{}'".format(nrel,rel))
                            mydb.commit()
                        #changing dob
                        if c==6:
                            dob=input("Wrong Date of Birth:")
                            ndob=input("Corrected Date of Birth:")
                            mycursor.execute("UPDATE TEACHERS_DETAIL SET DOB='{}' WHERE DOB='{}'".format(ndob,dob))
                            mydb.commit()
                        #changing date of join
                        if c==7:
                            doj=input("Wrong Date of Join:")
                            ndoj=input("Corrected Date of Join:")
                            mycursor.execute("UPDATE TEACHERS_DETAIL SET DATE_OF_JOIN='{}' WHERE DATE_OF_JOIN='{}'".format(ndoj,doj))
                            mydb.commit()
                        #changing qualification
                        if c==8:
                            qua=input("present Qualification:")
                            nqua=input("Updated Qualification:")
                            mycursor.execute("UPDATE TEACHERS_DETAIL SET QUALIFICATION='{}' WHERE QUALIFICATION='{}'".format(nqua,qua))
                            mydb.commit()
                    #search for student
                    if a==7:
                        print("Search Student By-")
                        print('1:By Admission No')
                        print('2:By Name')
                        d=int(input("Enter your choice:"))
                        #by admission no
                        if d==1:                                                                                             
                            adno=int(input("Admission No"))
                            mycursor.execute("SELECT*FROM STUDENT_DETAIL WHERE ADMISSION_NO={}".format(adno))
                            data=mycursor.fetchone()
                            if data !=None:
                                print(data)
                            else:
                                print("No Data Found")
                        #by name
                        if d==2:
                            name=input("Name:")
                            mycursor.execute("SELECT*FROM STUDENT_DETAIL WHERE NAME='{}'".format(name))
                            data=mycursor.fetchone()
                            if data !=None:
                                print(data)
                            else:
                                print("No Data Found")
                    #search for teacher
                    if a==8:
                        print("Search teacher by-")
                        print('1:By Teacher Id')
                        print('2:By Name')
                        e=int(input("Enter your choice:"))
                        #by teacher id
                        if e==1:
                            tid=int(input("Teachers ID:"))
                            mycursor.execute("SELECT*FROM TEACHERS_DETAIL WHERE TEACHER_ID={}".format(tid))
                            data=mycursor.fetchone()
                            if data !=None:
                                print(data)
                            else:
                                print("No Data found")
                        #search by name
                        if e==2:
                            name=input("Name:")
                            mycursor.execute("SELECT*FROM TEACHERS_DETAIL WHERE NAME='{}'".format(name))
                            data=mycursor.fetchone()
                            if data !=None:
                                print(data)
                            else:
                                print("No Deta Found")
                    #breakig while loop for menu
                    if a==9:
                        print("Thank You")
                        break
            #else statement for password clarification
            else:
                print("Incorrect Password")
        #else statement for username entry
        else:
            print("User Name not fount")
            print("Signup to add Username")
    #breakig while loop of login page
    if ch==3:
        print("Thank You")
        break
#disconnection from SQL database
mydb.close()
# end of code
