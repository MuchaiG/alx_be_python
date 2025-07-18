task = str(input("Enter your task: "))
priority = str(input("Priority (high/medium/low): ")).lower()
time_bound = str(input("Is it time-bound? (yes/no): ")).lower()
match priority:
    case "high":
        print(f"Reminder: {task} is a high priority task. Make sure to complete it today!")
    case "medium":
        print(f"Reminder: {task} is a medium priority task. Try to complete it soon.")
    case "low":
        print(f"Reminder: {task} is a low priority task. You can take your time with this one.")
if time_bound == "yes":
    print(f"Reminder: {task} is time-bound. Make sure to complete it on time!")