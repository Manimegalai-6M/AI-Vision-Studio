def update_progress(targets, detected):

    completed = []

    remaining = []

    detected = [obj.lower() for obj in detected]

    for target in targets:

        if target.lower() in detected:
            completed.append(target)
        else:
            remaining.append(target)

    score = len(completed) * 20

    return {
        "completed": completed,
        "remaining": remaining,
        "score": score
    }