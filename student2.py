import sys

if len(sys_argv) == 3:
  script_name = sys.argv[0]
  name = sys_argv[1]
  rollno = sys.argv[2]
  print("enter provided input values:")
else :
  script_name = sys.argv[0]
  namec = "srushti"
  rollno = "260"
  print("no input given - using default values:")

print("script name:", script_name)
print("student name:",name)
print("roll number:",rollno)
