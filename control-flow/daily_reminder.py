task = str(input("Describe your task for today: "))
priority = str(input("Set the priority (high/medium/low): ")).lower()
time_bound = str(input("Is this task time-bound? (yes/no): ")).lower()
match priority:
    case "high":
        print(f"Remember: {task} is a high priority task. Make sure to complete it today!")
    case "medium":
        print(f"Remember: {task} is a medium priority task. Try to complete it soon.")
    case "low":
        print(f"Remember: {task} is a low priority task. You can take your time with this one.")
if time_bound == "yes":
    print(f"Remember to complete your {task}. It's high priority!")