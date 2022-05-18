import altair as alt
import base64
import os
from typing import Dict
import requests
import pandas as pd
import streamlit as st
from io import BytesIO
from PIL import Image
from typing import List, Dict
import sys
import json

from project_metadata import (
    DEPLOYMENT_ID,
    API_URL,
    API_KEY,
    DATAROBOT_KEY,
    IMAGE_RESIZED_HEIGHT,
    IMAGE_RESIZED_WIDTH,
    IMAGE_COLUMN_NAME,
)

# ============================================================================================================
# Function for making predictions - Copy Paste From Deployment in DR
# ============================================================================================================

def make_datarobot_deployment_predictions(data, deployment_id):
    """
    Make predictions on data provided using DataRobot deployment_id provided.
    See docs for details:
         https://app.datarobot.com/docs/predictions/api/dr-predapi.html
 
    Parameters
    ----------
    data : str
        If using CSV as input:
        Feature1,Feature2
        numeric_value,string
 
        Or if using JSON as input:
        [{"Feature1":numeric_value,"Feature2":"string"}]
 
    deployment_id : str
        The ID of the deployment to make predictions with.
 
    Returns
    -------
    Response schema:
        https://app.datarobot.com/docs/predictions/api/dr-predapi.html#response-schema
 
    Raises
    ------
    DataRobotPredictionError if there are issues getting predictions from DataRobot
    """
    # Set HTTP headers. The charset should match the contents of the file.
    headers = {
        # As default, we expect CSV as input data.
        # Should you wish to supply JSON instead,
        # comment out the line below and use the line after that instead:
        # 'Content-Type': 'text/plain; charset=UTF-8',
         'Content-Type': 'application/json; charset=UTF-8',
 
        'Authorization': 'Bearer {}'.format(API_KEY),
        'DataRobot-Key': DATAROBOT_KEY,
    }
 
    url = API_URL.format(deployment_id=deployment_id)
 
    # Prediction Explanations:
    # See the documentation for more information:
    # https://app.datarobot.com/docs/predictions/api/dr-predapi.html#request-pred-explanations
    # Should you wish to include Prediction Explanations or Prediction Warnings in the result,
    # Change the parameters below accordingly, and remove the comment from the params field below:
 
    params = {
        # If explanations are required, uncomment the line below
        # 'maxExplanations': 3,
        # 'thresholdHigh': 0.5,
        # 'thresholdLow': 0.15,
        # Uncomment this for Prediction Warnings, if enabled for your deployment.
        # 'predictionWarningEnabled': 'true',
    }
    # Make API request for predictions
    predictions_response = requests.post(
        url,
        data=data,
        headers=headers,
        # Prediction Explanations:
        # Uncomment this to include explanations in your prediction
        # params=params,
    )
    
    # Return a Python dict following the schema in the documentation
    return predictions_response.json()
 
# ============================================================================================================
# Function for image processing to base64 format
# ============================================================================================================

def image_to_base64(image: Image) -> str:
    """Convert a image to base64 text format for DataRobot
    https://docs.datarobot.com/en/docs/modeling/special-workflows/visual-ai/vai-predictions.html#deep-dive
    Args:
        image (Image): jpeg image
    Returns:
        str: base64 text encoding of image
    """
    img_bytes = BytesIO()
    image.save(img_bytes, "png", quality=90)
    image_base64 = base64.b64encode(img_bytes.getvalue()).decode("utf-8")
    return image_base64

# ============================================================================================================
# Functions for making predictions and visualizing results
# ============================================================================================================

# input is dataframe and output is explanation chart
def render_prediction_barchart(df: pd.DataFrame) -> alt.Chart:
    chrt = alt.Chart(df).mark_bar().encode(
        alt.X('value', title='Predictions'),    
        alt.Y('label', title='Class Labels', sort='-x')
    ).properties(
        width=400,
        height=350,
    )
    return chrt

def prep_score_render_output(data):
    scoring = make_datarobot_deployment_predictions(data,DEPLOYMENT_ID)
    predictions = scoring["data"]
    pred_df = pd.DataFrame(predictions[0]['predictionValues']).sort_values(by='value', ascending=False).reset_index(drop=True)
    chrt =  render_prediction_barchart(pred_df)
    st.write("Based on analyzing 200+ actual hiking and walking trail trips in the Bay Area, our model predicts you would most like",  pred_df.loc[0, 'label'], ' - with a probability of', "{:.0%}".format(pred_df.loc[0, 'value']))
    st.write(chrt)
    return chrt


