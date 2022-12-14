# WORKOUT LOGGER

![Freelancer](https://img.shields.io/badge/Freelancer-29B2FE?style=for-the-badge&logo=Freelancer&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
\
![50%](https://progress-bar.dev/100)

## Description

This is a python command line application in which it will prompt you what exercises did you do today, and after you've written them in a plain english sentence, the application will read it and decifer what exercise did you do for how long and how many calories did it used.  For this application to work we need to pass in some parameters as environment variables

### Environment variables

- NUTRITION_API_KEY
    - For this app to work we will need to create a developer account in the [nutritionix API](http://developer.nutritionix.com) and when it's done we will get the api key
- NUTRITION_API_APPLICATION_ID
    - Once we've created the account we will get the app id
- NUTRITION_API_END_POINT
    - The api end point for the nutritionix api and it has to be https://trackapi.nutritionix.com/v2/natural
- NUTRITION_GENDER
    - The gender of the person who will be using the app
- NUTRITION_WEIGHT
    - The weight of the person in kg using the app
- NUTRITION_HEIGHT_CM
    - The height of the person in cm 
- NUTRITION_AGE
    - The age of the person
- SHEETY_API_END_POINT
    - You will need to create a new [sheety api](https://sheety.co/) by signing in with your google account, you must grant access to read and write to your spreadsheets in order for this app to work.  Once you are done creating the account you will need to create a project by giving it a link to an existing spreadsheet in your google drive and only then you will have your end point
- SHEETY_API_BEARER_TOKEN
    - Inside your poject there is an **Authentication** tab, there you select the Bearer(Token) option and give your own Token 

### Installation

Make sure you have the latest version of python installed on your machine:
'''
python --version
'''
if it doesn't work, you can use
'''
python3 --version
'''
if you don't have python installed or your version is less than 3.10.5 you will need to download and install [Python](https://www.python.org/downloads/)

Once you've verified you got the latest version of Python installed then proceed to clone this repository, and inside the application directory run the following command:
'''
python3 -m venv venv
'''

To install all required modules for the app to work, run
'''
pip install -r requirements.txt
'''

And finally on the application root folder, create your .env file with the environment variables described earlier

To run the application, open your terminal and run
'''
python3 main.py
'''

Follow the instructions and go to your google drive and look the spreadsheet being updated with the info you provided

[<img src="./images/icons8-linkedin-2-48.png" alt="LinkedIn" width="25" />](https://www.linkedin.com/in/andres-court-benitez-11ab6613b)
[<img src="./images/icons8-twitter-48.png" alt="Twitter" width="25" />](https://twitter.com/alcb1310)