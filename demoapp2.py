import streamlit as st
import pandas as pd

# Initial student data
data = {
     "StudentID": [1, 2, 3,4,5],
    "FirstName": ["Thomas", "Bob", "John","Black","Wonder"],
    "LastName": ["Shelby", "Marlie", "Wick","Widow","Women"],
    "DateOfBirth": ["2002-05-14", "2001-09-23", "2003-01-10","2004-07-18","2005-12-19"],
    "Gender": ["Male", "Male", "Male","Female","Female"],
    "Email": ["shelby@example.com", "bob@example.com", "jhon@example.com","black@example.com","Women@example.com"],
    "PhoneNumber": ["057545690", "9876543210", "8675497367","7645834581","265129078756"]
}



if "df" not in st.session_state:
    st.session_state.df = pd.DataFrame(data)

st.title("Student Table")

st.write(" Edit Existing Students")
edited_df = st.data_editor(st.session_state.df, num_rows="dynamic")
st.session_state.df = edited_df  

st.write("Add a New Student")
with st.form("add_student"):
    sid = st.number_input("Student ID", min_value=1)
    fname = st.text_input("First Name")
    lname = st.text_input("Last Name")
    dob = st.date_input("Date of Birth")
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    email = st.text_input("Email")
    phone = st.text_input("Phone Number")
    submitted = st.form_submit_button("Add Student")

    if submitted:
        new_row = {
            "StudentID": sid,
            "FirstName": fname,
            "LastName": lname,
            "DateOfBirth": dob.strftime("%Y-%m-%d"),
            "Gender": gender,
            "Email": email,
            "PhoneNumber": phone
        }
        st.session_state.df = pd.concat(
            [st.session_state.df, pd.DataFrame([new_row])],
            ignore_index=True
        )
        st.success("✅ Student added successfully!")

st.write("Current Student List")
st.dataframe(st.session_state.df)

st.download_button(
    "Download Updated CSV",
    st.session_state.df.to_csv(index=False),
    "students.csv",
    "text/csv"
)