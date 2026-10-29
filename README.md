# Face Recognition System

A simple, accurate, and easy-to-use **Real-Time Face Recognition** system built with Python.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## Features

- Real-time face recognition using webcam
- High accuracy using `face_recognition` library (powered by dlib)
- Easy to add new people (just drop photos in a folder)
- Clean and simple code structure
- Works offline

---

## Project Structure

```
face-recognition-system/
│
├── known_faces/          ← Put known people photos here
│   └── .gitkeep
│
├── test_images/          ← Optional test images
│   └── .gitkeep
│
├── utils/
│   └── helpers.py        ← Helper functions
│
├── main.py               ← Main application
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

### 1. Clone or Download this repository

```bash
git clone https://github.com/vikassankpal20-lgtm/face-recognition-system.git
cd face-recognition-system
```

### 2. Create virtual environment (Recommended)

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac / Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

> **Note:** Installing `dlib` and `face_recognition` may take a few minutes.  
> On Windows, if you face issues, install Visual C++ Build Tools or use pre-built wheels.

---

## How to Use

### Step 1: Add Known Faces

1. Go to the `known_faces` folder
2. Add clear front-facing photos of people
3. Name the file with the person's name

**Examples:**
```
known_faces/
├── vikas_sankpal.jpg
├── rahul.jpg
└── priya_sharma.png
```

> Tip: Use clear, well-lit photos with only one face per image for best results.

### Step 2: Run the Application

```bash
python main.py
```

### Step 3: Controls

- The webcam window will open
- Recognized faces will show the person's name in **green**
- Unknown faces will show **"Unknown"** in **red**
- Press **`q`** to quit

---

## Accuracy Tips

- Use high-quality, clear photos of known people
- Prefer front-facing photos with good lighting
- You can lower the `tolerance` value in `main.py` (default `0.5`) for stricter matching
- For higher accuracy (but slower), change `model="hog"` to `model="cnn"` in `main.py`

---

## Requirements

- Python 3.8 or higher
- Webcam
- Libraries listed in `requirements.txt`

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Webcam not opening | Check if another app is using the camera |
| No face detected | Improve lighting / use clearer photos |
| Installation error (dlib) | Install CMake and Visual Studio Build Tools (Windows) |
| Slow performance | Keep using `hog` model (default) |

---

## Author

**Vikas Sankpal**  
GitHub: [vikassankpal20-lgtm](https://github.com/vikassankpal20-lgtm)

---

## License

This project is open source and available under the [MIT License](LICENSE).
