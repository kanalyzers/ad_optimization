# Objective
Train a machine learning model to predict whether a particular user will click on an ad or not based on training data from the Avazu advertising platform provided by Criteo Labs 


# Background
Determining whether advertisers will click on an ad on a mobile platform is a question that encapsulates increasing market value as mobile advertising revenue explodes. In FY 2017 mobile ad revenue grew to $49.9B (+36% YoY) in 2017. This increase in the mobile ad market means mobile is increasingly relevant to overall marketing ROI and more and more data is available to train machine learning models. 

ML has the potential to impact mobile marketers in several important ways. Namely, ML can play a role in campaign targeting optimization. Rather than require advertisers manually optimized bids/budgets for their campaigns, ML can automate this process, saving time.  This technology also has the ability to uncover deep correlations between particular creatives/targeting elements of a campaign and user’s propensity to click on ads that may have escaped manual optimization methods.

Furthermore, as mobile advertising revenues increase, so are the attempts to fraudulently click  mobile ads. Mobile app marketers were exposed to 30% more fraud in Q1 2018, costing them and estimated $700-800 million worldwide. ML could play a role in helping marketers avoid ad fraud by classifying ad impressions as fraud or not and help prevent ads from being clicked on by fraudulent users. ML, however, may only be piece in the overall solution as fraudsters are constantly changing their methods and ML models may not be able to effectively classify fraud in this ever changing landscape. 

Enter our dataset, which is based on eleven days worth of mobile data from the Avazu ad platform. We plan to create a classification model that will determine whether a user will click on an ad or not,  providing a model marketers could use to determine whether an ad with a particular bid and targeting data will be effective or not. An ML regression model could also be employed to help determine a particular CTR for an ad and targeting criteria, which could help marketers identify high/low performing ads before they ever serve.

--------------------------------------

# Setup / Dependencies
* Install the latest versions of Python 3
* Install a text editor or IDE (optional)
* Install the Google Cloud SDK (optional)
* Install the Google Cloud CLI (optional)


# Google Compute Engine 
## Spin up a server from the VM instance
`
Strongly recommended to use the Compute Engine browser tool to ```ssh``` into the VM. You can access the VM via two methods:

1) From gcloud command-line tool with your terminal
```
 gcloud compute --project "xx" ssh --zone "xx" "xx"
```
2) From the G-Suite here: https://cloud.google.com/compute/
 
### To shut down the VM instance:
```
 gcloud compute instances stop example-instance-1 example-instance-2
```
## Jupyter Notebook from VM instance

-  Spin up Jupyter Notebook from VM (ports only open from 5000-5010)

```
jupyter notebook —ip=0.0.0.0 --port=5000 --no-browser &
```
-  get link from Jupyter output 
-  copy url with token into browser 
-  copy static IP address between the parentheses


## ML Tasks 
_ preprocess data
_ iteratively train and evaluate models

# Tools used
* Google Cloud Compute Engine
* Visual Studio Code with SFTP OR browser Compute Engine ```ssh```
* Jupyter Notebook
* Github for Version control
* Python3
* pandas
* flask
* Tensorflow, scikit learn, etc. 

# Data

## Data fields
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
