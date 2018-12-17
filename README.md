# Ease Entertainment
## Summary
###### Functionality 1
The given project will save the community from all the spoilers of their favourite tv series hovering around . The main aim of the project is to send an email to the user that contains the information about the Air Date of episode of the TV series a user likes ( air date = Date on which the episode will be broadcasted). 
It enables user to register for themself.
List of favourite TV Series is stored in the MySQL DataBase and mailed to all the registered user on their registered email address on demand.


###### Tools and Technologies
Language: Python
Concept: Web Scraping
Scraped Site: https://www.imdb.com/


## Getting Started

### Dependencies

#### 1. Make sure these libraries are installed in your system
##### Libraries:
smtplib
urllib
bs4 ( BeautifulSoup)
datetime
Mysql.connector
##### Installation
Installing dependencies:
sudo apt-get install python3-mysql.connector
sudo apt-get install python3-bs4

###### Enter your Credentials at config.py code.
EmailAddress="Your_Email_Address"
Enter your email address through which you want to email all the users
Password="Your_Password"
Enter Password of your email address

Enter host name, username and password of your mysql
Mysql
MysqlHost="Your_Host_Name"
MysqlUser="Your_User_Name"
MysqlPassword="Your_password"
Example:
MysqlHost=”local host”
MysqlUser="User"
MysqlPassword="My password"
Your Gmail should allow third party apps(Less secure apps) to send mails.

Usage
Run main1.py in terminal and enter your choice of functions as per the instructions
For TV Series format to enter data:
Enter user email address
example: kungwanikomal8@gmail.com
Enter tv series information requirement separating with comma
example: friends,sacred games,The passage


## Screenshots
### TV Series


##### Interface

<p align="center">
    <img src="https://github.com/komalkungwani/TV_series_update_system/blob/master/images/1.png" width="500" title="hover text">
  </p>

##### create database tv_series and table series_detail
 <p align="center">
  <img src="https://github.com/komalkungwani/TV_series_update_system/blob/master/images/12.png" width="500" title="hover text">
</p>



##### register user
 <p align="center">
  <img src="https://github.com/komalkungwani/TV_series_update_system/blob/master/images/13.png" width="500" title="hover text">
</p>
 


##### email send with 3rd option

<p align="center">
  <img src="https://github.com/komalkungwani/TV_series_update_system/blob/master/images/14.png" width="500" title="hover text">
</p>
 
 
 
###### received emails 
 <p align="center">
  <img src="https://github.com/komalkungwani/TV_series_update_system/blob/master/images/15.png" width="500" title="hover text">
</p>

##### received emails 
 <p align="center">
  <img src="https://github.com/komalkungwani/TV_series_update_system/blob/master/images/16.png" width="500" title="hover text">
</p>

##### received emails 
 <p align="center">
  <img src="https://github.com/komalkungwani/TV_series_update_system/blob/master/images/17.png" width="500" title="hover text">
</p>
