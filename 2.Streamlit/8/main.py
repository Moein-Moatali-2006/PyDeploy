import datetime 
import streamlit as st

st.title("My Streamlit App")

with st.sidebar:
    agree = st.checkbox("I agree")
    values = st.slider("Select a range of values", 0.0, 100.0, (25.0,75.0))
    values = st.date_input("When's your birthday", datetime.date(2019, 7, 6))

col1, col2 = st.columns(2)

with col1:
    st.write("Hello World")

    my_btn = st.button("Click me")
    if my_btn:
        st.write("سلام")
    else:
        st.write("خداحافظ")

    st.text_input("FirstName")
    st.text_input("LastName")

with col2:
    weight = st.number_input("Enter your weight (kg)")
    height = st.number_input("Enter your height (cm)")

    my_btn_2 = st.button("Calculate BMI")

    if my_btn_2:
        bmi = weight / ((height / 100) ** 2)
        st.info(bmi)
        # st.error()
        # st.success()
        # st.warning()
        if bmi < 18.5:
            st.write("لاغر")
        elif 18.5 < bmi < 25:
            st.write("عالی!")
        elif 25 < bmi <30:
            st.write("چاقالو")

st.warning("سطر جدید")