#1
file = open("clients.txt", "r")
file2 = open("spain_german.txt", "w")
email_file = []
countries = set()
for line in file:
    p = line.strip().split(";")
    name = p[0]
    email = p[1]
    country = p[2]
    year = p[3].split("/")[-1]
    if country == "Spain" or country == "Germany":
        file2.write(name + "\n")
    if year == "2011":
        email_file.append(email)
    countries.add(country)
print(email_file)
print(countries)
file.close()
file2.close()