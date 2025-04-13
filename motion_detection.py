import cv2
import numpy as np
import pygame
import os
import time
from datetime import datetime
from ultralytics import YOLO  # ✅ Use YOLOv8 for better performance
from threading import Thread  # ✅ Multi-threading for real-time speed
from send_email import send_email  # ✅ Import email module

class MotionDetector:
    def __init__(self, video_path):
        self.video_path = video_path
        self.cap = cv2.VideoCapture(video_path)

        # ✅ Set Video Properties for Faster Playback
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 2)  # ✅ Reduce buffer size
        self.cap.set(cv2.CAP_PROP_FPS, 30)  # ✅ Ensure max FPS
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"XVID"))  # ✅ Optimize codec

        # ✅ Load YOLOv8 Model (Faster than YOLOv5)
        self.model = YOLO("yolov8s.pt")  # ✅ Smallest YOLOv8 model for speed

        # ✅ Define Target Classes
        self.target_classes = ['person']

        # ✅ Pygame for Alarm Sound
        pygame.init()
        self.alarm_path = "Alarm/alarm.wav"
        pygame.mixer.music.load(self.alarm_path)

        # ✅ Variables
        self.pts = []  # Polygon points
        self.save_folder = None
        self.count = 0  # Counter for saving images
        self.number_of_photos = 3
        self.frame_skip = 2  # ✅ Process every 2nd frame (adjust for smoothness)
        self.frame_count = 0

        # ✅ Open Video Window & Allow Drawing
        cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
        cv2.setMouseCallback("Video", self.draw_polygon)

    def draw_polygon(self, event, x, y, flags, param):
        """Allows user to draw ROI polygon"""
        if event == cv2.EVENT_LBUTTONDOWN:
            print(f"Point Added: ({x}, {y})")
            self.pts.append([x, y])
        elif event == cv2.EVENT_RBUTTONDOWN:
            print("ROI Reset!")
            self.pts = []

    def inside_polygon(self, point):
        """Check if a point is inside the drawn polygon"""
        if len(self.pts) < 3:
            return False
        return cv2.pointPolygonTest(np.array(self.pts), (point[0], point[1]), False) == 1

    def save_detected_images(self, frame, person_img):
        """Saves images of detected persons in structured folders"""
        if self.save_folder is None:
            timestamp = datetime.now().strftime("%Y-%m-%d_%I-%M%p")  # 12-hour format
            self.save_folder = f"Captured/{timestamp}"
            os.makedirs(f"{self.save_folder}/Full Frame", exist_ok=True)
            os.makedirs(f"{self.save_folder}/Person", exist_ok=True)

        frame_name = f"{self.save_folder}/Full Frame/frame_{int(time.time())}.jpg"
        person_name = f"{self.save_folder}/Person/person_{int(time.time())}.jpg"

        cv2.imwrite(frame_name, frame)
        cv2.imwrite(person_name, person_img)

        # ✅ Send email with both images in a separate thread
        Thread(target=send_email, args=(person_name, frame_name)).start()

    def detect_motion(self):
        """Main function to detect motion and trigger alerts"""
        while True:
            ret, frame = self.cap.read()
            if not ret:
                break

            # ✅ Skip frames for real-time speed
            self.frame_count += 1
            if self.frame_count % self.frame_skip != 0:
                continue  # Skip frames to maintain FPS

            frame_detected = frame.copy()
            results = self.model(frame, conf=0.4)  # ✅ Confidence threshold for detection

            person_detected = False

            # ✅ Create Overlay for Highlighting ROI
            overlay = frame.copy()
            if len(self.pts) >= 3:
                cv2.fillPoly(overlay, [np.array(self.pts)], (0, 255, 0))  # ✅ Fill ROI
                frame = cv2.addWeighted(overlay, 0.5, frame, 0.5, 0)  # ✅ Blend with transparency

            for detection in results[0].boxes.data:
                x1, y1, x2, y2, score, class_id = detection.tolist()
                if int(class_id) == 0:  # ✅ Class ID 0 is 'person' in YOLO
                    center_x, center_y = (int(x1) + int(x2)) // 2, (int(y1) + int(y2)) // 2

                    # ✅ Draw Bounding Box
                    cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (255, 255, 0), 2)
                    cv2.putText(frame, "Person", (int(x1), int(y1) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 0), 2)
                    cv2.circle(frame, (center_x, center_y), 5, (0, 0, 255), -1)

                    # ✅ Check if Person is Inside ROI
                    if len(self.pts) >= 3 and self.inside_polygon((center_x, center_y)):
                        person_detected = True
                        person_img = frame_detected[int(y1):int(y2), int(x1):int(x2)]

                        # ✅ Save Images
                        if self.count < self.number_of_photos:
                            self.save_detected_images(frame_detected, person_img)
                            self.count += 1

                        # ✅ Trigger Alarm
                        if not pygame.mixer.music.get_busy():
                            pygame.mixer.music.play()

                        # ✅ Mark Detection
                        cv2.putText(frame, "Person Detected!", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 0, 255), 2)

            # ✅ Show Video
            cv2.imshow("Video", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.cap.release()
        cv2.destroyAllWindows()
