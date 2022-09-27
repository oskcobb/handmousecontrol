import cv2
import mediapipe as mp
import mouse
import keyboard
import math

#cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
#cap = cv2.resize(capt, (960, 540)) 
mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
#pyautogui.FAILSAFE = False

def off():
    while True:
        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("c"):
            exit()
        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("f1"):
            vid()
        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("f2"):
            novid()
        print('off')
    
            

def vid():
    while True:
        success, image = cap.read()
        imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(imageRGB)
        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("c"):
            exit()
        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("f1"):
            novid()
        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("f2"):
            off()
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks: # working with each hand
                for id, lm in enumerate(handLms.landmark):
                    #print(id)
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    if id == 0 :
                        mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
                        x = cx - 900
                        print("")
                        print("x")
                        print(cx)
                        print("")
                        y = cy - 50
                        print("")
                        print("y")
                        print(y)
                        print("")
                        if x >= 0:
                            x = -abs(x)
                        else:
                            x = abs(x)
                        mouse.move(x, y)
        cv2.imshow("Output", image)
        cv2.waitKey(1)

def novid():
    while True:
        cv2.destroyAllWindows()
        success, image = cap.read()
        imageRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        results = hands.process(imageRGB)
        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("c"):
            exit()
        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("f1"):
            vid()
        if keyboard.is_pressed("ctrl") and keyboard.is_pressed("f2"):
            off()
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks: # working with each hand
                for id, lm in enumerate(handLms.landmark):
                    #print(id)
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    if id == 0 :
                        mpDraw.draw_landmarks(image, handLms, mpHands.HAND_CONNECTIONS)
                        x = cx - 900
                        print("")
                        print("x")
                        print(cx)
                        print("")
                        y = cy - 50
                        print("")
                        print("y")
                        print(y)
                        print("")
                        if x >= 0:
                            x = -abs(x)     
                        else:
                            x = abs(x)
                        mouse.move(x, y)
                        #pyautogui.moveTo(cx, y, duration = 0)
                        #print(pyautogui.position())
                    try:
                        h, w, c = image.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        if id == 4:
                            h, w, c = image.shape
                            cx, cy = int(lm.x * w), int(lm.y * h)
                            y1 = cy
                            
                            #print(x1)
                        if id == 8:
                            h, w, c = image.shape
                            cx, cy = int(lm.x * w), int(lm.y * h)
                            y2 = cy
                        i = math.isclose(y1, y2, abs_tol = 20.0)
                        if i == True:
                            mouse.click("left")
                    except NameError:
                        print()
                    try:
                        h, w, c = image.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        if id == 4:
                            h, w, c = image.shape
                            cx, cy = int(lm.x * w), int(lm.y * h)
                            y3 = cy
                            print(x1)
                        if id == 12:
                            h, w, c = image.shape
                            cx, cy = int(lm.x * w), int(lm.y * h)
                            y4 = cy
                        i = math.isclose(y3, y4, abs_tol = 20.0)
                        if i == True:
                            mouse.click("right")
                    except NameError:
                        print()
                    try:
                        h, w, c = image.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        if id == 4:
                            h, w, c = image.shape
                            cx, cy = int(lm.x * w), int(lm.y * h)
                            y5 = cy
                            print(x1)
                        if id == 5:
                            h, w, c = image.shape
                            cx, cy = int(lm.x * w), int(lm.y * h)
                            y6 = cy
                        i = math.isclose(y5, y6, abs_tol = 20.0)
                        """
                        if i == True:
                            z = mouse.get_position()
                            xf = mouse.get_position()
                            if z >= xf:
                                mouse.wheel(-1)
                                z = mouse.get_position()
                                xf = mouse.get_position()
                            elif z <= xf:
                                mouse.wheel(1)
                                z = mouse.get_position()
                                xf = mouse.get_position()
                                """
                    except NameError:
                        print()
                    
        #cv2.imshow("Output" image)
        #cv2.waitKey(1)

novid()