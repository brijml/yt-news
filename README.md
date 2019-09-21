# yt-news

#### Analysis project of YouTube data for Indian news channels

##### Introduction

###### This application is based on Flask and uses MongoDB for the database. It makes use of the youtube data api using the `google-python-client` to store the data of channels of interest to the database. This data can be analyzed and visualized for different purposes such as

- Number of views, comments, likes and dislikes.
- Change in number of subscribers over time.
- Number of comments that agree/disagree with the views of the channel (This is tricky!!!)
- etc

##### Building this project

###### This project uses flask and mongodb for the backend.
Requirements
- python
- flask
- mongoengine

###### Instruction
- Install python, pip and Mongodb on your system, once you have done that, run the following command
    $ pip install -r requirements.txt
- Run the server
    $ python server.py
- Test the app by going to `localhost:5000` using a browser