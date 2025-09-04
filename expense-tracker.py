def temp(date):
 file=open("csv.txt",a)
 file.write(date)
 category=str(input("where you  spend the money (like on food, on bike)"))
 amount=str(input("how much you have spended on this="))
 note=str(input("plz enter a note for this expense or explain where you spended money"))
 file.write("\t\t\t\t\t"+category)
 file.write("\t\t\t\t\t\t\t"+amount)
 file.write("\t\t\t\t\t\t"+note)
 file.close()

print("welcome to the expense traacker app")
print("before starts this app eneter your necessary detaails")
date=str(input("enter the date of your expense "))
category=str(input("where you  spend the money (like on food, on bike)"))
amount=str(input("how much you have spended on this="))
note=str(input("plz enter a note for this expense or explain where you spended money"))
def saver():
 file=open("csv.txt","a")
 file.write("\n")
 file.write(date)
 file.write("\t\t\t\t\t"+category)
 file.write("\t\t\t\t\t\t\t"+amount)
 file.write("\t\t\t\t\t\t"+note)
 print("expense details added")
 useropinion=str(input(f"do you want to add more expenses for date {date}(type samedate) or wwant to add new day(type new) expesnse"))
 if(useropinion=="sameday"):
  temp(date)
 elif(useropinion=="new"):
  saver()

 file.close()
useropinion1=str(input("do you want total exxpense analysis(type yes or no)"))
if(useropinion1=="yes"):
 useropinion2=str(input("do you want total exxpense analysis for a day or week or month"))
 if(useropinion2=="day"):
  useropinion3=str(input("enter the date = "))
  
