dict1={"Mat":123,"John":456}

#get value from key Mat
print(dict1["Mat"])

#change the value of key Mat
dict1["Mat"] = 456
print(dict1["Mat"])

#add new pair key:value
dict1["Kim"] = 789

dict2 = {
    "Mia": "nguyenminhnga",
    "Adam": "daiduong"
}

dict2["Kimmi"] = "kimirakoinen"
print(dict2)
dict2["Kimmi"] = "rajoinen"
print(dict2)

if "Mat" in dict1:
    print(dict1["Mat"])

for key in dict1:
    print(key)
for key in dict2:
    print(dict2[key])