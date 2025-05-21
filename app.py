import streamlit as st
from datetime import datetime, date

st.title("🎓 Sri Chaitanya Techno School Admission Assistant")
st.markdown("Welcome! This tool helps determine your child's eligibility for admission into LKG or Pre-Nursery.")

# Query about joining
query = st.radio("Would you like to join our school?", ("Select", "Yes", "No"))

if query == "Yes":
    grade1 = st.radio("Would you like to join LKG or Pre-Nursery?", ("Select", "LKG", "Pre-Nursery"))

    st.markdown("**Age Criteria:**")
    st.markdown("- Pre-Nursery: 2.6 years - 3.9 years")
    st.markdown("- LKG: 3.10 years - 4.10 years")

    date_entry = st.date_input("Enter your child's Date of Birth")

    if date_entry:
        # Calculate age
        today = date.today()
        age_in_days = (today - date_entry).days
        age_in_years = round(age_in_days / 365.2425, 2)
        st.success(f"Your child's age is approximately **{age_in_years} years**")

        # Check eligibility
        if age_in_years <= 2.5:
            st.error("Your child is not eligible for admission.")
        elif 3.10 <= age_in_years <= 4.10:
            st.success("Your child is eligible for **LKG**.")
            if st.button("Confirm Admission to LKG"):
                fee = 30000 + 90000
                st.info(f"The total fee is ₹{fee}")
        elif 2.6 <= age_in_years <= 3.9:
            st.success("Your child is eligible for **Pre-Nursery**.")
            program = st.selectbox("Choose a program:", ["Select", "Maverick", "Starkids"])
            if program == "Maverick":
                fee = 30000 + 80000
                st.info(f"The fee for the Maverick program is ₹{fee}")
            elif program == "Starkids":
                fee = 30000 + 55000
                st.info(f"The fee for the Starkids program is ₹{fee}")
        elif age_in_years >= 6.0:
            st.warning(f"Your child is too old for LKG or Pre-Nursery (age: {age_in_years} years). Please contact the admissions office.")
        elif 4.10 < age_in_years < 6.0:
            st.warning("Your child's age falls into a special category. Please contact the admin department for further details.")
elif query == "No":
    st.info("Thanks for visiting our website!")
