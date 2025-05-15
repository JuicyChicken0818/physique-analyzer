def generateFeedback(userRatios, goalRatios, threshold=0.1):

    # Define what each ratio maps to in terms of training
    ratioToMuscle = {
        "shoulderToWaist": "shoulders",
        "armToTorso": "arms",
        "legToTorso": "legs"
    }

    trainingAdvice = {
        "shoulders": "Add lateral raises, overhead press, and rear delt flys",
        "arms": "Increase volume on biceps and triceps (curls, extensions)",
        "legs": "Focus on squats, leg press, and hamstring curls"
    }

    feedback = {}

    for key in userRatios:
        userVal = userRatios.get(key)
        goalVal = goalRatios.get(key)

        if userVal is None or goalVal is None:
            continue  # skip if either value is missing

        # Calculate proportional difference
        gap = (goalVal - userVal) / goalVal

        if gap > threshold:
            muscle = ratioToMuscle.get(key)
            suggestion = trainingAdvice.get(muscle, "Add more volume to this area.")
            feedback[muscle] = f"{muscle.capitalize()} lagging by {gap:.0%}. {suggestion}"

    return feedback
