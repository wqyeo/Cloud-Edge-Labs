#%% Reference: https://github.com/googlesamples/mediapipe/tree/main/examples/hand_landmarker/raspberry_pi
import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision

#%% Parameters
numHands = 2  # Number of hands to be detected
model = 'hand_landmarker.task'  # Model file
minHandDetectionConfidence = 0.5
minHandPresenceConfidence = 0.5
minTrackingConfidence = 0.5
frameWidth = 640
frameHeight = 480

# Visualization parameters
MARGIN = 10  # pixels
FONT_SIZE = 1
FONT_THICKNESS = 1
TEXT_COLOR = (0, 255, 0)  # Green for text
DOT_COLOR = (0, 0, 255)  # Red for landmarks
LINE_COLOR = (0, 255, 0)  # Green for connections

#%% Create HandLandmarker object.
base_options = python.BaseOptions(model_asset_path=model)
options = vision.HandLandmarkerOptions(
        base_options=base_options,        
        num_hands=numHands,
        min_hand_detection_confidence=minHandDetectionConfidence,
        min_hand_presence_confidence=minHandPresenceConfidence,
        min_tracking_confidence=minTrackingConfidence)
detector = vision.HandLandmarker.create_from_options(options)

# MediaPipe hand landmark connections
HAND_CONNECTIONS = mp.solutions.hands.HAND_CONNECTIONS

#%% Open CV Video Capture
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, frameWidth)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, frameHeight)

if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    try:
        ret, frame = cap.read() 
        frame = cv2.flip(frame, 1)  # Flip the image
        
        # Convert image to RGB
        rgb_image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Run hand landmarker
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_image)
        detection_result = detector.detect(mp_image)
        
        hand_landmarks_list = detection_result.hand_landmarks
        
        for hand_landmarks in hand_landmarks_list:
            points = []
            
            for landmark in hand_landmarks:
                x, y = int(landmark.x * frame.shape[1]), int(landmark.y * frame.shape[0])
                points.append((x, y))
                cv2.circle(frame, (x, y), 5, DOT_COLOR, -1)  # Draw red dots
            
            # Draw connections between landmarks
            for connection in HAND_CONNECTIONS:
                start_idx, end_idx = connection
                if start_idx < len(points) and end_idx < len(points):
                    cv2.line(frame, points[start_idx], points[end_idx], LINE_COLOR, 2)

            # Improved Finger Detection
            finger_tips = [4, 8, 12, 16, 20]
            finger_bases = [2, 6, 10, 14, 18]

            # Thumb detection (checks horizontal distance instead of vertical)
            thumb_tip_x, thumb_tip_y = points[4]
            thumb_joint_x, thumb_joint_y = points[3]
            thumb_base_x, thumb_base_y = points[2]

            thumb_extended = abs(thumb_tip_x - thumb_joint_x) > abs(thumb_base_x - thumb_joint_x)

            # Other fingers (use vertical position)
            finger_count = sum(points[tip][1] < points[base][1] for tip, base in zip(finger_tips[1:], finger_bases[1:]))

            # Include thumb if extended
            if thumb_extended:
                finger_count += 1

            # Display finger count
            cv2.putText(frame, f'Fingers: {finger_count}', (10, 50),
                        cv2.FONT_HERSHEY_DUPLEX, FONT_SIZE, TEXT_COLOR, FONT_THICKNESS, cv2.LINE_AA)

        cv2.imshow('Hand Tracking', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
   
    except KeyboardInterrupt:
        break

cap.release()
cv2.destroyAllWindows()
