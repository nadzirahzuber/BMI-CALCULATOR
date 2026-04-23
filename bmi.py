import streamlit as st
st.set_page_config(page_title="BMI Calculator",page_icon="🔥",layout="centered")
st.title("BMI Calculator💪")
st.write("Let's Calculate Your **Body Mass Index** And Understand What It Means")

st.header("Enter Your Details 🖋️")

height = st.number_input("Enter Your Height (in cm)",min_value=90,max_value=200,value=170)
weight = st.number_input("Enter Your Weight (in kg)",min_value=10,max_value=300,value=70)

st.write(f"📏 Your Height :{height} in cm")
st.write(f"📍 Your Weight :{weight} in kg")

if st.button("Calculate BMI"):
    h_m = height / 100 # convert cm into meters
    bmi = weight /(h_m)**2
    st.success(f"Your BMI Is **{bmi:.2f}**")

    # Print BMI Categoory
    if bmi < 18.5:
          category = "Underweight 🥲"
          color ="#27F5E7"

    elif 18.5<=bmi<25:
         category = "Normal 😜"
         color ="#FA82D9"
         
    elif 25<=bmi<30:
         category = "Overweight 🫣"
         color = "#D62B50"

    else:
         category = "Obese 🤯"
         color ="#EB3323"

    st.markdown(
         f"""
         <div style='background-color:{color};padding:15px;border-radius:10px;text-align:center'>
         <h3 style='color: #F5F5C1;'>Your BMI Category : {category}</h3>
         </div>
         """,
         unsafe_allow_html=True
    )