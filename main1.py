import mysql.connector                    #importing mysql connector
import urllib                             #importing urllib
import smtplib                            #importing smtp for sending emails
import re
import datetime                            #importing datetime module
from string import Template
from email.mime.multipart import MIMEMultipart       
from email.mime.text import MIMEText
import requests            #importing requests module
from bs4 import BeautifulSoup   #importing beautiful soup as bs4
      #function which returns the string which will be mailed for every series
from config import *
mydb = mysql.connector

base_link = 'https://www.imdb.com'           # base link of the site
def result(xx):
  x=xx
  link="https://www.imdb.com/find?ref_=nv_sr_fn&q="+x+"&s=all"  #searching the tv series on the site
  page=requests.get(link)
  soup=BeautifulSoup(page.text,'html.parser')
  par=soup.findAll('td',attrs={'class':'result_text'})        #search results
  found=0
  for la in par:                    #for every search result matching it with the input tv series
    if(la is None):
      break
    a=la.findAll('a')
    if(a is None):
      break
    for kx in a:
      title_match=kx.getText().strip().lower()
      if(title_match==xx.lower()):
        v=kx['href']
        found=1
        break
    if(found):
      break
  if(found==0):                            #if no tv series found for the input return no series found
    return "tv series not found"
  
  p=base_link+v                           #if tv series is found than go to the first link which matches with the input series name
  page = requests.get(p)                  
  soup = BeautifulSoup(page.text, 'html.parser')
  par = soup.find('div', attrs={'class':'seasons-and-year-nav'})  #parsing the seasons of that series from the last series details available
  if(par is None):
    return "series not found"          #if seasons not found return no series found
  a = par.findAll('a')
  today=datetime.date.today()
  ss=mm=0
  d2=''
  kk=0
  prin=0
  for x in a:                 
    blank=0
    value = x['href']
    if("sn" not in value):                           
      break
    page = requests.get(base_link + value)
    soup = BeautifulSoup(page.text, 'html.parser')
  
    for k in reversed(soup.findAll('div',attrs={'class':'airdate'})):  #traversing in reverse order from the last episode airdate to first
      l=k.getText().strip()     #airdate text
      if(l==''):          #no date available
        blank=1
        continue             
      if(len(l)==4):            #if only the year of the release is available
        if(int(l)>=2018):
          d2=l
          mm=1
        continue 
      elif(l[1]==' '):
        if(l[5]=='.'):                    #taking account of different date formats
          d=datetime.date(int(l[7:]),int(month(l[2:5])),int(l[0:1]))
        else:
          d=datetime.date(int(l[6:]),int(month(l[2:5])),int(l[0:1]))
      elif(not l[0].isdigit()):          #if date is not given only month and year is given ,then converting it into just year
          l=l[5:]
          if(int(l)>=2018):
            d2=l
            mm=1
          continue 
      else:
        if(l[6]=='.'):                    #whole date available
          d=datetime.date(int(l[8:]),int(month(l[3:6])),int(l[0:2]))
        else:
          d=datetime.date(int(l[7:]),int(month(l[3:6])),int(l[0:2]))
      if(d>=today):          #comparing date with the present date 
        kk=1
        d1=d
      if(d<today):
        ss=1                  #breaking loop as soon as we found the latest date 
        break
  
    if(ss==1 and kk==0 and mm==0 and blank==0):          #if show has finished then no date will be there after the present date
      prin=1
      return("The show has finished streaming all its episodes.")
      break
    elif(ss==1):                             #if latest date is found return the latest date
      if(kk==1):
        prin=1
        return("The next episode airs on "+str(d1))
      break
    elif(mm==1 and d2!='' and kk==0):                  #if year is latest return year
      prin=1
      return("The next season begins in "+str(d2))
      break
    
  
  
                #if the date for the last episode is not available return information not available as the show has yet not finished 
  if(ss==1 and mm==0 and blank==1):         
    return("information about next episode is not available")
  elif(prin==0):                       
    return("The next episode airs on "+str(d1))
def registerUser():
	mycursor = mydb.cursor()
	mycursor.execute("use tv_series") 
	print("enter the number of users")                   #enter the number of users you want to enter in the database
	n=int(input())
	for i in range(n):                                   #taking input from every user 
  		x=input("Email address:")
  		tv=input("TV series:")
  		sql="INSERT INTO series_details(Email,series) VALUES(%s,%s)" 
  		val=(x,tv)
  		mycursor.execute(sql,val)
  		mydb.commit()                     


def mailUsers():
	#Taking out emails and series from the database 
	mycursor = mydb.cursor()
	mycursor.execute("use tv_series") 
	mycursor.execute("SELECT Email,series FROM series_details")
	mm={}
	for x in mycursor:
		username=Email                          #this is the mail id from which mail will be send to all the users
		password=Password                              #password of that mail id
		server=smtplib.SMTP('smtp.gmail.com:587')                #creating the server
		server.ehlo()
		server.starttls()
		server.login(username,password)
		sender=Email
		toadd=x[0]                                 #message format to be sent to the user email ids
		msg = MIMEMultipart()                               
		msg['From']=sender
		msg['To']=toadd
		msg['Subject']="tv series details"
		message=''
  	#storing results in dictionary if again same series is entered through the user directly result will be taken from the dictionary
		for k in x[1].split(','):
			xx=k.strip()
			if xx not in mm:
				mm[xx]=result(xx)
			message+="Tv series name: "+str(xx)+"\r\n"+"Status: "+mm[xx]+"\r\n"    
			message+="\r\n"
		msg.attach(MIMEText(message, 'plain'))
		server.send_message(msg)                        #message sent to the mail id of users given information about the tv series
		server.quit()                                    #quiting the server
  
    


def month(a):                 #function to convert into date format
  if(a=="Jul"):
    return 7
  elif(a=="Oct"):
    return 10
  elif(a=="Jan"):
    return 1
  elif(a=="Feb"):
    return 2
  elif(a=="Mar"):
    return 3
  elif(a=="Apr"):
    return 4
  elif(a=="May"):
    return 5
  elif(a=="Jun"):
    return 6
  elif(a=="Aug"):
    return 8
  elif(a=="Sep"):
    return 9
  elif(a=="Nov"):
    return 11
  else:
    return 12

def create_database():

	try:                                          
	  mydb = mysql.connector.connect(         #selecting database if already created
	    host=MysqlHost,
	    user=MysqlUser,
	    password=MysqlPassword,
	    database="tv_series"
	  )


	except:

	    mydb = mysql.connector.connect(           #creating database tv_series if not created
	    host=MysqlHost
	    user=MysqlUser
	    password=MysqlPassword
	    )
	mycursor = mydb.cursor()
	mycursor.execute("CREATE DATABASE tv_series")    
	mycursor.execute("use tv_series")         #creating table to store tv series and emails
	mycursor.execute("CREATE TABLE series_details(Id INT AUTO_INCREMENT PRIMARY KEY,Email VARCHAR(255), series VARCHAR(255))")
	    

	
def del_users():
	mycursor = mydb.cursor()
	mycursor.execute("drop DATABASE tv_series")       
	


try:                                          
  mydb = mysql.connector.connect(         #selecting database if already created
    host="localhost",
    user="root",
    password="Khudha2213",
    
  )


except:
  System.out.println(" error in connecting to mysql")
print("Enter you choice:")
print("1. create database ")
print("2. Register new User")
print("3. Mail current Users")
print("4. Remove all registered users")
i=int(input())
if(i==1):
	create_database()
elif(i==2):
	registerUser()
elif (i==3):
	mailUsers()
elif(i==4):
	del_users()
else:
	print("Invalid Choice")
