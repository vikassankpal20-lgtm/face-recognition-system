"""
Face Recognition System
-----------------------
A simple, accurate real-time face recognition application.

How to use:
1. Put photos of known people in the 'known_faces' folder
   (filename will be used as the person's name)
2. Run: python main.py
3. Press 'q' to quit
"""

import cv2
import face_recognition
import numpy as np
from utils.helpers import load_known_faces, get_face_locations_and_encodings


def main():
    print("=" * 50)
    print("      FACE RECOGNITION SYSTEM")
    print("=" * 50)
    print("Loading known faces...\n")

    # Load known faces
    known_face_encodings, known_face_names = load_known_faces("known_faces")

    if len(known_face_encodings) == 0:
        print("\n[IMPORTANT] No known faces found!")
        print("Please add clear face photos in the 'known_faces' folder.")
        print("Example: known_faces/vikas.jpg")
        print("\nThen run this program again.")
        return

    # Start webcam
    print("\nStarting webcam... Press 'q' to quit.\n")
    video_capture = cv2.VideoCapture(0)

    if not video_capture.isOpened():
        print("[ERROR] Could not open webcam. Please check your camera.")
        return

    # Process every other frame for better performance
    process_this_frame = True
    face_locations = []
    face_names = []

    while True:
        ret, frame = video_capture.read()
        if not ret:
            print("[ERROR] Failed to grab frame from camera.")
            break

        # Resize frame for faster processing (1/4 size)
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        if process_this_frame:
            # Detect faces
            face_locations, face_encodings = get_face_locations_and_encodings(
                small_frame, model="hog"  # change to "cnn" for higher accuracy (slower)
            )

            face_names = []
            for face_encoding in face_encodings:
                # Compare with known faces
                matches = face_recognition.compare_faces(
                    known_face_encodings, face_encoding, tolerance=0.5
                )
                name = "Unknown"

                # Use the known face with the smallest distance
                face_distances = face_recognition.face_distance(
                    known_face_encodings, face_encoding
                )
                best_match_index = np.argmin(face_distances)

                if matches[best_match_index] and face_distances[best_match_index] < 0.5:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display results on the original frame size
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up since we scaled down the frame
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            color = (0, 255, 0) if name != "Unknown" else (0, 0, 255)
            cv2.rectangle(frame, (left, top), (right, bottom), color, 2)

            # Draw a label with the name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), color, cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.8, (255, 255, 255), 1)

        # Show the frame
        cv2.imshow("Face Recognition - Press 'q' to quit", frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    # Cleanup
    video_capture.release()
    cv2.destroyAllWindows()
    print("\nProgram closed. Thank you!")


if __name__ == "__main__":
    main()
