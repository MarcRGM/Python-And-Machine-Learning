import cv2 # Webcam + display
import mediapipe as mp # Hand landmark detection
import joblib # Load trained model (from train_model.py)
import numpy as np # Array handling for predictions

mp_hands = mp.solutions.hands # MediaPipe hand detection module
mp_drawing = mp.solutions.drawing_utils # Draws hand skeleton on screen

# Load both trained model for side-by-side comparison
rf_model = joblib.load("rf_model.pkl")  # Random Forest model (left side)
svm_model = joblib.load("svm_model.pkl")  # SVM model (right side)

# Hand detector (same as collect_data.py but max_num_hands=1 for single hand)
hands = mp_hands.Hands(
    static_image_mode=False, # Track hands across frames (video mode)
    max_num_hands=1, # Detect only 1 hand (simpler for static gestures)
    min_detection_confidence=0.5, # 50% confidence to detect hand
    min_tracking_confidence=0.5 # 50% confidence to track between frames
)

# Open webcam (index 0 = default camera)
cap = cv2.VideoCapture(0) # cap reads frames from camera

while True:
    # Read one frame from camera
    success, frame = cap.read() # success=True if frame captured, frame=NumPy image array
    if not success: # If camera fails
        break
        
    # Convert BGR→RGB (MediaPipe needs RGB, OpenCV gives BGR)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) # OpenCV=BGR, MediaPipe=RGB
    result = hands.process(rgb) # Detect hands → get 21 landmarks per hand
    
    # Reset points every frame
    points = [] # Always start empty each frame, will hold 63 x,y,z values
    
    if result.multi_hand_landmarks: # If hand detected (not empty):
        for hand_landmarks in result.multi_hand_landmarks: # Loop each detected hand
            # Draw skeleton on screen
            mp_drawing.draw_landmarks( # Drawing landmarks on the video
                frame, # what to draw on
                hand_landmarks, # which landmarks to draw (21 points)
                mp_hands.HAND_CONNECTIONS # how the points are connected
            )
            
            # Extract 63 values (21 landmarks × x,y,z)
            # hand_landmarks.landmark = list of 21 landmarks, each with x,y,z
            for lm in hand_landmarks.landmark: # Loop 21 landmarks
                points.extend([lm.x, lm.y, lm.z]) # Add x,y,z → 21×3=63 values
        
        # Predict if we have valid 63 values
        if len(points) == 63: # Exactly 21 landmarks detected
            features = np.array([points]).reshape(1, -1)
            # Format data as single sample:
            # models expect [[x1,y1,z1,x2,y2,z2...]] format
            
            rf_pred = rf_model.predict(features)[0]   
            # Random Forest analyzes hand pose, outputs predicted letter
            svm_pred = svm_model.predict(features)[0] 
            # SVM analyzes identical hand pose
            
            # Split frame into left (RF) and right (SVM)
            h, w = frame.shape[:2]
            left_frame = frame.copy()
            right_frame = frame.copy()
            
            # model-specific labels on each side
            cv2.putText(left_frame, f"RF: {rf_pred}", (50, 50), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
            cv2.putText(right_frame, f"SVM: {svm_pred}", (50, 50), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
            
            # combine frames horizontally for comparison
            dual_frame = np.hstack([left_frame, right_frame])
            cv2.imshow("RF (left) vs SVM (right) - ESC to quit", dual_frame)
            # Display dual-model live evaluation
        else:
            cv2.imshow("RF (left) vs SVM (right) - ESC to quit", frame)
            # Show regular camera feed when no hand detected

    # Show frame with landmarks + prediction
    cv2.imshow("Real-Time SignSpeak Demo - Press ESC to quit", frame) # Display window
    
    # ESC to quit
    key = cv2.waitKey(1) & 0xFF # Wait 1ms for keypress, &0xFF=OpenCV keycode pattern
    if key == 27: # 27=ESC keycode
        break # Pressing ESC breaks loop → cleanup

# Cleanup
cap.release() # Closes the webcam
cv2.destroyAllWindows() # Closes all OpenCV windows
hands.close() # Releases MediaPipe resources
