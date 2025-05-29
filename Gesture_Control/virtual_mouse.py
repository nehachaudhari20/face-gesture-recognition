''' 
Virtual Mouse Control using Hand Gestures

Move cursor with hand movement
Left-click using thumb + index finger pinch
Scroll using finger gestures (optional/advanced)
'''
import cv2
import mediapipe as mp
import pyautogui
import numpy as np

cap = cv2.VideoCapture(0)
cap.set(3, 1280)  #width
cap.set(4, 720)   #height

mpHands = mp.solutions.hands
hands = mpHands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

screen_w, screen_h = pyautogui.size()

while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)


    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            lmList = []
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
            
            # Index Finger Tip = lmList[8], Thumb Tip = lmList[4]
            if len(lmList) > 9:
                x1, y1 = lmList[8][0], lmList[8][1]   # Index tip
                x2, y2 = lmList[4][0], lmList[4][1]   # Thumb tip

                # Move cursor
                screen_x = np.interp(x1, (0, 640), (0, screen_w))
                screen_y = np.interp(y1, (0, 480), (0, screen_h))
                pyautogui.moveTo(screen_x, screen_y)

                 #distance between thumb and index (hypotenuse)
                dist = np.hypot(x2 - x1, y2 - y1)
                if dist < 30:
                    pyautogui.click()
                    pyautogui.sleep(0.2)

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.imshow("Virtual Mouse", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
