# MORINGA PITCHH PROJECT

an application that allows users to use that one minute wisely. The users will submit their one minute pitches and other users will vote on them and leave comments to give their feedback on them.

## Author

[Kiprotich Dominic Korir](https://github.com/kiprotichdominic)

# Description

This is an application that allows users to sign in or sign up and post one minute pitches.It also allows the to upvote and downvote on different pitches.

## User Story

- Comment on the different pitches posted py other uses.
- See the pitches posted by other uses.
- Vote on s pitch they have viwed by giving it a upvote or a downvote.
- Register to be allowed to log in to the application
- View pitches from the different categories.
- Submit a pitch to a specific category of their choice.

## BDD

| Behaviour             |                Input                |                                                                       Output |
| :-------------------- | :---------------------------------: | ---------------------------------------------------------------------------: |
| Load the page         |          **On page load**           |                               Get all posts, Select between signup and login |
| Select SignUp         | **Email**,**Username**,**Password** |                                                            Redirect to login |
| Select Login          |    **Username** and **password**    | Redirect to page with app pitches based on categories and commenting section |
| Select comment button |             **Comment**             |                                             Form that you input your comment |
| Click on submit       |                                     |       Redirect to all comments tamplate with your comment and other comments |

## Development Installation

To get the code..

1. Cloning the repository:

```bash
https://github.com/kiprotichdominic/Moringa-Project-Pitch
```

2. Move to the folder and install requirements

```bash
cd pitch-world
pip install -r requirements.txt
```

3. Exporting Configurations

```bash
export SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://{User Name}:{password}@localhost/{database name}
```

4. Running the application

```bash
python3.6 manage.py server
```

5. Testing the application

```bash
python3.6 manage.py test
```

Open the application on your browser `127.0.0.1:5000`.

## Technology used

- [Python3.6](https://www.python.org/)
- [Flask](http://flask.pocoo.org/)
- [Heroku](https://heroku.com)

## Contact Information

If you have any question or contributions, please email me at [kiprotichkorir36@gmail.com]

## Live Link To Project

- [Moringa Pitch Project](https://moringapitchproject.herokuapp.com/home)

## License

- _MIT License:_
- Copyright (c) 2019 ** Kiprotich Dominic Korir**
