# The main limitation of the Firebase Real time data base is that, only JSON data can be imported. However the Kaggle data set is of CSV format.
# Hence it is necessary to convert from CSV to the JSON format.

# Used the link https://csvjson.com/csv2json to convert CSV to JSON. However the JSON still needed to be restructured properly for accessing the data properly.
# Hence used the below python code to convert into proper JSON format to be imported to Firebase

import json

# Loading the JSON data from the input file and converting it to the required format
with open('C:/Users/visha/Downloads/csvjson.json', 'r') as file:
    input_data_json_data = json.load(file)

# Transforming the JSON data into the desired JSON format which could be uploaded in the Firebase, by importing the json file
output_Alldata_proper = {"EmployeeSet": {}}

for each_entry_data in input_data_json_data:
    user_id = each_entry_data["User_ID"]
    # Adding the each_each_entry_data_data under the EmployeeSet Root key
    output_Alldata_proper["EmployeeSet"][user_id] = {
        "USER_ID": user_id,
        "Age": each_entry_data["Age"],
        "Gender": each_entry_data["Gender"],
        "Technology_Usage_Hours": each_entry_data["Technology_Usage_Hours"],
        "Social_Media_Usage_Hours": each_entry_data["Social_Media_Usage_Hours"],
        "Gaming_Hours": each_entry_data["Gaming_Hours"],
        "Screen_Time_Hours": each_entry_data["Screen_Time_Hours"],
        "Mental_Health_Status": each_entry_data["Mental_Health_Status"],
        "Stress_Level": each_entry_data["Stress_Level"],
        "Sleep_Hours": each_entry_data["Sleep_Hours"],
        "Physical_Activity_Hours": each_entry_data["Physical_Activity_Hours"],
        "Support_Systems_Access": each_entry_data["Support_Systems_Access"],
        "Work_Environment_Impact": each_entry_data["Work_Environment_Impact"],
        "Online_Support_Usage": each_entry_data["Online_Support_Usage"],
    }

# Writing the transformed JSON data to an output file
with open('C:/Users/visha/Downloads/proper_jsonFirebase.json', 'w') as file:
    json.dump(output_Alldata_proper, file, indent=2)

print("Data has been converted successfully and saved properly in required format to proper_jsonFirebase.json")
