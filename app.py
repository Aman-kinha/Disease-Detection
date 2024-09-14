from flask import *
import os
import google.generativeai as genai
import speech_recognition as sr
import pyttsx3
import requests
from gtts import *
import pygame
from voice import *
# app = Flask(__name__)
app = Flask(__name__, static_folder='static')

# Set the API key as an environment variable
api_key = "AIzaSyCFptHf1cqnx-NVrmVqlxqLxQ-yC7mxbzQ"

# Configure the API key
genai.configure(api_key=api_key)

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

@app.route("/")
def index():          #Render the HTML Template from template folder 
    return render_template("index.html")    

# To add css to linked html 

@app.route("/submit", methods=["POST"]) # Submit the response    
def submit():                              # To get input from the webpage and sed to gemni 
    g = request.form.get("tk")
    chat_session = model.start_chat(
      history=[
      ]
    )
    message = f"There are some symptoms of a disease below please tell me which disease it is in one word {g}"
    response = chat_session.send_message(message)
    a=response.text
    cr=cure(a)
    return render_template("index.html", response=a,cure_response=cr)
def cure(a):
    print(a)
    chat_session = model.start_chat(
      history=[
      ]
    )
    chat_session = model.start_chat(
      history=[
      ]
    )
    message = f"There are some symptoms of a disease below please provide the steps to be avoided to handel te disease in not more than 2 sentences {a}"
    response = chat_session.send_message(message)
    cr=response.text
    return cr


@app.route("/play", methods=["GET"])  # New route for the play button
def plays():
    print("Play  button clicked")   
    # play()
    command=play()  # Call the play function here
    print(command)
    chat_session = model.start_chat(
      history=[
      ]
    )
    message = f"There are some symptoms of a disease below please tell me which disease it is in one word {command}"
    response = chat_session.send_message(message)
    rs=response.text
    crsd=core(rs)
    return render_template("index.html",command = command,response=rs,cure_response=crsd)  # Return a success message

def core(rs):
    print(rs)
    chat_session = model.start_chat(
      history=[
      ]
    )
    message = f"There are some symptoms of a disease below please provide the steps to be avoided to handel te disease in not more than 2 sentences {rs}"
    response = chat_session.send_message(message)
    crs=response.text
    return crs

if __name__ == "__main__":     # To run the app in debug Mode Flask Function 
    app.run(debug=True)

   
    