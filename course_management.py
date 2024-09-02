def registrationu():
   import mysql.connector as ms
   con=ms.connect(host='localhost',user='root',passwd='Ankitha123',database='student_info')
   if con.is_connected():
         print()
   nm=input('enter student fullname')
   ag=int(input('enter student age'))
   ph=int(input('enter phone number'))
   eid=input('enter email id')
   import datetime
   dreg = datetime.datetime.now()
   cor=input('enter course name')
   cur=con.cursor()
   cur.execute ('insert into undergraduate values("{}",{},{},"{}","{}","{}")'.format(nm,ag,ph,eid,dreg,cor))
   con.commit()
   print()
   print('YOU HAVE BEEN SUCCESSFULLY REGISTERED TO THE CHOOSEN COURSE')
   print('PLEASE PAY THE SPECIFIED REGISTRATION FEES')
   print('THANK YOU FOR CHOOSING NJ UNIVERSITY')

def registrationi():
   import mysql.connector as ms
   con=ms.connect(host='localhost',user='root',passwd='Ankitha123',database='student_info')
   if con.is_connected():
         print()
   nm=input('enter student fullname')
   ag=int(input('enter student age'))
   ph=int(input('enter phone number'))
   eid=input('enter email id')
   import datetime
   dreg = datetime.datetime.now()
   cor=input('enter company name ')
   cur=con.cursor()
   cur.execute ('insert into internship values("{}",{},{},"{}","{}","{}")'.format(nm,ag,ph,eid,dreg,cor))
   con.commit()
   print()
   print('YOU HAVE BEEN SUCCESSFULLY REGISTERED FOR THE CHOSEN INTERNSHIP')
   print('THANK YOU FOR CHOOSING NJ UNIVERSITY')



