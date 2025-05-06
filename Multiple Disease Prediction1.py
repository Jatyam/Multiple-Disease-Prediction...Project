# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 22:42:16 2025

@author: sohan
"""

import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu


# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")

    

# getting the working directory of the main.py
working_dir = os.path.dirname(os.path.abspath(__file__))


# loading the saved models

diabetes_model = pickle.load(open('Saved Models/diabetes_model.sav','rb'))

heart_disease_model = pickle.load(open('Saved Models/heart_disease_model.sav','rb'))

parkinsons_model = pickle.load(open('Saved Models/parkinsons_model.sav','rb'))

lung_cancer_model = pickle.load(open('Saved Models/lung_cancer_model.sav','rb'))


# sidebar for navigation

with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System', 
                           
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            'Parkinsons Prediction',
                            'Lung Cancer Prediction'],
                           menu_icon='hospital-fill',
                           icons = ['activity','heart','person','lungs'],
                           default_index = 0)
    
    
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction Using ML')
    

    # Custom Theme
    ms = st.session_state
    if "themes" not in ms: 
      ms.themes = {"current_theme": "light",
                        "refreshed": True,
                        
                        "light": {"theme.base": "dark",
                                  "theme.backgroundColor": "black",
                                  "theme.primaryColor": "#c98bdb",
                                  "theme.secondaryBackgroundColor": "#5591f5",
                                  "theme.textColor": "white",
                                  "theme.textColor": "white",
                                  "button_face": "🌜"},

                        "dark":  {"theme.base": "light",
                                  "theme.backgroundColor": "white",
                                  "theme.primaryColor": "#5591f5",
                                  "theme.secondaryBackgroundColor": "#82E1D7",
                                  "theme.textColor": "#0a1464",
                                  "button_face": "🌞"},
                        }
      

    def ChangeTheme():
      previous_theme = ms.themes["current_theme"]
      tdict = ms.themes["light"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]
      for vkey, vval in tdict.items(): 
        if vkey.startswith("theme"): st._config.set_option(vkey, vval)

      ms.themes["refreshed"] = False
      if previous_theme == "dark": ms.themes["current_theme"] = "light"
      elif previous_theme == "light": ms.themes["current_theme"] = "dark"


    btn_face = ms.themes["light"]["button_face"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]["button_face"]
    st.button(btn_face, on_click=ChangeTheme)

    if ms.themes["refreshed"] == False:
      ms.themes["refreshed"] = True
      st.rerun()
    
    # User Input Section

    user_input = st.text_input("Name of the patient")

    # Button with no effect on input or result
    if st.button("Enter"):
       # st.balloons()  # This will show an animation but won't affect data

    # Displaying User Input
        st.write("Submit")
        st.write(f"You entered: {user_input}")

    
    
    #getting the input data from user
    #columns for input fields
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
         
    with col2:
        Glucose = st.text_input('Glucose Level')
         
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
         
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
         
    with col2:
        Insulin = st.text_input('Insulin Level')
         
    with col3:
        BMI = st.text_input('BMI value')
        
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')    
             
    with col2:
        Age = st.text_input('Age of the Person')   


    

    # Code for Prediction
    diabetes_diagnosis = ''
     
    # creating a button for Prediction
     
    if st.button('Diabetes Test Result'):
        
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin,
                      BMI, DiabetesPedigreeFunction, Age]

        user_input = [float(x) for x in user_input]
        
        diabetes_prediction = diabetes_model.predict([user_input])
         
        if (diabetes_prediction[0]) == 1:
            diabetes_diagnosis == 'The Person is Diabetic'
            
        else:
            diabetes_diagnosis = 'The Person is not Diabetic'
            
    st.success(diabetes_diagnosis)
     
                   
  
# Heart Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    #page title
    st.title('Heart Disease Prediction Using ML')    
    

    
    ms = st.session_state
    if "themes" not in ms: 
      ms.themes = {"current_theme": "light",
                        "refreshed": True,
                        
                        "light": {"theme.base": "dark",
                                  "theme.backgroundColor": "black",
                                  "theme.primaryColor": "#c98bdb",
                                  "theme.secondaryBackgroundColor": "#5591f5",
                                  "theme.textColor": "white",
                                  "theme.textColor": "white",
                                  "button_face": "🌜"},

                        "dark":  {"theme.base": "light",
                                  "theme.backgroundColor": "white",
                                  "theme.primaryColor": "#5591f5",
                                  "theme.secondaryBackgroundColor": "#82E1D7",
                                  "theme.textColor": "#0a1464",
                                  "button_face": "🌞"},
                        }
      

    def ChangeTheme():
      previous_theme = ms.themes["current_theme"]
      tdict = ms.themes["light"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]
      for vkey, vval in tdict.items(): 
        if vkey.startswith("theme"): st._config.set_option(vkey, vval)

      ms.themes["refreshed"] = False
      if previous_theme == "dark": ms.themes["current_theme"] = "light"
      elif previous_theme == "light": ms.themes["current_theme"] = "dark"


    btn_face = ms.themes["light"]["button_face"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]["button_face"]
    st.button(btn_face, on_click=ChangeTheme)

    if ms.themes["refreshed"] == False:
      ms.themes["refreshed"] = True
      st.rerun()
      
      
    # User Input Section

    user_input = st.text_input("Name of the patient")

    # Button with no effect on input or result
    if st.button("Enter"):
       # st.balloons()  # This will show an animation but won't affect data

    # Displaying User Input
        st.write("Submit")
        st.write(f"You entered: {user_input}")

    
    
    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.text_input('Age')

    with col2:
        sex = st.text_input('Sex')

    with col3:
        cp = st.text_input('Chest Pain types')

    with col1:
        trestbps = st.text_input('Resting Blood Pressure')

    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')

    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')

    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')

    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')

    with col3:
        exang = st.text_input('Exercise Induced Angina')

    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')

    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')

    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')

    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):

        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]

        user_input = [float(x) for x in user_input]

        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)
    
    
    
# Parkinsons Prediction Page
if (selected == 'Parkinsons Prediction'):
    
    #page title
    st.title('Parkinsons Prediction Using ML') 
    

    
    ms = st.session_state
    if "themes" not in ms: 
      ms.themes = {"current_theme": "light",
                        "refreshed": True,
                        
                        "light": {"theme.base": "dark",
                                  "theme.backgroundColor": "black",
                                  "theme.primaryColor": "#c98bdb",
                                  "theme.secondaryBackgroundColor": "#5591f5",
                                  "theme.textColor": "white",
                                  "theme.textColor": "white",
                                  "button_face": "🌜"},

                        "dark":  {"theme.base": "light",
                                  "theme.backgroundColor": "white",
                                  "theme.primaryColor": "#5591f5",
                                  "theme.secondaryBackgroundColor": "#82E1D7",
                                  "theme.textColor": "#0a1464",
                                  "button_face": "🌞"},
                        }
      

    def ChangeTheme():
      previous_theme = ms.themes["current_theme"]
      tdict = ms.themes["light"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]
      for vkey, vval in tdict.items(): 
        if vkey.startswith("theme"): st._config.set_option(vkey, vval)

      ms.themes["refreshed"] = False
      if previous_theme == "dark": ms.themes["current_theme"] = "light"
      elif previous_theme == "light": ms.themes["current_theme"] = "dark"


    btn_face = ms.themes["light"]["button_face"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]["button_face"]
    st.button(btn_face, on_click=ChangeTheme)

    if ms.themes["refreshed"] == False:
      ms.themes["refreshed"] = True
      st.rerun()
    
    
    # User Input Section

    user_input = st.text_input("Name of the patient")

    # Button with no effect on input or result
    if st.button("Enter"):
       # st.balloons()  # This will show an animation but won't affect data

    # Displaying User Input
        st.write("Submit")
        st.write(f"You entered: {user_input}")

    
    
    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')

    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')

    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')

    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')

    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')

    with col2:
        PPQ = st.text_input('MDVP:PPQ')

    with col3:
        DDP = st.text_input('Jitter:DDP')

    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')

    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')

    with col3:
        APQ = st.text_input('MDVP:APQ')

    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')

    with col1:
        HNR = st.text_input('HNR')

    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')

    with col4:
        spread1 = st.text_input('spread1')

    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')

    with col2:
        PPE = st.text_input('PPE')

    # code for Prediction
    parkinsons_diagnosis = ''

    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):

        user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                      RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                      APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

        user_input = [float(x) for x in user_input]

        parkinsons_prediction = parkinsons_model.predict([user_input])

        if parkinsons_prediction[0] == 1:
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"

    st.success(parkinsons_diagnosis)  
   
    
 # Lung Cancer Prediction Page
if (selected == 'Lung Cancer Prediction'):
     
     #page title
     st.title('Lung Cancer Prediction Using ML')
     
     ms = st.session_state
     if "themes" not in ms: 
       ms.themes = {"current_theme": "light",
                         "refreshed": True,
                         
                         "light": {"theme.base": "dark",
                                   "theme.backgroundColor": "black",
                                   "theme.primaryColor": "#c98bdb",
                                   "theme.secondaryBackgroundColor": "#5591f5",
                                   "theme.textColor": "white",
                                   "theme.textColor": "white",
                                   "button_face": "🌜"},

                         "dark":  {"theme.base": "light",
                                   "theme.backgroundColor": "white",
                                   "theme.primaryColor": "#5591f5",
                                   "theme.secondaryBackgroundColor": "#82E1D7",
                                   "theme.textColor": "#0a1464",
                                   "button_face": "🌞"},
                         }
       

     def ChangeTheme():
       previous_theme = ms.themes["current_theme"]
       tdict = ms.themes["light"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]
       for vkey, vval in tdict.items(): 
         if vkey.startswith("theme"): st._config.set_option(vkey, vval)

       ms.themes["refreshed"] = False
       if previous_theme == "dark": ms.themes["current_theme"] = "light"
       elif previous_theme == "light": ms.themes["current_theme"] = "dark"


     btn_face = ms.themes["light"]["button_face"] if ms.themes["current_theme"] == "light" else ms.themes["dark"]["button_face"]
     st.button(btn_face, on_click=ChangeTheme)

     if ms.themes["refreshed"] == False:
       ms.themes["refreshed"] = True
       st.rerun()
     
     # User Input Section

     user_input = st.text_input("Name of the patient")

     # Button with no effect on input or result
     if st.button("Enter"):
        # st.balloons()  # This will show an animation but won't affect data

     # Displaying User Input
         st.write("Submit")
         st.write(f"You entered: {user_input}")

     
     
     #getting the input data from user
     #columns for input fields
     
     col1, col2, col3 = st.columns(3)
     
     with col1:
         GENDER = st.text_input('GENDER')
          
     with col2:
         AGE = st.text_input('AGE')
          
     with col3:
         SMOKING = st.text_input('SMOKING')
          
     with col1:
         YELLOW_FINGERS = st.text_input('YELLOW_FINGERS')
          
     with col2:
         ANXIETY = st.text_input('ANXIETY')
          
     with col3:
         PEER_PRESSURE = st.text_input('PEER_PRESSURE')
         
     with col1:
         CHRONIC_DISEASE = st.text_input('CHRONIC_DISEASE')    
              
     with col2:
         FATIGUE = st.text_input('FATIGUE')   

     with col3:
         ALLERGY = st.text_input('ALLERGY')
    
     with col1:
         WHEEZING = st.text_input('WHEEZING')    
         
     with col2:
         ALCOHOL_CONSUMING = st.text_input('ALCOHOL CONSUMING')  
     
     with col3:
         COUGHING = st.text_input('COUGHING')
            
     with col1:
         SHORTNESS_OF_BREATH = st.text_input('SHORTNESS OF BREATH')    
                 
     with col2:
         SWALLOWING_DIFFICULTY = st.text_input('SWALLOWING DIFFICULTY')  
         
     with col3:
         CHEST_PAIN = st.text_input('CHEST PAIN')
             
         

     # Code for Prediction
     Lung_Cancer_diagnosis = ''
      
     # creating a button for Prediction
      
     if st.button('Lung Cancer Test Result'):
         
         user_input = [
             GENDER, AGE, SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE, FATIGUE, ALLERGY,
             WHEEZING, ALCOHOL_CONSUMING, COUGHING, SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN
             ]
        
          
         user_input = [float(x) for x in user_input]
         
         Lung_Cancer_prediction = lung_cancer_model.predict([user_input])
          
         if (Lung_Cancer_prediction[0]) == 1:
             Lung_Cancer_diagnosis == 'The Person suffers from Lung Cancer'
             
         else:
             Lung_Cancer_diagnosis = 'The Person doesnot suffer from Lung Cancer'
            
     st.success(Lung_Cancer_diagnosis)
      
                       

    
    
    
    
    
    
    
    