from deepface import DeepFace
import os

def analyze_face(image_path):
    if not os.path.isfile(image_path):
        print(f"Error: Image file '{image_path}' does not exist.")
        return None
    
    try:
        analysis = DeepFace.analyze(
            img_path=image_path,
            actions = ["age", "gender", "emotion", "race"],
            detector_backend="mtcnn"
        )

        result = analysis[0] if isinstance(analysis, list) else analysis


        print(f"Age: {result['age']}")
        print(f"Gender: {result['gender']}")
        print(f"Emotion: {result['dominant_emotion']}")
        print(f"Race: {result['dominant_race']}")

        return result
    
    except Exception as e:
        print(f"Error occurred during face analysis: {e}")
        return None
    
if __name__ == "__main__":
    image_path = "C:/Users/DELL/Desktop/Summer Term/Face-gesture/captured_face.jpg"
    analyze_face(image_path)
