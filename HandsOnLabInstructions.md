# Instructions

1. **Download your multimodal dataset** (images, text, tabular) from [box](https://datarobot.box.com/shared/static/bo4qqislafk6hmfuann84jbzcfnor2kk.zip)
2. **Upload to datarobot** via drag and drop
3. **Prepare, test and validate** various cutting edge deep learning and NLP models through [automated ML]( https://docs.datarobot.com/en/docs/modeling/build-models/build-basic/model-data.html)
4. **Evaluate and explain models** through [automated insights](https://docs.datarobot.com/en/docs/modeling/special-workflows/visual-ai/vai-insights.html) - Visual AI provides several tools to help visually assess, understand, and evaluate model performance
5. **Deploy a Datarobot Model** - From the Leaderboard, select the model to use for generating predictions and click Predict > Deploy. The [Deploy model page](https://docs.datarobot.com/en/docs/mlops/deployment/deploy-methods/deploy-model.html) lets you create a new deployment for the selected model
6. **Setup Deployment Integration** - DataRobot provides sample Python code containing the necessary commands and identifiers needed to submit a CSV or JSON file for scoring. To use the [Prediction API Scripting Code](https://docs.datarobot.com/en/docs/mlops/deployment/deploy-pred/code-py.html), open the deployment you want to make predictions through and click Predictions > Prediction API. Follow the sample provided and make the necessary changes when you want to integrate the model, via API, into your production application.
7. **Assemble a code-first app to generate model predictions** from sample scenic images and text descriptions. Streamlit app code examples can be edited easily for the different use cases - see file "Hiking_app.py" for example setup!

Enjoy!!
