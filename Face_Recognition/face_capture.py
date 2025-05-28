import cv2

def capture_face(save_path="captured_face.jpg"):
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Error: Could not open camera.")
        return
    
    print("Press 'c' to captured face and 'q' to quit.")
    while True:
        ret, frame = cam.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        cv2.imshow("Face Capture", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == ord('c'):
            cv2.imwrite(save_path, frame)
            print(f"Face captured and saved to {save_path}")
        elif key == ord('q'):
            print("Quitting face capture.")
            break
    
    cam.release()
    cv2.destroyAllWindows()
    return save_path

if __name__ == "__main__":
    capture_face()
