gender = input ("Enter biological gender (male/female): ")

#So sanh data.lower() == 'x' => X=x cover both cases

if  gender.lower() == 'male':
    hemo_value = float (input ("Enter hemoglobin value (g/l): ") )
    if 134 <= hemo_value <= 167:
        print("Your hemoglobin is normal.")
    elif hemo_value < 134:
        print("Your hemoglobin is low.")
    elif hemo_value >167:
        print("Your hemoglobin is high.")
elif gender.lower() == 'female':
    hemo_value = float (input ("Enter hemoglobin value (g/l): ") )
    if 117 <= hemo_value <= 155:
        print("Your hemoglobin is normal.")
    elif hemo_value < 117:
        print("Your hemoglobin is low.")
    elif hemo_value >155:
        print("Your hemoglobin is high.")

else:
    print("Invalid gender.")