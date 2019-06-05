# Objective
Train a machine learning model to predict whether a particular user will click on an ad or not based on training data from the Avazu advertising platform provided by Criteo Labs 

# Website
 * https://kanalyzers.appspot.com/
 * note: when uploading a CSV, the CSV must have 22 columns. Additional functionality coming soon.
 * It is recommended to use the `ad_optimization/flask_site/uploads/demofeatures1.csv` to understand how the MVP work. The CSV 'demofeatures1.csv' within this repo is the best CSV to use to understand the full capacity and utility of our web tool in it's current state of development. 

# Background
Determining whether advertisers will click on an ad on a mobile platform is a question that encapsulates increasing market value as mobile advertising revenue explodes. In FY 2017 mobile ad revenue grew to $49.9B (+36% YoY) in 2017. This increase in the mobile ad market means mobile is increasingly relevant to overall marketing ROI and more and more data is available to train machine learning models. 

ML has the potential to impact mobile marketers in several important ways. Namely, ML can play a role in campaign targeting optimization. Rather than require advertisers manually optimized bids/budgets for their campaigns, ML can automate this process, saving time.  This technology also has the ability to uncover deep correlations between particular creatives/targeting elements of a campaign and user’s propensity to click on ads that may have escaped manual optimization methods.

Furthermore, as mobile advertising revenues increase, so are the attempts to fraudulently click  mobile ads. Mobile app marketers were exposed to 30% more fraud in Q1 2018, costing them and estimated $700-800 million worldwide. ML could play a role in helping marketers avoid ad fraud by classifying ad impressions as fraud or not and help prevent ads from being clicked on by fraudulent users. ML, however, may only be piece in the overall solution as fraudsters are constantly changing their methods and ML models may not be able to effectively classify fraud in this ever changing landscape. 

Enter our dataset, which is based on eleven days worth of mobile data from the Avazu ad platform. We plan to create a classification model that will determine whether a user will click on an ad or not,  providing a model marketers could use to determine whether an ad with a particular bid and targeting data will be effective or not. An ML regression model could also be employed to help determine a particular CTR for an ad and targeting criteria, which could help marketers identify high/low performing ads before they ever serve.

--------------------------------------

# Setup / Dependencies
* Install the latest versions of Python 3
* Install a text editor or IDE (optional)
* Install the Google Cloud SDK

# configure development environment
https://cloud.google.com/python/setup
 - pip install --upgrade virtualenv
 - cd your-project
 - virtualenv --python python3 env
 - source env/bin/activate
 - pip install -r requirements.txt
 - when you're done developing run: ``` deactivate```

# Back End Technology 
 - Google: Cloud Compute Engine, Cloud Storage, ML Engine API https://googleapis.github.io/google-cloud-python/latest/
 - Flask
 
# Google Compute Engine 
## How to spin up a server from the VM instance and use Jupyter Notebook from the VM
We used Compute Engine to store our dataset (6+GB)
`
Strongly recommended to use the Compute Engine browser tool to ```ssh``` into the VM. You can access the VM via two methods:

1) From gcloud command-line tool with your terminal
```
 gcloud compute --project "xx" ssh --zone "xx" "xx"
```
2) From the G-Suite console here: https://cloud.google.com/compute/
 
### To shut down the VM instance:
```
 gcloud compute instances stop example-instance-1 example-instance-2
```
## Jupyter Notebook from VM Instance

-  Spin up Jupyter Notebook from VM
```
jupyter notebook —ip=0.0.0.0 --port=8888 --no-browser &
```
## Jupyter Notebook Auth Token:
-  get link from Jupyter output 
-  copy url with token into browser 
-  copy static IP address between the parentheses


## Machine Learning / Data 
- Preprocess and feature engineer data with Pandas, Numpy, scikit learn and 
- iteratively train and evaluate predictive classification models:
 - SGDClassifier
 - Random Forest
 - Tensorfolow: Multi-layer Perceptron Neural Net

# Tools used
* Visual Studio Code with SFTP OR browser Compute Engine ```ssh```
* Jupyter Notebook
* Github
* Python3
* pandas
* Flask
* Tensorflow, scikit learn, 

# Data

## Default/Original Features 
 - id: ad identifier
 - click: 0/1 for non-click/click
 - hour: format is YYMMDDHH, so 14091123 means 23:00 on Sept. 11, 2014 UTC.
 - C1 -- anonymized categorical variable
 - banner_pos
 - site_id
 - site_domain
 - site_category
 - app_id
 - app_domain
 - app_category
 - device_id
 - device_ip
 - device_model
 - device_type
 - device_conn_type
 - C14-C21 -- anonymized categorical variables

 Preprocessed / Feature Engineered Data
 - One hot encoded: 
    * device_conn_type
    * device_type
 - Features converted to numeric data types
 - Removed C1, C14, C17-21
 - Feature engineered:
    * Date
    * Time
    * User counts
    

    
