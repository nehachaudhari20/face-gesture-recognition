from deepface import DeepFace
import os

KNOWN_FACES_DIR = os.path.abspath("known_users")

def verify_face(captured_image_path, known_faces_dir=KNOWN_FACES_DIR):
    if not os.path.exists(known_faces_dir):
        print(f"Error: Known faces directory '{known_faces_dir}' does not exist.")
        return False
    if not os.path.isfile(captured_image_path):
        print(f"Error: Image file '{captured_image_path}' does not exist.")
        return False
    

    for user_img in os.listdir(known_faces_dir):
        user_path = os.path.join(known_faces_dir, user_img)

        if not user_img.lower().endswith((".jpg", ".png", ".jpeg")):
            continue

        try:
            result = DeepFace.verify(
                img1_path=captured_image_path,
                img2_path=user_path,
                enforce_detection=True,
                model_name="Facenet",
                detector_backend="retinaface"
            )

            if result["verified"]:
                print("Face verified successfully!")
                return True 
        except Exception as e:
            print(f"Error occurred: {e}")
    
    print("Face verification failed.")
    return None

if __name__ == "__main__":
    verify_face("C:/Users/DELL/Desktop/Summer Term/Face-gesture/captured_face.jpg")