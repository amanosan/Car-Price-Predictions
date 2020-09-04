import streamlit as st
import datetime
import pickle

model = pickle.load(open('used_car_predict_model.pkl', 'rb'))

st.title("Used Car Price Prediction")
st.write("#### This App will predict the selling price of your car.")


def get_features():
    # Age
    current_year = datetime.datetime.now().year
    age = current_year - int(st.number_input(label="Year of Manufacturing", value=0, step=1))

    # Kilometers Driven
    kms_driven = float(st.number_input(label="Kilometers Driven", value=0.0, step=0.1))

    # Mileage
    mileage = float(st.number_input(label="Mileage(kmpl)", value=0.0, step=0.1))

    # Engine Size
    engine = int(st.number_input(label='Engine Size(in CC)', value=0, step=1))

    # Power
    power = int(st.number_input(label='Power (bhp)', value=0, step=1))

    # Number of Seats
    seats = int(st.number_input(label="Number of Seats", min_value=2, max_value=10, value=2, step=1))

    # Transmission
    transmission = st.radio(label='Transmission Type', options=('Manual', 'Automatic'))
    if transmission == 'Manual':
        transmission_manual=1
    else:
        transmission_manual=0

    # Fuel Type
    fuel = st.selectbox(label='Fuel', options=('Petrol', 'Diesel', 'CNG', 'LPG'))
    if fuel == 'CNG':
        fuel_type_diesel = 0
        fuel_type_petrol = 0
        fuel_type_lpg = 0
    elif fuel == 'Diesel':
        fuel_type_diesel = 1
        fuel_type_petrol = 0
        fuel_type_lpg = 0
    elif fuel == 'Petrol':
        fuel_type_diesel = 0
        fuel_type_petrol = 1
        fuel_type_lpg = 0
    else:
        fuel_type_diesel = 0
        fuel_type_petrol = 0
        fuel_type_lpg = 1

    # Owner 
    owner = st.selectbox(label="Owner Type", options=('First', 'Second', 'Third', 'Fourth & Above'))
    if owner == 'First':
        owner_type_second = 0
        owner_type_third = 0
        owner_type_fourth = 0
    elif owner == 'Second':
        owner_type_second = 1
        owner_type_third = 0
        owner_type_fourth = 0
    elif owner == 'Third':
        owner_type_second = 0
        owner_type_third = 1
        owner_type_fourth = 0
    else:
        owner_type_second = 0
        owner_type_third = 0
        owner_type_fourth = 1


    return [kms_driven, mileage, engine, power, seats, age,
    fuel_type_diesel, fuel_type_lpg, fuel_type_petrol, transmission_manual,
    owner_type_fourth, owner_type_second, owner_type_third]


features = get_features()

predicted_price = model.predict([features])
predicted_price *= 100000
# Creating a button of Predict
predict = st.button(label='PREDICT')

my_prediction = st.empty()
if predict:
    my_prediction.subheader(f"The car can be sold for Rs.{float(predicted_price):.0f}")