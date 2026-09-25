student=[]

print("Welcome to the Student Data Organizer!")

while True:

   print("\nSelect an option:")
   print("1. Add Student")
   print("2. Display all Students")
   print("3. Update Student Information")
   print("4. Delete Student")
   print("5. Display Subjects Offered")
   print("6. Exit")

   choice=int(input("\nEnter your choice:"))

   if choice == 1:
      print("Enter Student Details:") 
      sid=int(input("Enter Student Id:"))
      sname=input("Enter Student Name:")
      sage=int(input("Enter Age:"))
      sgrade=input("Enter Grade:")
      sdob = input("Enter Date of Birth (YYYY-MM-DD):")
      ssubject=input("Enter subject (Comma separated):")
      sub={sub.strip() for sub in ssubject.split(",") if sub.strip()}
      #sub=set(ssubject.split(","))

      students={
         "id":(sid,),
         "name":sname,
         "age":sage,
         "grade":sgrade,
         "dob":(sdob,),
         "subject":sub
      }
      student.append(students)
      print(f"\nStudent {sname} Added Successfully!")
   

   elif choice == 2:
      if len(student) == 0:
         print("Student Not Found") 
      else:
         for stu in student:
            print(f"Student Id: {stu['id']} | Name: {stu['name']} | Age: {stu['age']} | Grade: {stu['grade']} | Subject: {stu['subject']}")

   elif choice == 3:
      sid=int(input("Enter Student Id:"))
      found = False
      for stu in student:
         
         if (sid,)==stu['id']:
            stu["age"] = input("Enter New Age: ")
            stu["subject"] = input("Enter New Subjects: ")
            print(f"Student id {stu['id']}`s Age and Subjects Updated Successfully")
            found = True
            break

      if found == False:
         print("Student Not Found")  

   elif choice == 4:

      sid=int(input("Enter Student Id:"))
      found = False
      for i in range(len(student)):
         if student[i]["id"] == (sid,):
            del student[i]         
            print("Student Deleted Successfully!")
            found = True
            break
      if found == False:
         print("Student Not Found")  


   elif choice == 5:
      #all_subjects=set()
      for stu in student:
         print(stu['subject'])
        

         #all_subjects.update(stu['subject'])
         #print(f"Subjects Offered: {(all_subjects)}")      

   elif choice == 6:
      print("Thank You For Using Student Data Organizer!")
      break

   else:
      print("Invalid Choice.") 