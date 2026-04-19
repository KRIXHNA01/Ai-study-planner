import json

# Function to take subjects
def get_subjects():
    subjects = input("Enter subjects (comma separated): ").lower().split(",")
    return [s.strip() for s in subjects]

# Function to assign priority
def get_priorities(subjects):
    priorities = {}
    print("\nGive priority (1 = high, 2 = medium, 3 = low)\n")

    for sub in subjects:
        p = int(input(f"Priority for {sub}: "))
        priorities[sub] = p

    return priorities

# Function to create study plan
def create_plan(subjects, priorities, total_hours):
    plan = {}
    total_weight = sum([4 - p for p in priorities.values()])

    for sub in subjects:
        weight = (4 - priorities[sub]) / total_weight
        plan[sub] = round(weight * total_hours, 2)

    return plan

# Function to display plan
def show_plan(plan):
    print("\n===== SMART STUDY PLAN =====")
    for sub, hrs in plan.items():
        print(f"{sub.upper()} → {hrs} hrs/day")

# Function to save plan
def save_plan(plan):
    with open("study_plan.json", "w") as f:
        json.dump(plan, f)
    print("💾 Study plan saved!")

# Function to track progress
def track_progress(plan):
    print("\n===== PROGRESS TRACKING =====")
    progress = {}

    for sub in plan:
        done = float(input(f"Hours studied for {sub}: "))
        progress[sub] = done

    return progress

# Function to predict performance
def predict_performance(progress):
    avg = sum(progress.values()) / len(progress)

    print("\n===== PERFORMANCE ANALYSIS =====")
    if avg >= 4:
     print("✅ Good performance expected")
    elif avg >= 2:
     print("⚠️ Average performance, can improve")
    else:
     print("❌ Needs improvement, increase study time")

# MAIN PROGRAM
subjects = get_subjects()
total_hours = int(input("Enter total study hours per day: "))
priorities = get_priorities(subjects)

plan = create_plan(subjects, priorities, total_hours)
show_plan(plan)

save_plan(plan)

progress = track_progress(plan)
predict_performance(progress)