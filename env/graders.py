from env.graders import grade_task_easy, grade_task_medium, grade_task_hard

def get_tasks():
    return [
        {
            "id": "task_easy",
            "description": "Classify emails",
            "grader": grade_task_easy,
        },
        {
            "id": "task_medium",
            "description": "Classify + prioritize emails",
            "grader": grade_task_medium,
        },
        {
            "id": "task_hard",
            "description": "Full email handling",
            "grader": grade_task_hard,
        }
    ]