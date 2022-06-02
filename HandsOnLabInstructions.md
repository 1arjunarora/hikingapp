# Instructions

1. **Download your multimodal dataset** (images, text, tabular) from [box](https://datarobot.box.com/shared/static/bo4qqislafk6hmfuann84jbzcfnor2kk.zip)
2. **Upload to datarobot** via drag and drop (or add through [AI catalog](https://docs.datarobot.com/en/docs/data/import-data/catalog.html) and create a project)
      - How many hikes do we have?
      - What do the hike images and text reviews look like? How much missing data do we have?
3. **Prepare, test and validate** various cutting edge deep learning and NLP models through [automated ML]( https://docs.datarobot.com/en/docs/modeling/build-models/build-basic/model-data.html)
      - What partitioning approach did you try?
      - Did you use image augmentation to create more accurate models? What settings?
      - What modeling mode did you try - Autopilot, Quick or Comprehensive?

4. **Evaluate and explain models** through [automated insights](https://docs.datarobot.com/en/docs/modeling/special-workflows/visual-ai/vai-insights.html) - Visual AI provides several tools to help visually assess, understand, and evaluate model performance
      - Evaluate - Golden Gate Park Loop is most frequently confused with which hike?
      - Understand - What feature are most important in making model predictions?
      - Understand - Text Mining - Does Sawyer Camp Trail have a polo field or Golden Gate Park Loop?
      - Understand - Activation Maps - What part of the image influenced model predictions - Oceans Vs Trees? (Compare Gray Whale Cove Vs. Mount Sutro)
      - Understand - Image Embeddings - How does the model group different trail images? Does it follow a trend?
5. **Deploy a Datarobot Model** - From the Leaderboard, select the model to use for generating predictions and click Predict > Deploy. The [Deploy model page](https://docs.datarobot.com/en/docs/mlops/deployment/deploy-methods/deploy-model.html) lets you create a new deployment for the selected model
6. **Setup Deployment Integration** - DataRobot provides sample Python code containing the necessary commands and identifiers needed to submit a CSV or JSON file for scoring. To use the [Prediction API Scripting Code](https://docs.datarobot.com/en/docs/mlops/deployment/deploy-pred/code-py.html), open the deployment you want to make predictions through and click Predictions > Prediction API. Follow the sample provided and make the necessary changes when you want to integrate the model, via API, into your production application.
7. **Assemble a code-first app to generate model predictions** from sample scenic images and text descriptions. Streamlit app code examples can be edited easily for the different use cases - see file "Hiking_app.py" for example setup!

Enjoy!!
