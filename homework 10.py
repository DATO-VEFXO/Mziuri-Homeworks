#1
file1 = open("f1", "r")
file2 = open("f2", "w")
for each in file1:
    a = int(each)
    file2.write(str(a * a) + "\n")
file1.close()
file2.close()
#2
file = open("oscars.txt", "r")
lines = file.readlines()
year_input = input("sheiyvanet weli ")
found = False
for line in lines:
    p = line.strip().split(",")
    year = p[0]
    name = p[3]
    if year == year_input:
        print("oskaris mflobeli", name)
        found = True
if not found:
    print("am wels aravis miugia oskari")
youngest_age = 100
youngest_name = ""
for line in lines:
    p = line.strip().split(",")
    age = int(p[2])
    name = p[3]
    if age < youngest_age:
        youngest_age = age
        youngest_name = name

print("yvelaze axalgazrda oskaris mflobeli", "- saxeli gvari ->", youngest_name, "- asaki -> ", youngest_age)
