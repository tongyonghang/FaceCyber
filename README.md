# FaceCyber (Cyber-aggression/Cyber-bullying/Aggressive word Detection From Social Media - FB )
My Final Year Project in Universiti Sains Malaysia (USM), Penang, Malaysia, which receive gold reward in USM CS Pixel 2021

Noted that this project will suitable for running in local machine, please be careful when testing in production.

Thanks to **stack overflow, github, programming blog** and many more for helping me to solve any difficulty during my implementation, without all these i will not make it on time.

Please do not hesitate email me through tongyonghang04@gmail.com if have any question regard this project, I will try to help as much as I can like how others helped me.

1.web_app/FaceCyber/accounts/model/ - training dataset and 6 machine learning models (Can be replaced with own dataset and models)

2.web_app - code for web application

3.web_ext - code for Chrome web extension (only work for Chrome)

4.chromedriver.exe - Used to scrape Facebook elements
		                 Have to insert in Python\Python39 or etc\Scripts in local machine in order to make it work 
                     
# Software required:
1.MongoDB Compass Community

2.Visual Studio Code

3.Jupyter Notebook (Not require if have own models)

# Programming Languages:
1.Python

2.HTML/CSS/JavaScript

# Library required:
***Extra library >>> python -m pip install --user virtualenv (if want setup virtual environment)***

1.pip install pandas 

2.pip install selenium

3.pip install django

4.pip install djongo

5.pip install sklearn

# Implementation Instructions (In Individual Local Machine)
# Web app
>> Install required library either in local machine or virtual environment

>> Open terminal in VS Code and follow:

>> Make sure it locates to web_app

>> Run command -> source virtual/Scripts/activate (To open virtual environment,ignore if run in local machine)

>> Run command -> cd FaceCyber

>> Run command -> python manage.py runserver, wait until server is running

>> Copy http://127.0.0.1:8000/ and open with Chrome browser (recommended)

>> After server is running, can try register and login to Web application by using username

# Web ext

>> Open Chrome browser and direct to chrome://extensions/

>> click load unpacked and select web_ext folder

>> FaceCyber icon will appear and click slider to allow FaceCyber web extension to be used in chrome

>> Click FaceCyber web extension icon to open - login with same account

***Click ctrl+c to exit server***

***run command -> deactivate to exit virtual environment***

***Please make sure chromedriver.exe is placed in required location***

***run command -> python manage.py migrate to connect to MongoDB database for the first time before run server***

# Database information:
>> Open MongoDB Compass Community

>> Click connect

>> Find demodatabase

>> Find accounts_user_post (To store post and comment information)

>> Find accounts_user_register (To store FaceCyber account information)

>> You can import the dataset into accounts_user_post & accounts_user_register from database folder to reuse information

# Usage in Web application and web extension
**Web application:**
>> Can view self and friend visualization

>> Can register & login

>> Can click profile section to update information

**Web extension**
>> Open facebook, new chrome browser will appear and run automatically.(require web extension login and insert correct facebook information - can found in web application profile section)

>> Please do not close that browser, it will close after done executing

>> will label cyber-aggression words in post and comment typing section with special border. (No need require web extension login)


