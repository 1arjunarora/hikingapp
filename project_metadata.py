import streamlit as st  # willl be redundant in main program

DEPLOYMENT_ID = '6272eac547441ad43bfed4b0'
API_URL = 'https://cfds-ccm-prod.orm.datarobot.com/predApi/v1.0/deployments/{deployment_id}/predictions'    # noqa
API_KEY = 'NjI1NzkxY2ViNmE0NzJjOGVkZjhmNGNkOjczY3BhVm8vQmR3OUgxR3BCa3FleHdRMGl4dys0T1JNdk1KMGswTzRrK1U9'
DATAROBOT_KEY = '544ec55f-61bf-f6ee-0caf-15c7f919a45d'

# Resized Image Proportions to match training. In the future these may change
IMAGE_RESIZED_HEIGHT = 224
IMAGE_RESIZED_WIDTH = 224

IMAGE_COLUMN_NAME = "ImagePath"
