#Program To Calculate Percentage of a student
name = input("Enter Your Name:  ")
maths = int(input("Enter Your Maths Marks [out of 100] :  "))
english = int(input("Enter Your English Marks [out of 100] :  "))
sst = int(input("Enter Your Marks SST [out of 100] :  "))
hindi = int(input("Enter Your Marks Hindi [out of 100] :  "))
science = int(input("Enter Your Marks Science [out of 100] :  "))

sum = maths + english + sst + hindi + science
print("Total Marks -> ",sum ,"/ 500")

percentage = (sum/500)*100
print("Percentage -> ",percentage,"%")
if percentage>=95:
    print("Grade => A+")
elif percentage>=90:
    print("Grade => A")
elif percentage>=75:
    print("Grade => B")
elif percentage>=50:
    print("Grade => C")
elif percentage>=30:
    print("Grade => D")
elif percentage<30:
    print("Grade => F")

print(name,"Secured",percentage,"%","by scoring",sum,"out of 500.")


