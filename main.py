from motion_detection import MotionDetector
from send_email import send_email

# Initialize motion detector
detector = MotionDetector(video_path="Test Videos/thief_video2.mp4")
detector.detect_motion()  # ✅ Correct method

# Send the last captured image
latest_image = "Captured/latest_detected.jpg"  # Modify this to dynamically get the latest image
send_email(latest_image)
