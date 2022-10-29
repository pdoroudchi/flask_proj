# Welcome to my Flask Deployment Project!

In this project I use Flask to deploy a web application that predicts employee salary given years of experience.

## Model

- model.py trains and saves the model to the disk
- model.pkb is the pickle model to be used by the web app

## App

- app.py contains the flask code and manages the API

## Running the App

- Download Git repo ZIP file
- Open the computer terminal
- Change directory to location of ZIP file
- If running for first time, run python model.py to create pickle model
- Run python app.py and copy/paste given HTTP address into web browser
