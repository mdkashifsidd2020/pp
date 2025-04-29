import streamlit as st
import joblib

model=joblib.load('placement.pkl')


def main():
    st.title("Welcome to Placement Predictor")

    # cgpa = st.slider("Select your CGPA", min_value=0.0, max_value=10.0, step=0.1)
    # st.write("Your entered CGPA:", cgpa)

    # percentage=st.slider("select your percentage",min_value=0.0,max_value=100.0,step=0.1)
    # st.write("entered percentage",percentage)

    cgpa=st.number_input("enter your cgpa")

    if st.button("Check"):
        result=model.predict([[cgpa]])
        st.success(f"your package will be {result}")
        

if __name__ == '__main__':
    main()
