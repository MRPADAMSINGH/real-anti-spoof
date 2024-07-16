# real_anti_spoof/streaming.py

import cv2
import numpy as np
from real_anti_spoof.spoofmodels.FasNet import FasNet

def main():
    # Initialize the FasNet model
    model = FasNet()

    # Open a video capture object
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Preprocess the frame for the model
        input_frame = preprocess_frame(frame)

        # Run the anti-spoofing model
        spoofing_score = model.predict(input_frame)

        # Display the result
        display_frame = postprocess_frame(frame, spoofing_score)
        cv2.imshow('Anti-Spoofing', display_frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the video capture object and close windows
    cap.release()
    cv2.destroyAllWindows()

def preprocess_frame(frame):
    # Resize, normalize, and any other preprocessing steps
    return frame

def postprocess_frame(frame, score):
    # Overlay the score on the frame
    cv2.putText(frame, f'Spoofing Score: {score}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    return frame

if __name__ == '__main__':
    main()
