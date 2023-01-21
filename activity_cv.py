import cv2
import time
from cv2 import WINDOW_FULLSCREEN
import numpy as np
from matplotlib import pyplot as plt

width = 1280
height = 720

class MediaPipe_Bodies:
    import mediapipe
    def __init__(self):
        self.pose = self.mediapipe.solutions.pose.Pose()
    
    def Marks(self, Frame):
        Landmarks = []
        frameRGB = cv2.cvtColor(Frame, cv2.COLOR_BGR2RGB)
        results = self.pose.process(frameRGB)
        if results.pose_landmarks != None:
            for lm in results.pose_landmarks.landmark:
                Landmarks.append((int(lm.x*width), int(lm.y*height)))
            return Landmarks

def run():
    evt, pntX1, pntY1, pntX2, pntY2 = 0, 0, 0, 0, 0

    def mouseClick(event, xPos, yPos, flags, params):
        nonlocal evt, pntX1, pntX2, pntY1, pntY2

        if event==cv2.EVENT_LBUTTONDOWN:
            pntX1 = xPos
            pntY1 = yPos
            evt = event
        if event==cv2.EVENT_LBUTTONUP: 
            pntX2 = xPos
            pntY2 = yPos
            evt = event
        
    Activity_Number_Graph = []
    Average_Time_Graph = []

    #DSHOW = Direct Show
    cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
    cap.set(cv2.CAP_PROP_FPS, 30)

    cv2.namedWindow('Shop Activity Analyzer', cv2.WINDOW_NORMAL)
    cv2.setMouseCallback('Shop Activity Analyzer', mouseClick)

    findPose = MediaPipe_Bodies()

    Font_Size = .5
    Font_Size_Small = .4
    Font_Thickness = 1
    Font_Title = cv2.FONT_HERSHEY_COMPLEX
    Font = cv2.FONT_HERSHEY_SIMPLEX
    LineThickness = 3
    weighted_color = (100, 0, 0)
    cnt = 0

    # Colours
    Red = (0, 0, 255)
    Green  = (0, 255, 0)
    Blue = (255, 0, 0)
    Cyan = (255, 255, 0)
    Purple = (255, 0, 255)
    Yellow = (0, 255, 255)
    White = (255, 255, 255)
    Black = (0, 0, 0)

    # Initialization 
    Start = False
    Roi_Created = False
    Roi_Activated = False
    Roi_Activity = False
    No_More_Click = False
    Location = ""
    Isle_Number = 0
    Activity = 0
    Activity_Start = 70
    Activity_Time = 0
    Last_Activity_Time = 0
    Total_Activity_Time = 0
    Activity_Number = 0
    Average_Time = 0
    Show_Average = 0
    Old_Time = 0
    Seconds_Elapsed = 0
    Minutes_Elapsed = 0
    Hours_Elapsed = 0

    while True:
        pressed_key = cv2.waitKey(1) & 0xFF

        Real_Time = time.localtime(time.time())
        Year = Real_Time[0]
        Month = Real_Time[1]
        Day = Real_Time[2]
        Hour = Real_Time[3]
        Minute = Real_Time[4]
        Second = Real_Time[5]

        # Frame Management
        _, frame = cap.read()
        cv2.rectangle(frame, (0, 0), (width, height), (255, 255, 255), 5)
        Gray_Frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        Was_Gray_Frame_First = cv2.cvtColor(Gray_Frame, cv2.COLOR_GRAY2BGR)
        Text_Background = np.zeros([height, width, 3], dtype = np.uint8)
        cv2.rectangle(Text_Background, (0, 0), (int(width*.18), height), (weighted_color), -1)

        # Generate Final Display
        Was_Grey_Frame = cv2.addWeighted(Was_Gray_Frame_First, .5, Text_Background, 1,1)
        
        # Intro Screen
        if Start == False:
            Roi = []
            Roi_Created = False
            Roi_Activated = False
            cv2.putText(Was_Grey_Frame, 'Shop Activity Analyzer!', (int(width * .01), int(height * .04)), Font_Title, Font_Size, Font_Thickness)
            cv2.putText(Was_Grey_Frame, 'Press S To Start!', (int(width * .01), int(height * .88)), Font_Title, Font_Size_Small, Font_Thickness)
            if pressed_key == ord('s'):
                Start = True

        # Setup Screen
        if Start == True and Roi_Activated == False:
            cv2.putText(Was_Grey_Frame, 'Please Select The', (int(width * .01), int(height * .04)), Font_Title, Font_Size, White, Font_Thickness)
            cv2.putText(Was_Grey_Frame, 'Region of Interest', (int(width * .01), int(height * .08)), Font_Title, Font_Size, White, Font_Thickness)
            if evt == 1:
                Roi_Created = False
            if evt == 4:
                Roi_Created = True
                Roi = frame[pntY1 : pntY2, pntX1 : pntX2]
                Was_Grey_Frame[pntY1:pntY2, pntX1:pntX2] = Roi
                cv2.rectangle(Was_Grey_Frame, (pntX1, pntY1), (pntX2, pntY2), (Green), LineThickness)

        # Get_Roi, Place in Display Frame :
        if Start == True and Roi_Created == True :
            if evt == 1:
                Start = False
            Roi = frame[pntY1:pntY2, pntX1:pntX2]
            Was_Grey_Frame[pntY1:pntY2, pntX1:pntX2] = Roi
        
        # Confirmation Screen:
        if Start == True and Roi_Created == True and Roi_Activated == False:
            cv2.putText(Was_Grey_Frame, "Press A to Activate", (int(width * .01), int(height * .12)), Font_Title, Font_Size_Small, White, Font_Thickness)
            Start_Year = Real_Time[0]
            Start_Month = Real_Time[1]
            Start_Day = Real_Time[2]
            Start_Hour = Real_Time[3]
            Start_Minute = Real_Time[4]
            Start_Second = Real_Time[5]
            if pressed_key == ord('a'):
                Roi_Activated = True
        
        # Working Screen
        if Start == True and Roi_Created == True and Roi_Activated == True:
            cv2.putText(Was_Grey_Frame, "Shop Activity Analyzer : ", (int(width * .01), int(height * .04)), Font_Title, Font_Size, White, Font_Thickness)
            cv2.putText(Was_Grey_Frame, "Details : ", (int(width * .01), int(height * .12)), Font_Title, Font_Size, White, Font_Thickness)
            cv2.putText(Was_Grey_Frame, "Time : ", (int(width * .01), int(height * .28)), Font_Title, Font_Size, White, Font_Thickness)
            cv2.putText(Was_Grey_Frame, "Start Date : "+str(Start_Day)+"-"+str(Start_Month)+"-"+str(Start_Year), (int(width * .01), int(height * .32)), Font_Title, Font_Size_Small, White, Font_Thickness)
            cv2.putText(Was_Grey_Frame, "Start Time : "+str(Start_Hour)+":"+str(Start_Minute)+":"+str(Start_Second), (int(width * .01), int(height * .36)), Font_Title, Font_Size_Small, White, Font_Thickness)
            cv2.putText(Was_Grey_Frame, "Current Date : "+str(Day)+"-"+str(Month)+"-"+str(Year), (int(width * .01), int(height * .40)), Font_Title, Font_Size_Small, White, Font_Thickness)
            cv2.putText(Was_Grey_Frame, "Current Time : "+str(Hour)+":"+str(Minute)+":"+str(Second), (int(width * .01), int(height * .44)), Font_Title, Font_Size_Small, White, Font_Thickness)

            # Elapsed Calculation:
            New_Time = Second
            if New_Time != Old_Time:
                Seconds_Elapsed = Seconds_Elapsed+1
                Old_Time = New_Time
            if Seconds_Elapsed == 60:
                Minutes_Elapsed = Minutes_Elapsed+1
                Seconds_Elapsed = 0
            if Minutes_Elapsed == 60:
                Hours_Elapsed = Hours_Elapsed+1
                Minutes_Elapsed = 0
            cv2.putText(Was_Grey_Frame, "Time Elapsed : "+str(Hours_Elapsed)+":"+str(Minutes_Elapsed)+":"+str(Seconds_Elapsed), (int(width * .01), int(height * .48)), Font_Title, Font_Size_Small, White, Font_Thickness)
            cv2.putText(Was_Grey_Frame, "Activity : ", (int(width * .01), int(height * .56)), Font_Title, Font_Size, White, Font_Thickness)
            cv2.putText(Was_Grey_Frame, "Activity Count : "+str(Activity_Number), (int(width * .01), int(height * .64)), Font_Title, Font_Size_Small, White, Font_Thickness)
            cv2.putText(Was_Grey_Frame, "Activity Timer (Secs) : "+str(Activity_Time), (int(width * .01), int(height * .68)), Font_Title, Font_Size_Small, White, Font_Thickness)
            cv2.putText(Was_Grey_Frame, "Last Activity Time (Secs) : "+str(Last_Activity_Time), (int(width * .01), int(height * .72)), Font_Title, Font_Size_Small, White, Font_Thickness)
            cv2.putText(Was_Grey_Frame, "Total Activity Time (Secs) : "+str(Total_Activity_Time), (int(width * .01), int(height * .76)), Font_Title, Font_Size_Small, White, Font_Thickness)
            cv2.putText(Was_Grey_Frame, "Average Activity Time (Secs) : "+str(Average_Time), (int(width * .01), int(height * .80)), Font_Title, Font_Size_Small, White, Font_Thickness)
            cv2.putText(Was_Grey_Frame, "Press R to Reset", (int(width * .01), int(height * .88)), Font_Title, Font_Size_Small, White, Font_Thickness)
        
            # Check For Bodies
            Bodies_Data = findPose.Marks(Roi)
            if Bodies_Data != None:
                cv2.putText(Was_Grey_Frame, "Status: ", (int(width * .01), int(height * .60)), Font, Font_Size_Small, White, Font_Thickness)
                cv2.putText(Was_Grey_Frame, "Activity ", (int(width * .05), int(height * .60)), Font_Title, Font_Size_Small, Red, Font_Thickness)
                cv2.rectangle(Was_Grey_Frame, (pntX1, pntY1), (pntX2, pntY2), (Red), LineThickness)
                if Activity == 0:
                    Activity_Number = Activity_Number + 1
                    Activity = 1
                if Activity_Start != Second:
                    Activity_Time = Activity_Time+1
                    Activity_Start = Second
            else:
                cv2.putText(Was_Grey_Frame, "Status: ", (int(width * .01), int(height * .60)), Font, Font_Size_Small, White, Font_Thickness)
                cv2.putText(Was_Grey_Frame, "No Activity ", (int(width * .05), int(height * .60)), Font, Font_Size_Small, White, Font_Thickness)
                cv2.rectangle(Was_Grey_Frame, (pntX1, pntY1), (pntX2, pntY2), (Green), LineThickness)
                Activity = 0
                if Activity_Time > 0:
                    Last_Activity_Time = Activity_Time
                    Total_Activity_Time = Total_Activity_Time + Activity_Time
                    Average_Time = int(Total_Activity_Time/Activity_Number)
                Activity_Time = 0

        # Reset To Start Screen
        if pressed_key == ord('r'):
            Roi = []
            Start = False
        
        # Quit Program
        cv2.putText(Was_Grey_Frame, "Press Q To Quit", (int(width * .01), int(height * .92)), Font_Title, Font_Size_Small, White, Font_Thickness)
        if pressed_key==ord('q'):
            break

        cv2.imshow('Shop Activity Analyzer', Was_Grey_Frame)
        cv2.moveWindow('Shop Activity Analyzer',0,0)
        Activity_Number_Graph.append(Activity_Number)
        Average_Time_Graph.append(Average_Time)
        cnt = cnt+1
        if(cnt > 100):
            Activity_Number_Graph.pop(0)
            Average_Time_Graph.pop(0)
    cap.release()

    return Average_Time_Graph, Activity_Number_Graph