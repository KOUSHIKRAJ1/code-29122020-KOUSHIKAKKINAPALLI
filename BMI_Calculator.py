import json #json module is used for reading data from json file
def load_json_data(json_file): #loads data from json file and in turn returns list of objects where each object is in the form of <key,value> pair
    #open json file for reading using open() by default it opens the file in read mode
    try:
        with open(json_file) as person_file_details: #person_file_details is file object pointing to json file
            person_details=json.load(person_file_details) #load function returns a list of objects using json module
        return person_details
    except OSError: #handling exception when file is not found for reading
        print("File not found for reading")
def calculate(mass,height): #bmi(kg/m2)=mass(kg)/height(m2)
    bmi=mass/(height*height)
    return bmi
def getBMICategoryAndHealthRisk(bmi): #return category and health risk
    if bmi<=18.4:
        category,healthrisk=("Underweight","Malnutrition risk")
    elif bmi>=18.5 and bmi<=24.9:
        category,healthrisk=("Normal weight","Low risk")
    elif bmi>=25 and bmi<=29.9:
        category,healthrisk=("Overweight","Enhanced risk")
    elif bmi>=30 and bmi<=34.9:
        category,healthrisk=("Moderately obese","Medium risk")
    elif bmi>=35 and bmi<=39.9:
        category,healthrisk=("Severely obese","High risk")
    elif bmi>=40:
        category,healthrisk=("Very severely obese","Very high risk")
    return (category,healthrisk)
def CalculateBMI(person_details): #calculate bmi for each individual person by storing the results in list and returning it
    bmi_details=[] #creates empty list for storing bmi details
    #loop through objects in person_details
    for person in person_details:
        mass=person["WeightKg"] #get the weight
        height=person["HeightCm"]*0.01 #convert height in cm to meters
        bmi=calculate(mass,height) #calculate bmi
        #get category and health risk based on bmi
        category,healthrisk=getBMICategoryAndHealthRisk(bmi)
        #add these entries as 3 new columns in the list
        bmi_details.append((bmi,category,healthrisk))
    return bmi_details
def count_overweight_persons(bmi_details): #returns count of overweight persons
    total_count=list(filter(lambda bmi:bmi[1]=='Overweight',bmi_details))
    return len(total_count)

    
