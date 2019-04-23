#!/usr/bin/env python
# coding: utf-8

# In[108]:


import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split


# In[125]:



raw_df = pd.read_csv('choice_features.csv')
raw_df = raw_df.drop('Unnamed: 0', axis = 1) 

raw_df.head()


# In[105]:



X = raw_df.drop('click',axis=1)
y = raw_df['click']


# In[109]:


X_train, X_test, y_train, y_test = train_test_split(X, y)


# In[110]:


from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

# Fit only to the training data
scaler.fit(X_train)

StandardScaler(copy=True, with_mean=True, with_std=True)

# Now apply the transformations to the data:
X_train = scaler.transform(X_train)
X_test = scaler.transform(X_test)


# In[111]:


from sklearn.neural_network import MLPClassifier


# In[112]:


mlp = MLPClassifier(hidden_layer_sizes=(13,13,13),max_iter=500)


# In[113]:


mlp.fit(X_train,y_train)


# In[114]:


MLPClassifier(activation='relu', alpha=0.0001, batch_size='auto', beta_1=0.9,
       beta_2=0.999, early_stopping=False, epsilon=1e-08,
       hidden_layer_sizes=(13, 13, 13), learning_rate='constant',
       learning_rate_init=0.001, max_iter=500, momentum=0.9,
       nesterovs_momentum=True, power_t=0.5, random_state=None,
       shuffle=True, solver='adam', tol=0.0001, validation_fraction=0.1,
       verbose=False, warm_start=False)


# In[115]:


predictions = mlp.predict(X_test)


# In[116]:


from sklearn.metrics import classification_report,confusion_matrix


# In[117]:


print(confusion_matrix(y_test,predictions))


# In[118]:


print(classification_report(y_test,predictions))


# In[119]:


# coefs_ is a list of weight matrices, where weight matrix at index i represents the weights between layer i and layer i+1.
len(mlp.coefs_)


# In[120]:


len(mlp.coefs_[0])


# In[122]:


#intercepts_ is a list of bias vectors, where the vector at index i represents the bias values added to layer i+1.
len(mlp.intercepts_[0])


# In[123]:


from sklearn import joblib
joblib.dump(model, ‘model.joblib’)


# In[ ]:




