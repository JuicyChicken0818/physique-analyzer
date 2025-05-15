# Physique Analyzer 🏋️‍♂️

A computer vision–based tool that analyzes physique proportions from a full-body image using Python and MediaPipe.  
It compares your ratios to a target physique and gives customized training feedback based on key proportional imbalances.

---

## 🔍 What It Does

- Detects body keypoints using MediaPipe Pose
- Computes 5 meaningful ratios:
  - `shoulderToWaist`
  - `armToTorso`
  - `legToTorso`
  - `upperToLowerArm`
  - `leftVsRightArm`
- Compares your ratios to a goal physique
- Suggests what to train (e.g. shoulders, arms) to improve balance

---

## 🚀 How to Run

1. Clone the repo  
2. Create a virtual environment  
3. Install requirements:
   ```bash
   pip install -r requirements.txt
4. Add a full-body photo to the images/ folder (Ex: user1.jpg)
5. Run:
    python main.py

---

## 🧠 Tech Stack

- Python 3.11

- MediaPipe

- OpenCV

- NumPy

---

## 📁 Project Structure

```bash
physique-analyzer/
├── images/               # Input images
├── main.py               # Runs the analysis
├── physique_metrics.py   # Extracts pose and calculates ratios
├── recommendations.py    # Generates training advice
├── requirements.txt
└── README.md

---

## ⚠️ Notes

- Use clear, front-facing or side-profile full-body images for best results

- Ratios are length-based and serve as visual proportion cues, not measurements of muscle mass

---

## 📌 Future Plans

- Add Streamlit web interface

- Enable side-by-side physique comparisons

- Visual overlays to highlight weak points

- Research DenseBody to work with 3-D modeling

---

## 🙋‍♂️ Author
Joseph Zou
GitHub: @JuicyChicken0818