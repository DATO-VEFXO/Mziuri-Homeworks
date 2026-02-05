file = open("titanic.txt","r")
for line in file:
    p = line.strip().split(",")
    ticket = p[2]
    gender = p[5]
    genderf = gender
    genderm = gender
    survive = p[1]
    survivef = survive
    survivem = survive
    ticket1 = ticket
    ticket2 = ticket
    ticket3 = ticket
    if genderf == "female":
        genderf = int(genderf)
        genderf = genderf * 100 / sum(gender)
        print("female gender",genderf,"%")
    if gender == "male":
        genderm = int(genderm)
        genderm = genderm * 100 / sum(gender)
        print("male gender",genderm,"%")
    if gender == "female" and survivef == "0":
        survivef = int(survivef)
        survivef = survivef * 100 / sum(survive)
        print(survivef)
    if gender == "female" and survivef == "1":
        survivef = survivef * 100 / sum(survive)
        print(survivef)
    if gender == "male" and survivem == "0":
        survivem = int(survivem)
        survivem = survivem * 100 / sum(survive)
        print(survivem)
    if gender == "male" and survivem == "1":
        survivem = survivem * 100 / sum(survive)
        print(survivem)
    if ticket1 == "1":
        ticket1 = int(ticket1)
        ticket1 = ticket1 * 100 / sum(ticket)
        print(ticket1,"%")
    if ticket2 == "2":
        ticket2 = int(ticket2)
        ticket2 = ticket2 * 100 / sum(ticket)
    if ticket3 == "3":
        ticket3 = int(ticket3)
        ticket3 = ticket3 * 100 / sum(ticket)
dict = {
}
dict1 = {}

#1 read write append
#2tavisit sheqmnis
#3tuplis monacemebis shecvla ar shegvizlia xolo listis ki
#4key




