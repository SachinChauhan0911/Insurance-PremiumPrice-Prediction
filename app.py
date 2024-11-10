import streamlit as st
import pickle
import pandas 
import numpy 


st.header("Premium Price Prediction", divider="gray")

col1, col2= st.columns(2)

#with col1:
#st.subheader("Age")
Age = st.number_input("Age")


#with col2:
#st.subheader("Diabetes")
Diabetes = col1.selectbox(
    "Diabetes",[0, 1])
   

#with col3:
#st.subheader("BloodPressureProblems")
BloodPressureproblems = col1.selectbox(
 "BloodPressureproblems",[0, 1])

#with col4:
#st.subheader("AnyTransplants")
AnyTransplants = col1.selectbox(
    "AnyTransplants",[0, 1])

#with col5:
#st.subheader("AnyChronicDiseases")
AnyChronicDisease = col2.selectbox(
    "AnyChronicDisease",[0, 1])

Height = st.slider("Height (in cm)", 140, 200, 1)

Weight = st.slider("Weight", 50, 200, 1)

#with col6:
#st.subheader("HistoryOfCancerinFamily")
HistoryofCancerinFamily = col2.selectbox(
    "HistoryofCancer",[0, 1])

#with col7:
#st.subheader("NumberOfmajorSurgeries")
NumberofMajorSurgeries = col2.selectbox(
    "NumberofMajorSurgeries",[0, 1, 2, 3, 4])


def model_pred(Age, Diabetes, BloodPressureproblems, AnyTransplants, AnyChronicDisease, Height, Weight, HistoryofCancerinFamily, NumberofMajorSurgeries):
    with open("best_model_4", "rb") as file:
        pred = pickle.load(file)

    input_features = [[Age, Diabetes, BloodPressureproblems,\
                        AnyTransplants, AnyChronicDisease, Height, Weight,\
                            HistoryofCancerinFamily, NumberofMajorSurgeries]]
    return pred.predict(input_features)

if (st.button("Predict Premium")):
    Premium = model_pred(Age, Diabetes, BloodPressureproblems,\
                    AnyTransplants, AnyChronicDisease, Height, Weight, \
                    HistoryofCancerinFamily, NumberofMajorSurgeries)
   
    st.text(f"The Premium Price for the individuals to be insured is {Premium[0].round(2)}")
