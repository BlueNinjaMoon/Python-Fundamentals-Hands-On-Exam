#Christian Lehman

studentid = input("Enter your Student ID: ").upper().strip()
studentid1 = studentid[0:2]
studentid2 = studentid[2:9]

if len(studentid) == 8:
     print("Valid ID length.")
else:
     print("Invalid ID - ID length must be exactly 8 characters.")
if studentid1.isalpha() == True:
     print("Valid first 2 characters.")
else:
     print("Invalid ID -  First 2 characters must be letters.")
if studentid2.isdigit() == True:
     print("Valid last 6 characters.")
else:
     print("Invalid ID - Last 6 characters must be numbers.")
print(f"Valid ID    Masked ID: {studentid1}****{studentid2[4:8]}")