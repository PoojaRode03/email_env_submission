def grade_task_easy(pred, gt):
    if not pred or not gt:
        return 0.5
    pred = pred if isinstance(pred, list) else [pred]
    gt = gt if isinstance(gt, list) else [gt]
    correct = sum(p == g for p, g in zip(pred, gt))
    return max(0.01, min(0.99, correct / max(len(gt), 1)))


def grade_task_medium(pred, gt):
    if not pred or not gt:
        return 0.5
    pred = pred if isinstance(pred, list) else [pred]
    gt = gt if isinstance(gt, list) else [gt]
    correct = sum(p == g for p, g in zip(pred, gt))
    return max(0.01, min(0.99, correct / max(len(gt), 1)))


def grade_task_hard(pred, gt):
    if not pred or not gt:
        return 0.5
    pred = pred if isinstance(pred, list) else [pred]
    gt = gt if isinstance(gt, list) else [gt]
    correct = sum(p == g for p, g in zip(pred, gt))
    return max(0.01, min(0.99, correct / max(len(gt), 1)))


def get_tasks():
    return [
        {"id": "task_easy", "description": "Classify emails", "grader": grade_task_easy},
        {"id": "task_medium", "description": "Classify + prioritize emails", "grader": grade_task_medium},
        {"id": "task_hard", "description": "Full email handling", "grader": grade_task_hard},
    ]