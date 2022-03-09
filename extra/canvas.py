from canvasapi import Canvas

def printclass(canvas):
    coursenum = int(input("enter course number: "))
    course = canvas.get_course(coursenum)
    print(f"course: {course.name}")
    users = course.get_users()

    for user in users:
        print(f"users: {user}")

def userclasses(canvas):
    usernum = int(input("enter user number: "))
    user = canvas.get_user(usernum)
    print(f"name: {user.name}")
    courses = user.get_courses()
    for course in courses:
        print(f"course: {course}")

def main():
    # Initialize a new Canvas object
    URL = "school email here"
    TOKEN = "token here"
    canvas = Canvas(URL, TOKEN)
    flag = True
    while flag:
        choice = int(input("enter 1 for printclass or 2 for userlasses"))
        if choice == 1:
            printclass(canvas)
        elif choice == 2:
            userclasses(canvas)
        choice2 = str(input("continue?"))
        choice2.lower()
        if choice2 == "n" or choice2 == "no":
            flag = False
            
main()