#printing welcome note
print("""
                                WELCOME TO NJ UNIVERSITY
                      UNDERGRADUATE AND INTERNSHIP APPLICATION PORTAL
                                      BANGALORE
""")
from tabulate import tabulate
while True:
    import csv
    import matplotlib.pyplot as plt
    import numpy as np
    f1=open('graph.csv', 'w', newline='')
    print('PLEASE SELECT AMONG THE FOLLOWING')
    print('1. UNDERGRADUATE COURSES')
    print('2. INTERNSHIP')
    print('3. APPLICATION STATUS')
    ch=input('enter your desired choice')
    if ch=='1':
        print('PLEASE CHOOSE YOUR DESIRED FIELD')
        print('1.ARTS')
        print('2.BUSINESS')
        print('3.ENGINEERING')
        print('4.MEDICAL')
        OP=input('enter your desired field')
        import mysql.connector as ms
        con=ms.connect(host='localhost',user='root',passwd='Ankitha123',database='undergraduate')
        if con.is_connected():
            print()
        print('PLEASE SELECT AMONG THE FOLLOWING')
        print('1.VIEW ALL COURSES')
        print('2.FILTER COURSES')
        A=input('enter your desired choice')
           
        if OP=='1':
            if A=='1':
                cur=con.cursor();
                cur.execute('select * from arts')
                z=cur.fetchall()
                  
                print(tabulate(z,headers=['sno','course name','duration','subject','pass percentage','yearly fees','registration fees','seat left'],tablefmt='grid'))

            elif A=='2':
                print('1.SELECT BY SUBJECT COMBINATION')
                print('2.SELECT BY POPULARITY')
                CH=input('enter your desired choice')
                if CH=='1':
                    cur=con.cursor();
                    cur.execute('select sno,subject from arts')
                    y=cur.fetchall()
                    print(tabulate(y,headers=['sno','subject combination']))
                    sc=input('PLEASE ENTER YOUR SUBJECT PREFERENCES')
                    cur=con.cursor();
                    cur.execute('select * from arts where subject="{}"'.format(sc))
                    x=cur.fetchall()
                    print()
                    print(tabulate(x,headers=['sno','course name','duration','subject','pass percentage','yearly fees','registration fees','seat left'],tablefmt='grid'))
                                   
                elif CH=='2':
                   print("2016-21 COURSES AT NJ UNIVERSITY")
                   print("please choose an option ")
                   grp=int(input("1.graph 2.pie chart \n "))
                   if grp==1:
                      x1val=np.array([2016,2017,2018,2019,2020,2021])
                      y1val=np.array([100,120,120,150,140, 160])
                      plt.plot(x1val,y1val,"-b", label="bachelor in fine arts")
                      x2val=np.array([2016,2017,2018,2019,2020,2021])
                      y2val=np.array([150,150,180,200,180,190])
                      plt.plot(x2val,y2val, "-r", label="bachelor of journalism")
                      x3val=np.array([2016,2017,2018,2019,2020,2021])
                      y3val=np.array([130,140,160,150,170,160])
                      plt.plot(x3val,y3val, "-o", label="bachelor of fashion designing")
                      x4val=np.array([2016,2017,2018,2019,2020,2021])
                      y4val=np.array([180,200,230,210,200,190])
                      plt.plot(x4val,y4val, "-y", label="bachelor of hotel management")
                      plt.legend(loc="upper right")
                      plt.show()

                      
                   elif grp==2:
                       lb=['bachelor in fine arts','bachelor of journalism', 'bachelor of fashion designing', 'bachelor of hotel management']
                       y1=[100,150,120,200]
                       p=plt.figure(figsize=(5,3))
                       plt.pie(y1,labels=lb)
                       plt.show()

                   else:
                      print('PLEASE SELECT A GIVEN OPTION')
                      break
                       
                else:
                   print('PLEASE SELECT A GIVEN OPTION')
                   break
                      
        elif OP=='2':
            if A=='1':
                cur=con.cursor();
                cur.execute('select * from business')
                z=cur.fetchall()
                  
                print(tabulate(z,headers=['sno','course name','duration','subject','pass percentage','yearly fees','registration fees','seat left'],tablefmt='grid'))

            elif A=='2':
                print('1.SELECT BY SUBJECT COMBINATION')
                print('2.SELECT BY POPULARITY')
                CH=input('enter your desired choice')
                if CH=='1':
                    print('Maths,Economics,Accountancy,Business studies')
                    print('Maths,Economics,Accountancy,Business studies,Physics/Chemistry/Biology ')
                    print('Physics,Chemistry,Maths,Biology,Business studies')
                    sc=input('PLEASE ENTER YOUR SUBJECT PREFERENCES')
                    cur=con.cursor();
                    cur.execute('select * from business where subject="{}"'.format(sc))
                    x=cur.fetchall()
                    print()
                    print(tabulate(x,headers=['sno','course name','duration','subject','pass percentage','yearly fees','registration fees','seat left'],tablefmt='grid'))
                                   
                elif CH=='2':
                   print("2016-21 COURSES AT NJ UNIVERSITY")
                   print("please choose an option ")
                   grp=int(input("1.graph 2.pie chart \n "))
                   if grp==1:
                      x1val=np.array([2016,2017,2018,2019,2020,2021])
                      y1val=np.array([200,350,380,400,450, 450])
                      plt.plot(x1val,y1val,'-b', label='bachelor of accountancy')
                      x2val=np.array([2016,2017,2018,2019,2020,2021])
                      y2val=np.array([200,300,350,380,320,370])
                      plt.plot(x2val,y2val, '-r', label='bachelor of business')
                      x3val=np.array([2016,2017,2018,2019,2020,2021])
                      y3val=np.array([250,310,300,290,350,380])
                      plt.plot(x3val,y3val, '-o', label='bachelor of business aviation')
                      x4val=np.array([2016,2017,2018,2019,2020,2021])
                      y4val=np.array([250,280,250,290,320,380])
                      plt.plot(x4val,y4val, '-y', label='bachelor in maritime studies')
                      plt.legend(loc='upper right')
                      plt.show()
                   elif grp==2:
                      lb=['bachelor of accountancy','bachelor of business', 'bachelor of business aviation', 'bachelor in maritime studies']
                      y1=[380,350,300,250]
                      p=plt.figure(figsize=(5,3))
                      plt.pie(y1,labels=lb)
                      plt.show()
                   else:
                      print('PLEASE SELECT A GIVEN OPTION')
                      break
                else:
                   print('PLEASE SELECT A GIVEN OPTION')
                   break                     

        elif OP=='3':
            if A=='1':
                cur=con.cursor();
                cur.execute('select * from engineering')
                z=cur.fetchall()
                  
                print(tabulate(z,headers=['sno','course name','duration','subject','pass percentage','yearly fees','registration fees','seat left'],tablefmt='grid'))

            elif A=='2':
                print('1.SELECT BY SUBJECT COMBINATION')
                print('2.SELECT BY POPULARITY')
                CH=input('enter your desired choice')
                if CH=='1':
                    
                    print('Physics,Chemistry,Maths')
                    print('Physics,Chemistry,Maths,Biology')
                    sc=input('PLEASE ENTER YOUR SUBJECT PREFERENCES')
                    cur=con.cursor();
                    cur.execute('select * from engineering where subject="{}"'.format(sc))
                    x=cur.fetchall()
                    print()
                    print(tabulate(x,headers=['sno','course name','duration','subject','pass percentage','yearly fees','registration fees','seat left'],tablefmt='grid'))
                                   
                elif CH=='2':
                   print("2016-21 COURSES AT NJ UNIVERSITY")
                   print("please choose an option ")
                   grp=int(input("1.graph 2.pie chart \n "))
                   if grp==1:
                      x1val=np.array([2016,2017,2018,2019,2020,2021])
                      y1val=np.array([200,350,330,360,400, 430])
                      plt.plot(x1val,y1val,'-b', label='aerospace engineering')
                      x2val=np.array([2016,2017,2018,2019,2020,2021])
                      y2val=np.array([100,230,90,180,300,200])
                      plt.plot(x2val,y2val, '-r', label='bio engineering')
                      x3val=np.array([2016,2017,2018,2019,2020,2021])
                      y3val=np.array([300,300,300,200,320,200])
                      plt.plot(x3val,y3val, '-o', label='civil engineering')
                      x4val=np.array([2016,2017,2018,2019,2020,2021])
                      y4val=np.array([250,270,230,328,323,103])
                      plt.plot(x4val,y4val, '-y', label='computer science engineering')
                      x5val=np.array([2016,2017,2018,2019,2020,2021])
                      y5val=np.array([150,160,310,404,321,415])
                      plt.plot(x5val,y5val, '-p', label='electrical engineering')
                      x6val=np.array([2016,2017,2018,2019,2020,2021])
                      y6val=np.array([280,200,322,512,370,210])
                      plt.plot(x6val,y6val, '-v', label='mechanical engineering')
                      plt.legend(loc='upper right')
                      plt.show()
                   elif grp==2:
                      lb=['mechanical engineering','civil engineering', 'bio engineering', 'cs engineering', 'electricaleng', 'aerospace eng']
                      y1=[280,300,100,250,150,200]
                      p=plt.figure(figsize=(5,3))
                      plt.pie(y1,labels=lb)
                      plt.show()
                   else:
                      print('PLEASE SELECT A GIVEN OPTION')
                      break
                else:
                   print('PLEASE SELECT A GIVEN OPTION')
                   break                      

        elif OP=='4':
            if A=='1':
                cur=con.cursor();
                cur.execute('select * from medicine')
                z=cur.fetchall()
                  
                print(tabulate(z,headers=['sno','course name','duration','subject','pass percentage','yearly fees','registration fees','seat left'],tablefmt='grid'))

            elif A=='2':
                print('1.SELECT BY SUBJECT COMBINATION')
                print('2.SELECT BY POPULARITY')
                CH=input('enter your desired choice')
                if CH=='1':
                    
                    print('Physics,Chemistry,Zoology,Botany')
                    print('Physics,Chemistry,Zoology,Botany,Maths')
                    sc=input('PLEASE ENTER YOUR SUBJECT PREFERENCES')
                    cur=con.cursor();
                    cur.execute('select * from medicine where subject="{}"'.format(sc))
                    x=cur.fetchall()
                    print()
                    print(tabulate(x,headers=['sno','course name','duration','subject','pass percentage','yearly fees','registration fees','seat left'],tablefmt='grid'))
                                   
                elif CH=='2':
                   print("2016-21 COURSES AT NJ UNIVERSITY")
                   print("please choose an option ")
                   grp=int(input("1.graph 2.pie chart \n "))
                   if grp==1:
                      x1val=np.array([2016,2017,2018,2019,2020,2021])
                      y1val=np.array([320,330,380,360,300, 300])
                      plt.plot(x1val,y1val,'-b', label='bachelor of medicine and surgery')
                      x2val=np.array([2016,2017,2018,2019,2020,2021])
                      y2val=np.array([400,390,370,410,400,420])
                      plt.plot(x2val,y2val, '-r', label='bachelor of ayurvedic medicine')
                      x3val=np.array([2016,2017,2018,2019,2020,2021])
                      y3val=np.array([300,270,290,300,310,300])
                      plt.plot(x3val,y3val, '-o', label='bachelor of pharmacy')
                      x4val=np.array([2016,2017,2018,2019,2020,2021])
                      y4val=np.array([250,250,280,270,300,290])
                      plt.plot(x4val,y4val, '-y', label='nursing')
                      plt.legend(loc='upper right')
                      plt.show()
                   elif grp==2:
                      lb=['bachelor of medicine and surgery','bachelor of ayurvedic medicine', 'bachelor of pharmacy', 'nursing']
                      y1=[320,400,300,250]
                      p=plt.figure(figsize=(5,3))
                      plt.pie(y1,labels=lb)
                      plt.show()
                   else:
                      print('PLEASE SELECT A GIVEN OPTION')
                      break                      
        else:
            print('PLEASE SELECT A GIVEN OPTION')
            break                       
       

    elif ch=='2':
        print('PLEASE CHOOSE YOUR DESIRED FIELD')
        print('1.ENGLISH')
        print('2.HISTORY')
        print('3.LAW')
        print('4.MEDICAL')
        print('5.PSYCHOLOGY')
        OP=input('enter your desired field')
        import mysql.connector as ms
        con=ms.connect(host='localhost',user='root',passwd='Ankitha123',database='internships')
        if con.is_connected():
            print()
        print('PLEASE SELECT AMONG THE FOLLOWING')
        print('1.VIEW ALL COURSES')
        print('2.FILTER COURSES')
        A=input('enter your desired choice')
        if OP=='1':
            if A=='1':
                cur=con.cursor();
                cur.execute('select * from english')
                z=cur.fetchall()
                  
                print(tabulate(z,headers=['sno','company name','designation','degree','salary','minimum age'],tablefmt='grid'))

            elif A=='2':
                print('1.SELECT BY DEGREE')
                print('2.SELECT BY DESIGNATION')
                CH=input('enter your desired choice')
                if CH=='1':
                    print('BA')
                    print('B.ED')
                    print('MA')
                    dg=input('PLEASE ENTER YOUR DEGREE')
                    cur=con.cursor();
                    cur.execute('select * from english where degree="{}"'.format(dg))
                    x=cur.fetchall()
                    print()
                    print(tabulate(x,headers=['sno','company name','designation','degree','salary','minimum age'],tablefmt='grid'))
                elif CH=='2':
                    cur=con.cursor();
                    cur.execute('select sno,design from english')
                    y=cur.fetchall()
                    print(tabulate(y,headers=['sno','designation'],tablefmt='grid'))
                    ds=input('PLEASE ENTER YOUR PREFERRED DESIGNATION')
                    cur=con.cursor();
                    cur.execute('select * from english where design="{}"'.format(ds))
                    u=cur.fetchall()
                    print(tabulate(u,headers=['sno','company name','designation','degree','salary','minimum age'],tablefmt='grid')) 
                    
                    
                    
        elif OP=='2':
            if A=='1':
                cur=con.cursor();
                cur.execute('select * from history')
                z=cur.fetchall()
                  
                print(tabulate(z,headers=['sno','company name','designation','degree','salary','minimum age'],tablefmt='grid'))

            elif A=='2':
                print('1.SELECT BY DEGREE')
                print('2.SELECT BY DESIGNATION')
                CH=input('enter your desired choice')
                if CH=='1':
                    print('BA')
                    print('BS')
                    print('PHD')
                    dg=input('PLEASE ENTER YOUR DEGREE')
                    cur=con.cursor();
                    cur.execute('select * from history where degree="{}"'.format(dg))
                    x=cur.fetchall()
                    print()
                    print(tabulate(x,headers=['sno','company name','designation','degree','salary','minimum age'],tablefmt='grid'))
                elif CH=='2':
                    cur=con.cursor();
                    cur.execute('select sno,design from history')
                    y=cur.fetchall()
                    print(tabulate(y,headers=['sno','designation'],tablefmt='grid'))
                    ds=input('PLEASE ENTER YOUR PREFERRED DESIGNATION')
                    cur=con.cursor();
                    cur.execute('select * from history where design="{}"'.format(ds))
                    u=cur.fetchall()
                    print(tabulate(u,headers=['sno','company name','designation','degree','salary','minimum age'],tablefmt='grid')) 
                    

        elif OP=='3':
            if A=='1':
                cur=con.cursor();
                cur.execute('select * from history')
                z=cur.fetchall()
                  
                print(tabulate(z,headers=['sno','company name','designation','degree','salary','minimum age'],tablefmt='grid'))

            elif A=='2':
                print('1.SELECT BY DEGREE')
                print('2.SELECT BY DESIGNATION')
                CH=input('enter your desired choice')
                if CH=='1':
                    print('JD')
                    print('LLM')
                    dg=input('PLEASE ENTER YOUR DEGREE')
                    cur=con.cursor();
                    cur.execute('select * from law where degree="{}"'.format(dg))
                    x=cur.fetchall()
                    print()
                    print(tabulate(x,headers=['sno','company name','designation','degree','salary','minimum age'],tablefmt='grid'))
                elif CH=='2':
                    cur=con.cursor();
                    cur.execute('select sno,design from law')
                    y=cur.fetchall()
                    print(tabulate(y,headers=['sno','designation']))
                    ds=input('PLEASE ENTER YOUR PREFERRED DESIGNATION')
                    cur=con.cursor();
                    cur.execute('select * from law where design="{}"'.format(ds))
                    u=cur.fetchall()
                    print(tabulate(u,headers=['sno','company name','designation','degree','salary','minimum age'],tablefmt='grid'))


        elif OP=='4':
            if A=='1':
                cur=con.cursor();
                cur.execute('select * from medical')
                z=cur.fetchall()
                  
                print(tabulate(z,headers=['sno','company name','designation','degree','salary','minimum age'],tablefmt='grid'))

            elif A=='2':
                print('1.SELECT BY DEGREE')
                print('2.SELECT BY DESIGNATION')
                CH=input('enter your desired choice')
                if CH=='1':
                    print('MBBS')
                    print('MS')
                    print('MD')
                    dg=input('PLEASE ENTER YOUR DEGREE')
                    cur=con.cursor();
                    cur.execute('select * from medical where degree="{}"'.format(dg))
                    x=cur.fetchall()
                    print()
                    print(tabulate(x,headers=['sno','company name','designation','degree','salary','minimum age'],tablefmt='grid'))
                elif CH=='2':
                    cur=con.cursor();
                    cur.execute('select sno,design from medical')
                    y=cur.fetchall()
                    print(tabulate(y,headers=['sno','designation'],tablefmt='grid'))
                    ds=input('PLEASE ENTER YOUR PREFERRED DESIGNATION')
                    cur=con.cursor();
                    cur.execute('select * from medical where design="{}"'.format(ds))
                    u=cur.fetchall()
                    print(tabulate(u,headers=['sno','company name','designation','degree','salary','minimum age'],tablefmt='grid'))


        elif OP=='5':
            if A=='1':
                cur=con.cursor();
                cur.execute('select * from psychology')
                z=cur.fetchall()
                  
                print(tabulate(z,headers=['sno','company name','designation','degree','salary','minimum age'],tablefmt='grid'))

            elif A=='2':
                print('1.SELECT BY DEGREE')
                print('2.SELECT BY DESIGNATION')
                CH=input('enter your desired choice')
                if CH=='1':
                    print('MAP')
                    print('MS')
                    print('PHD')
                    print('PYSD')
                    dg=input('PLEASE ENTER YOUR DEGREE')
                    cur=con.cursor();
                    cur.execute('select * from psychology where degree="{}"'.format(dg))
                    x=cur.fetchall()
                    print()
                    print(tabulate(x,headers=['sno','company name','designation','degree','salary','minimum age'],tablefmt='grid'))
                elif CH=='2':
                    cur=con.cursor();
                    cur.execute('select sno,design from psychology')
                    y=cur.fetchall()
                    print(tabulate(y,headers=['sno','designation'],tablefmt='grid'))
                    ds=input('PLEASE ENTER YOUR PREFERRED DESIGNATION')
                    cur=con.cursor();
                    cur.execute('select * from psychology where design="{}"'.format(ds))
                    u=cur.fetchall()
                    print(tabulate(u,headers=['sno','company name','designation','degree','salary','minimum age'],tablefmt='grid'))
      

    elif ch=='3':
       print('1. UNDERGRADUATE')
       print('2. INTERNSHIP')
       ans=input('choose a desired option')
       if ans=='1':
          import mysql.connector as ms
          con=ms.connect(host='localhost',user='root',passwd='Ankitha123',database='student_info')
          if con.is_connected():
              cur=con.cursor()
              nm=input('enter student name')
              cur.execute('select * from undergraduate where name like "{]" '.format(nm))
              rec=cur.fetchall()
              print(tabulate(rec,headers=['name','age','phone number','email id','date of registration','course'],tablefmt='grid'))
          else:
             print('SORRY, NO RECORDS FOUND. PLEASE MAKE SURE YOU HAVE ENTERED THE RIGHT NAME ')
       elif ans=='2':
          import mysql.connector as ms
          con=ms.connect(host='localhost',user='root',passwd='Ankitha123',database='student_info')
          if con.is_connected():
              cur=con.cursor()
              nm=input('enter student name')
              cur.execute('select * from internship where name like "{}" '.format(nm))
              rec=cur.fetchall()
              print(tabulate(rec,headers=['name','age','phone number','email id','date of registration','company name'],tablefmt='grid'))
              break
          else:
             print('SORRY, NO RECORDS FOUND. PLEASE MAKE SURE YOU HAVE ENTERED THE RIGHT NAME ')
             break

       else:
         print('PLEASE SELECT A GIVEN OPTION')
         break
          
          
       
    f1.close()                 
    print('1. REGISTER YOURSELF')
    print('2. VIEW ANOTHER COURSE')
    RG=input('enter your desired choice')
    if RG=='1':
       print('1. UNDERGRADUATE')
       print('2. INTERNSHIP')
       sel=input('choose a desired option')
       if sel=='1':
         registrationu()
         break
       elif sel=='2':
         registrationi()
         break
    else:
         continue 
