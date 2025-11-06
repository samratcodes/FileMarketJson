import os
import json

# Create folders if they don't exist
os.makedirs("male", exist_ok=True)
os.makedirs("female", exist_ok=True)

# Paste your Excel-like data here (tab-separated for each row)
# Each row should be a string in this list
excel_data = [
    "S46\t#0002C (Nepali, Male, 22, Chitwan, Nepal)\tSylvester\tMale\t26\tKenya\tKenya\tKenya\tSwahili\tEnglish, Swahili, Mamba\tKenya Accent\tEnglish\tYes\t\t46:22 min\t234 MB\t229 MB\t234 MB\tXiaomi Redmi A5\tOk (Low volume and some noise)",
    "S48\t#0002C (Nepali, Male, 22, Chitwan, Nepal)\tGbenle\tMale\t21\tNigeria\tNigeria\tNigeria\tYoruba\tYoruba, English\tNigerian Accent\tEnglish\tYes\t\t41:25 min\t200.9 MB\t200.9 MB\t200.9 MB\tItel A80\tOk (Some background noise)",
    "S49\t#0002C (Nepali, Male, 22, Chitwan, Nepal)\tJoseph\tMale\t30\tKenya\tKenya\tKenya\tEnglish\tEnglish\tKenya Accent\tEnglish\tYes\t\t38:52 min\t195.5 MB\t196.4 MB\t196.6 MB\tTecno KJ5, Tecno Earphone\tOk (White noise)",
    "S50\t#0002C (Nepali, Male, 22, Chitwan, Nepal)\tJoshua\tMale\t28\tNigeria\tNigeria\tNigeria\tYoruba, English\tYoruba, English\tNigerian Accent\tEnglish\tYes\t\t39:42 min\t200 MB\t200 MB\t200 MB\tDell 7290, Tecno Small Headset\tOk (Constant white noise and background noise)"
]



for row in excel_data:
    # Split row by tab
    columns = row.split("\t")
    
    # Extract agent details (split the complex string)
    agent_info = columns[1].strip()
    # Example format: "#0002C (Nepali, Male, 22, Chitwan, Nepal)"
    code, details = agent_info.split(" (")
    details = details.rstrip(")").split(", ")
    
    agent_dict = {
        "code": code,
        "native_language": details[0],
        "gender": details[1],
        "age": int(details[2]),
        "city": details[3],
        "country": details[4]
    }
    
    # Respondent details
    languages_known = [lang.strip() for lang in columns[9].split(",")]
    
    respondent_dict = {
        "first_name": columns[2].strip(),
        "gender": columns[3].strip(),
        "age": int(columns[4]),
        "country": columns[5].strip(),
        "language_native": columns[8].strip(),
        "languages_known": languages_known,
        "accent_or_dialect": columns[10].strip(),
        "call_language": columns[11].strip()
    }
    
    # Recording details
    recording_dict = {
        "recording_link_agent": [""],  # Leave empty for now
        "recording_link_respondent": [""],  # Leave empty for now
        "duration": columns[14].strip(),
        "file_size_agent": columns[15].strip(),
        "file_size_respondent": columns[16].strip(),
        "device_used": columns[18].strip(),
        "noise_level": "Low",  # You can modify if needed
        "notes": columns[19].strip()
    }
    
    # Full JSON structure
    json_data = {
        "id": columns[0].strip(),
        "agent_details": agent_dict,
        "respondent_details": respondent_dict,
        "consent": columns[12].strip(),
        "recording_details": recording_dict
    }
    
    # Determine folder by respondent gender
    gender_folder = "male" if respondent_dict["gender"].lower() == "male" else "female"
    
    # Save JSON file
    file_path = os.path.join(gender_folder, f"{columns[0].strip()}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(json_data, f, ensure_ascii=False, indent=2)

print("Conversion complete. JSON files saved in 'male' and 'female' folders.")