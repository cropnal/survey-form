import streamlit as st
import pandas as pd
import subprocess

def install_libraries():
    try:
        # Use subprocess to run the pip install commands
        subprocess.check_call(["pip", "install", "matplotlib", "seaborn"])

        print("Matplotlib and Seaborn installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing libraries: {e}")


import matplotlib.pyplot as plt
import seaborn as sns
import os
# Tab 2: Analytics
def main():
    st.title("Cropnal Survey")
    tabs = ["Farmer Survey","Vegetable Survey","Trader Survey", "Admin Analytics"]
    current_tab = st.selectbox("Select Tab", tabs)

    if current_tab == "Farmer Survey":
        st.header("Farmer Survey")
        csv_filename = "farmer_survey_data.csv"
        file_exists = os.path.isfile(csv_filename)

        st.subheader("Farmer Information")
        farmer_name = st.text_input("Farmer Name", "John Doe")
        village = st.text_input("Village", "Sample Village")
        mobile = st.text_input("Mobile", "1234567890")

        st.subheader("Main Income Crops")
        crop_name = st.text_input("Crop Name", "Rice")
        crop_duration = st.number_input("Crop Duration (months)", min_value=1, step=1, value=6)
        crop_area = st.number_input("Crop Area in Bigha", min_value=0.1, step=0.1, value=5.0)
        seeds = st.text_input("Seeds", "Hybrid Seeds")
        fertilizer_cost = st.number_input("Fertilizer Cost", min_value=0, value=5000)
        fertilizer_type = st.text_input("Which Fertilizer", "NPK")
        pesticide_cost = st.number_input("Pesticide Cost", min_value=0, value=1000)

        st.subheader("Water Supply")
        water_supply_options = st.radio("Water Supply Options", ["Tube Well", "Canal Water"], index=0)
        water_supply_system = st.selectbox("Water Supply System", ["Randomly", "Drip Irrigation", "Fountains", "Others"], index=1)
        water_system_cost = st.number_input("Cost of Water System", min_value=0, value=2000)

        st.subheader("Labor and Yield")
        labour_cost = st.number_input("Labour Cost", min_value=0, value=3000)
        crop_yield = st.number_input("Crop Yield in KG", min_value=0, value=5000)

        st.subheader("Market Information")
        selling_market = st.text_input("Selling Market", "Local Market")
        market_price = st.number_input("Market Price", min_value=0, value=10)

        st.subheader("Challenges and Satisfaction")
        weather_issue = st.text_input("Weather Issue", "Drought")
        gov_compensation = st.checkbox("Government Compensation", value=True)
        crop_insurance = st.checkbox("Crop Insurance", value=False)
        storage_challenges = st.checkbox("Storage Challenges", value=True)

        st.subheader("Miscellaneous and Satisfaction")
        happy_with_income = st.radio("Are you happy with your current income?", ["Yes", "No"], index=0)
        farming_job_satisfaction = st.radio("Is salary farming job okay?", ["Yes", "No"], index=1)
        inspire_other_farmers = st.radio("Open to inspiring other farmers?", ["Yes", "No"], index=0)

        miscellaneous_cost = st.number_input("Miscellaneous Cost", min_value=0, value=500)
        extra_description = st.text_area("Extra Description", "No additional comments")

        if st.button("Submit"):
            # Store data in CSV
            data = {
                "Farmer Name": farmer_name,
                "Village": village,
                "Mobile": mobile,
                "Crop Name": crop_name,
                "Crop Duration (months)": crop_duration,
                "Crop Area in Bigha": crop_area,
                "Seeds": seeds,
                "Fertilizer Cost": fertilizer_cost,
                "Which Fertilizer": fertilizer_type,
                "Pesticide Cost": pesticide_cost,
                "Water Supply Options": water_supply_options,
                "Water Supply System": water_supply_system,
                "Cost of Water System": water_system_cost,
                "Labour Cost": labour_cost,
                "Crop Yield in KG": crop_yield,
                "Selling Market": selling_market,
                "Market Price": market_price,
                "Weather Issue": weather_issue,
                "Government Compensation": gov_compensation,
                "Crop Insurance": crop_insurance,
                "Storage Challenges": storage_challenges,
                "Happy with Income": happy_with_income,
                "Farming Job Satisfaction": farming_job_satisfaction,
                "Inspire Other Farmers": inspire_other_farmers,
                "Miscellaneous Cost": miscellaneous_cost,
                "Extra Description": extra_description
            }

            # Check if the file exists to determine whether to write the header
            mode = "w" if not file_exists else "a"

            df = pd.DataFrame(data, index=[0])
            df.to_csv(csv_filename, mode=mode, header=not file_exists, index=False)

            st.success("Survey submitted successfully!")
            st.toast('Data Saved', icon='😍')

    elif current_tab == "Admin Analytics":
        st.header("Admin Analytics")

        # Choose survey type
        survey_type = st.selectbox("Select Survey Type", ["farmer_survey", "vegetable_survey", "trader_survey"])

        

        

        
        if survey_type=="farmer_survey":
            csv_filename = f"{survey_type.lower()}_data.csv"
            data = pd.read_csv(csv_filename) 
            # Display data table
            st.subheader("Data Table")
            st.dataframe(data)

            # Display relevant graphs
            st.subheader("Data Analytics")

            # Total number of entries
            total_entries = len(data)
            if 'Happy with Income' in data.columns:
                st.subheader("Farmers Happiness Distribution")

                # Calculate percentage of happy and unhappy farmers
                happy_percentage = (data['Happy with Income'] == 'Yes').sum() / total_entries * 100
                unhappy_percentage = (data['Happy with Income'] == 'No').sum() / total_entries * 100

                # Determine background color based on happiness percentage
                background_color_happy = "#4CAF50"
                background_color_sad = "#FF5733"
                background_color_total = "#808080"  # Grey for total

                # Create labeled areas with big green or red background
                st.markdown(
                    f"""
                    <div style='background-color: #0000; padding: 10px; border-radius: 10px; display: flex; justify-content: space-between;'>
                        <div style='background-color: {background_color_happy}; padding: 30px; border-radius: 10px;'>
                            <h1 style='color: white; font-size: 40px; text-align: center;'> {happy_percentage:.2f}%</h1>
                            <p style='color: white; text-align: center;'>Happy Farmers</p>
                        </div>
                        <div style='background-color: {background_color_total}; padding: 30px; border-radius: 10px;'>
                            <h1 style='color: white; font-size: 40px; text-align: center;'> {total_entries}</h1>
                            <p style='color: white; text-align: center;'>Total Farmers</p>
                        </div>
                        <div style='background-color: {background_color_sad}; padding: 30px; border-radius: 10px;'>
                            <h1 style='color: white; font-size: 40px; text-align: center;'> {unhappy_percentage:.2f}%</h1>
                            <p style='color: white; text-align: center;'>Unhappy Farmers</p>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )




        elif survey_type=="vegetable_survey":   
            csv_filename = f"{survey_type.lower()}_data.csv"

            data = pd.read_csv(csv_filename) 
            # Display data table
            st.subheader("Data Table")
            st.dataframe(data)

            # Display relevant graphs
            st.subheader("Data Analytics")

            # Total number of entries
            total_entries = len(data)
            st.subheader("Vegetable Sellers Analysis")

            # Calculate total vegetable sellers
            total_vegetable_sellers = total_entries

            # Calculate percentage of happy and unhappy vegetable sellers
            happy_percentage_vegetable = (data['Happiness Index'] == 'Yes').sum() / total_vegetable_sellers * 100
            unhappy_percentage_vegetable = (data['Happiness Index'] == 'No').sum() / total_vegetable_sellers * 100


            # Determine background color based on happiness percentage
            background_color_happy_vegetable = "#4CAF50"
            background_color_sad_vegetable = "#FF5733"
            background_color_total_vegetable = "#808080"  # Grey for total

            # Create labeled areas with big green or red background for vegetable sellers
            st.markdown(
                f"""
                <div style='background-color: #0000; padding: 10px; border-radius: 10px; display: flex; justify-content: space-between;'>
                    <div style='background-color: {background_color_happy_vegetable}; padding: 30px; border-radius: 10px;'>
                        <h1 style='color: white; font-size: 40px; text-align: center;'> {happy_percentage_vegetable:.2f}%</h1>
                        <p style='color: white; text-align: center;'>Happy Vegetable Sellers</p>
                    </div>
                    <div style='background-color: {background_color_total_vegetable}; padding: 30px; border-radius: 10px;'>
                        <h1 style='color: white; font-size: 40px; text-align: center;'> {total_vegetable_sellers}</h1>
                        <p style='color: white; text-align: center;'>Total Vegetable Sellers</p>
                    </div>
                    <div style='background-color: {background_color_sad_vegetable}; padding: 30px; border-radius: 10px;'>
                        <h1 style='color: white; font-size: 40px; text-align: center;'> {unhappy_percentage_vegetable:.2f}%</h1>
                        <p style='color: white; text-align: center;'>Unhappy Vegetable Sellers</p>
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )




    elif current_tab == "Vegetable Survey":
        st.title("Vegetable Survey")
        # Check if the CSV file exists
        csv_filename = "vegetable_survey_data.csv"
        file_exists = os.path.isfile(csv_filename)
        # Vegetable Information
        seller_name = st.text_input("Seller Name", "Vegetable Seller")
        vegetable_name = st.text_input("Vegetable Name", "Tomato")
        amount_purchase = st.number_input("Kg purchase", min_value=0.0, value=10.0)
        purchase_value_per_kg = st.number_input("Vegetable Purchase Value per KG", min_value=0.0, value=5.0)
        transport_cost = st.number_input("Transport Cost", min_value=0.0, value=50.0)
        spoilage_losses = st.number_input("Spoilage Losses", min_value=0.0, value=10.0)
        selling_price = st.number_input("Selling Price", min_value=0.0, value=15.0)

        # Purchase Information
        purchase_location = st.text_input("Purchase Location", "Local Market")

        # Happiness Index
        happiness_index = st.radio("Happy with Income?", ["Yes", "No"], index=0)

        if st.button("Submit"):
        # Store data in CSV
            data = {
                "Seller Name": seller_name,
                "Vegetable Name": vegetable_name,
                "Vegetable Purchase Value per KG": purchase_value_per_kg,
                "Kg Purchase": amount_purchase,
                "Transport Cost": transport_cost,
                "Spoilage Losses": spoilage_losses,
                "Selling Price": selling_price,
                "Purchase Location": purchase_location,
                "Happiness Index": happiness_index,
            }

            # Check if the file exists to determine whether to write the header
            mode = "w" if not file_exists else "a"

            df = pd.DataFrame(data, index=[0])
            df.to_csv(csv_filename, mode=mode, header=not file_exists, index=False)

            st.success("Survey submitted successfully!")
            st.toast("Data successfully added!")

            



            



            

            


        
    


if __name__ == "__main__":
    main()
