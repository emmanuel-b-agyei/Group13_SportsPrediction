import streamlit as st
import pickle


model = pickle.load(open('Group13_SportsPrediction.pkl', 'rb'))


st.title('Player Rating Prediction App')
st.write('Enter player details to predict the rating.')


age = st.number_input('Age', min_value=16, max_value=40)
potential = st.number_input('Potential', min_value=0, max_value=100)
Value_in_Euros = st.number_input('Value in Euros', min_value=0, max_value=9999999999999)
Wage_in_euros = st.number_input('Wage in Euros', min_value=0, max_value=9999999999999)
Passing = st.number_input('Passing', min_value=0, max_value=100)
Dribbling = st.number_input('Dribbling', min_value=0, max_value=100)
Physic = st.number_input('Physic', min_value=0, max_value=100)
Attacking_short_passing = st.number_input('Attacking Short Passing', min_value=0, max_value=100)
Movement_reactions = st.number_input('Movement Reactions', min_value=0, max_value=100)
Power_shot_power = st.number_input('Power Shot Power', min_value=0, max_value=100)
Mentality_vision = st.number_input('Mentality Vision', min_value=0, max_value=100)
Mentality_composure = st.number_input('Mentality Composure', min_value=0, max_value=100)


def predict_rating(age, potential, Value_in_Euros, Wage_in_euros, Passing, Dribbling, Physic, Attacking_short_passing, Movement_reactions, Power_shot_power, Mentality_vision, Mentality_composure):
    
    
    prediction = model.predict([[age, potential, Value_in_Euros, Wage_in_euros, Passing, Dribbling, Physic, Attacking_short_passing, Movement_reactions, Power_shot_power, Mentality_vision, Mentality_composure]])[0]
    return prediction

if st.button('Predict'):
    rating = predict_rating(age, potential, Value_in_Euros, Wage_in_euros, Passing, Dribbling, Physic, Attacking_short_passing, Movement_reactions, Power_shot_power, Mentality_vision, Mentality_composure)
    st.write(f'Predicted Rating: {rating}')