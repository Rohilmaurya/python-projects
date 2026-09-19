from datetime import date, timedelta

sessions = []


def start_study_session():
    subject = input("Enter the subject you are studying: ")
    topic = input("Enter the topic you are focusing on: ")
    duration = input("Enter the duration of your study session (in minutes): ")
    session_date = input("Enter the date of the study session (YYYY-MM-DD): ")

    session = {
        "subject": subject,
        "topic": topic,
        "duration": duration,
        "date": session_date
    }

    sessions.append(session)
    print("Session recorded successfully!")


def view_study_history():
    print("Study Session History:")

    if sessions:
        for session in sessions:
            print(
                "Date: " + session["date"]
                + ", Subject: " + session["subject"]
                + ", Topic: " + session["topic"]
                + ", Duration: " + session["duration"]
                + " minutes"
            )
    else:
        print("No study sessions recorded.")


def view_today_summary():
    today = date.today().strftime("%Y-%m-%d")
    today_sessions = []

    for session in sessions:
        if session["date"] == today:
            today_sessions.append(session)

    print("Today's Study Summary:")

    if today_sessions:
        for session in today_sessions:
            print(
                "Subject: " + session["subject"]
                + ", Topic: " + session["topic"]
                + ", Duration: " + session["duration"]
                + " minutes"
            )
    else:
        print("No study sessions recorded for today.")


def view_weekly_summary():
    weekly_sessions = []

    today = date.today()
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)

    for session in sessions:
        session_date = date.fromisoformat(session["date"])

        if start_of_week <= session_date <= end_of_week:
            weekly_sessions.append(session)

    print("Weekly Study Summary:")

    if weekly_sessions:
        for session in weekly_sessions:
            print(
                "Date: " + session["date"]
                + ", Subject: " + session["subject"]
                + ", Topic: " + session["topic"]
                + ", Duration: " + session["duration"]
                + " minutes"
            )
    else:
        print("No study sessions recorded for this week.")


print("===============================")
print("Welcome to Study Session Tracker!")
print("===============================")
print("This program will help you track your study sessions and provide insights into your study habits.")

while True:
    print(
        "1. Start a new study session\n"
        "2. View all study session history\n"
        "3. Today's study summary\n"
        "4. Weekly study summary\n"
        "5. Exit"
    )

    option = input("Please select an option (1-5): ")

    if option == "1":
        start_study_session()

    elif option == "2":
        view_study_history()

    elif option == "3":
        view_today_summary()

    elif option == "4":
        view_weekly_summary()

    elif option == "5":
        print("Exiting the program. Happy studying!")
        break

    else:
        print("Invalid option. Please select a number from 1 to 5.")