# ============================================================================================================
# streamlit app and buttons setup
# ============================================================================================================

# Let’s create a header for our web application
image_path = os.path.join(os.path.dirname(__file__), "dr_logo.jpg")
st.image(image_path, width=175)
st.title("Bay Area Hiking Trail Prediction App")

# Let’s create the inputs
col1, col2, col3 = st.columns(3)
Route = col1.selectbox("Enter your Preferred Route Type",["Loop", "Point to Point", "Out And Back"])
Dog = col2.selectbox("Dog Friendly",["Yes", "On leash", "No"])
Kid = col3.selectbox("Kid Friendly",["Yes", "No"])
Review = st.text_area("What kind of hike do you feel like doing this morning?",'I want to do something that has ocean views, some flowers, is easy to do and maybe has some birds - Am I asking for too much?')
# image = None

# ============================================================================================================
# image upload option for users
# ============================================================================================================

uploaded_img = st.file_uploader("Upload an image of a hike you feel like going to")

if uploaded_img is not None:
    img = Image.open(uploaded_img)

    img_resized = img.resize(
        (IMAGE_RESIZED_WIDTH, IMAGE_RESIZED_HEIGHT), Image.ANTIALIAS)

    st.image(img_resized, "Uploaded image")
    st.write("Note: *This image has been resized to match training image dimensions*")

    b64_img = image_to_base64(img_resized)    
    df_input = pd.DataFrame([[Route,Dog,Kid,Review,b64_img]], columns= ['Route Type','Dog Friendly','Kid Friendly','Hike Review','ImagePath'])

else : 
    df_input = pd.DataFrame([[Route,Dog,Kid,Review,None]], columns= ['Route Type','Dog Friendly','Kid Friendly','Hike Review','ImagePath'])

# ============================================================================================================
# Making Predictions Finally
# ============================================================================================================

# predict button formatting
st.title("Let's Make Some Predictions")
 
json_input = df_input.to_json(orient="records")

# predictions
if st.button('Click Here To Generate Personalized Hiking Recommendations For Your Mood!'):  
   
    # make predictions
    pred_df = prep_score_render_output(json_input)



# ============================================================================================================
# Enable users to make recommendations based on sample scenic images
# ============================================================================================================

st.header('Example Trail Images')
col1, col2, col3 = st.columns(3)

with col1:
    img1_path = os.path.join(os.path.dirname(__file__), "images/MountSutro.jpeg")
    st.image(img1_path)
    img1_button = st.button("Recommended Hikes Based On This Image", key='1')
with col2:
    img2_path = os.path.join(os.path.dirname(__file__), "images/LakeChabotTrail.png")
    st.image(img2_path)
    img2_button = st.button("Recommended Hikes Based On This Image", key='2')
with col3:
    img3_path = os.path.join(os.path.dirname(__file__), "images/GrayWhaleCoveTrail.png")
    st.image(img3_path)
    img3_button = st.button("Recommended Hikes Based On This Image", key='3')


if img1_button:
    img = Image.open(img1_path)
    img_resized = img.resize(
        (IMAGE_RESIZED_WIDTH, IMAGE_RESIZED_HEIGHT), Image.ANTIALIAS)
    b64_img = image_to_base64(img_resized)    
    df_input = pd.DataFrame([[None,None,None,None,b64_img]], columns= ['Route Type','Dog Friendly','Kid Friendly','Hike Review','ImagePath'])
    json_input = df_input.to_json(orient="records")
    prep_score_render_output(json_input)
elif img2_button:
    img = Image.open(img2_path)
    img_resized = img.resize(
        (IMAGE_RESIZED_WIDTH, IMAGE_RESIZED_HEIGHT), Image.ANTIALIAS)
    b64_img = image_to_base64(img_resized)    
    df_input = pd.DataFrame([[None,None,None,None,b64_img]], columns= ['Route Type','Dog Friendly','Kid Friendly','Hike Review','ImagePath'])
    json_input = df_input.to_json(orient="records")
    prep_score_render_output(json_input)
elif img3_button:
    img = Image.open(img3_path)
    img_resized = img.resize(
        (IMAGE_RESIZED_WIDTH, IMAGE_RESIZED_HEIGHT), Image.ANTIALIAS)
    b64_img = image_to_base64(img_resized)    
    df_input = pd.DataFrame([[None,None,None,None,b64_img]], columns= ['Route Type','Dog Friendly','Kid Friendly','Hike Review','ImagePath'])
    json_input = df_input.to_json(orient="records")
    prep_score_render_output(json_input)
    
