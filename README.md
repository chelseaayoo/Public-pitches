## Public-pitches
## By ONYANGO ANIPHER CHELSEA AYOO ,{8/11/2021}
## Description
Public-pitches is a web application that enables the users to submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.

The pitches are organized by category and users can view their pitches and comments made by other users.

## Application Behaviour
A user should be able to:

See the pitches other people have posted.
Vote on the pitch they liked and give it a downvote or upvote.
Sign in for them to leave a comment
Receive a welcoming email once they sign up.
View the pitches I have created in their profile page.
Comment on the different pitches and leave feedback.
Submit a pitch in any category.
View the different categories.

## SetUp / Installation Requirements

Prerequisites
python3.6
pip3
pipenv
Git and Github
Cloning
In your terminal:

  $ git clone https://github.com/chelseaayoo/Public-pitches
  $ cd PUBLIC-PITCHES

Running the Application
Install the requirements:

   $ pipenv install
Start your virtual environmrnt;

  $ pipenv shell 
Export your configuraions

  $ export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}

  $ export SECRET_KEY='Your secret key'

  $ export MAIL_USERNAME='Your email username'

  $ export MAIL_PASSWORD='Your password'
To run the application, in your terminal:

  $ python3.8 manage.py server
Open your browser and navigate to http://localhost:5000 to view the web app

## Technologies and Languages Used
Python version 3.6
Flask
HTML 5
Bootstrap
## License
MIT License Copyright (c) [2021] [ONYANGO ANIPHER CHELSEA AYOO]

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE. Copyright (c) {2021} {ONYANGO ANIPHER CHELSEA AYOO}