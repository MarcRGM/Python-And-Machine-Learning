import cv2 # webcam
import mediapipe as mp # Detects hand and gives it Landmark
import csv # writes to a .csv file

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Hand detection
hands = mp_hands.Hands(
    static_image_mode=False, # Track hands across frames
    max_num_hands=1, # detects 1 hand
    min_detection_confidence=0.5, # 50% hand detection
    min_tracking_confidence=0.5 # 50% tracking between frames
)

# Opens the webcam
cap = cv2.VideoCapture(0) # open camera index 0 (Main camera)
# cap read frames from camera

def save_sample(label, points, filename="data/sign_data.csv"): 
    row = points + [label] # Row to save the points and the label
    with open(filename, mode="a", newline="") as csv_file:
        # Opens the file "data/sign_data.csv" in append mode
        # Gives the opened file object a variable name: csv_file
        writer = csv.writer(csv_file) # creates a writer for the file
        writer.writerow(row) # writes one row into the file
# Defines a function named save_sample
# It takes:
# label: "A", "B", etc
# points: list of 63 values
# 63 values describing the hand pose (21 landmarks * 3 coordinates each landmark)
# filename: where to save 

# Runs every frame
while True:
    success, frame = cap.read() # Tries to read one frame from the webcam
    # success is True if it got a frame, False if it failed
    # frame is a NumPy array representing the image
    if not success:
        break
    
    # Convert BGR (OpenCV) to RGB (MediaPipe)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB) 
    # OpenCV frames are in BGR (blue, green, red) order
    # MediaPipe expects RGB (red, green, blue)
    # cv2.cvtColor converts the frame from BGR to RGB and stores it in rgb

    result = hands.process(rgb) # passes the image to the MediaPipe model
    # It returns a result object like:
    # result.multi_hand_landmarks – list of detected hands, each with 21 landmarks

    points = [] # Always start empty each frame
    if result.multi_hand_landmarks: # If this is not empty, then at least one hand was detected
        for hand_landmarks in result.multi_hand_landmarks: # Loop over each detected hand
            # hand_landmarks is a structure with 21 points
            mp_drawing.draw_landmarks( # Drawing landmarks on the video
                frame, # what to draw on
                hand_landmarks, # which landmarks to draw
                mp_hands.HAND_CONNECTIONS # how the points are connected
            )

            # hand_landmarks.landmark is a list of 21 landmarks
            # each landmark contains x, y, and z coordinates
            # Example: 
            for lm in hand_landmarks.landmark:
                points.append(lm.x)
                points.append(lm.y)
                points.append(lm.z)

            print("Number of values:", len(points)) 
            # 21 landmarks * 3 coordinates each = 63 values

    
    # Shows the current frame in a window named "Collect Data - Press q to quit"
    cv2.imshow("Collect Data - Press ESC to quit", frame)

    key = cv2.waitKey(1) & 0xFF
    # cv2.waitKey(1) waits 1 millisecond for a key press
    # & 0xFF is a common OpenCV pattern to get the key code

    # Used for looping the keys
    label_map = {
        ord('a'): "A",
        ord('b'): "B",
        ord('c'): "C",
        ord('d'): "D",
        ord('e'): "E",
        ord('f'): "F",
        ord('g'): "G",
        ord('h'): "H",
        ord('i'): "I",
        ord('k'): "K",
        ord('l'): "L",
        ord('m'): "M",
        ord('n'): "N",
        ord('o'): "O",
        ord('p'): "P",
        ord('q'): "Q",
        ord('r'): "R",
        ord('s'): "S",
        ord('t'): "T",
        ord('u'): "U",
        ord('v'): "V",
        ord('w'): "W",
        ord('x'): "X",
        ord('y'): "Y",
        ord('0'): "0",
        ord('1'): "1",
        ord('2'): "2",
        ord('3'): "3",
        ord('4'): "4",
        ord('5'): "5",
        ord('6'): "6",
        ord('7'): "7",
        ord('8'): "8",
        ord('9'): "9"
    }

    if key == 27:
        break
    # 27 is the keycode for the ESC key
    # Pressing ESC will break the loop and the program goes to cleanup
    elif key in label_map and len(points) == 63: 
        # Checks if a known key is pressed and makes sure a valid hand vector with 63 values is detected
        label = label_map[key] # extracts the pressed key
        save_sample(label, points)
        # Call the save_sample function 
        # and saves the current 63 values plus the label of the Key
        print(f"Saved one '{label}' sample")
    else:
        print("No valid hand data to save")
    
    

cap.release() # closes the webcam
cv2.destroyAllWindows() # closes all OpenCV windows
hands.close() # releases resources used by MediaPipe
