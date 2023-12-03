import cv2

# Load the cascade file for detecting faces
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


# Open the default camera
cap = cv2.VideoCapture(0)

# Loop until the user presses 'q'
while True:
    # Read the frame from the camera
    _, img = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Look for faces in the image using the loaded cascade file
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Draw a rectangle around every found face
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

    # Show the result on the screen
    cv2.imshow('Video', img)

    # Check if the user pressed 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera
cap.release()