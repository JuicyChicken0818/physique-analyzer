from physique_metrics import extractRatios
from recommendations import generateFeedback

# Load and analyze user's image
userRatios = extractRatios("images/user1.jpg")

# Define your goal ratios (adjust these if you have a goal image)
goalRatios = {
    "shoulderToWaist": 1.75,
    "armToTorso": 1.15,
    "legToTorso": 1.55,
    "upperToLowerArm": 1.1,
    "leftVsRightArm": 1.0
}

if userRatios:
    print("Your Body Ratios:")
    for key, val in userRatios.items():
        print(f"{key}: {val:.2f}")

    feedback = generateFeedback(userRatios, goalRatios)
    print("\n🧠 Training Feedback:")
    if feedback:
        for muscle, advice in feedback.items():
            print(f"- {advice}")
    else:
        print("✅ Your proportions already match the goal well!")
else:
    print("❌ Pose detection failed. Please try a clearer full-body image.")
