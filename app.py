#!/usr/bin/env python
# coding: utf-8

# In[5]:


pip install streamlit


# In[6]:


import streamlit as st
import numpy as np
import pickle
import warnings

warnings.filterwarnings("ignore")


# In[7]:


strength_model = pickle.load(open('final_model.pkl','rb'))


# In[9]:


st.title("Strenth checker")
st.header("Check your construction's strength!!")
st.subheader("Demo application ")


# In[11]:


cement= st.text_input("Enter cement")
slag = st.text_input("Enter slag")
ash = st.text_input("Enter ash")
water = st.text_input("Enter water")
superplastic = st.text_input("Enter superplastic")
courseagg= st.text_input("Enter courseagg")
fineagg= st.text_input("Enter fineagg")
age=st.text_input("Enter age")        
    


# In[12]:


def prediction(cement,slag,ash,water,superplastic,courseagg,fineagg,age):
    input_data = np.asarray([cement,slag,ash,water,superplastic,courseagg,fineagg,age])
    input_data = input_data.reshape(1,-1)
    prediction = strength_model.predict(input_data)
    return prediction[0]


# In[14]:


strength=""
if st.button("Predict"):
    strength=prediction(cement,slag,ash,water,superplastic,courseagg,fineagg,age)
    print("Strenth of your construction will be {} years with {} of accuracy".format(strength,r2score(y_test,y_pred)))
       


# In[ ]:




