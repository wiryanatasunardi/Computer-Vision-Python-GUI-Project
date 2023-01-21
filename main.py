import sys
from PyQt5.QtWidgets import QMainWindow, QLineEdit, QApplication, QStackedWidget
from PyQt5 import QtGui
from PyQt5.uic import loadUi
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import QTimer, QPropertyAnimation
from interface import Ui_MainWindow
import misc
import activity_cv
import cv2
import mediapipe as mp
import numpy as np
import pickle
import os.path

import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT
from matplotlib.figure import Figure

import firebase_admin
import pyrebase
from firebase_admin import credentials
from firebase_admin import firestore
import json
from datetime import datetime

""" Backend """
cred = credentials.Certificate(r"pyqt5-gui-firebase-adminsdk-rohct-d8177f166d.json")
with open(r"pyqt5-gui-pyrebase-config.json") as f:
    config = json.load(f)
with open(r"pyqt5-gui-firebase-db-options.json") as f:
    options = json.load(f)
    firebase_admin.initialize_app(cred, options)
auth = pyrebase.initialize_app(config).auth()
db = firestore.client()

#variabel global
gestNames = []
knownGestures = []
keyPoints = [0, 4, 5, 9, 13, 17, 8, 12, 16, 20]
width = 648
height = 432

class mpHands:
    def __init__(self, maxHands=2, modelComplexity = 1, tol1=0.5, tol2=0.5):
        self.hands=mp.solutions.hands.Hands(False, maxHands, modelComplexity, tol1, tol2)
            
    def Marks(self,frame):
        myHands=[]
        handsType=[]
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frameRGB)
        if results.multi_hand_landmarks != None:
            for handLandMarks in results.multi_hand_landmarks:
                myHand=[]
                for landmark in handLandMarks.landmark:
                    myHand.append((int(landmark.x*width), int(landmark.y*height)))
                myHands.append(myHand)
        return myHands

findHands = mpHands(1)
tol=10

""" GUI """
class Login(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs):
        super(Login, self).__init__(*args, **kwargs)
        loadUi("loginpage.ui", self)
        self.stackedWidget_welcome.setCurrentWidget(self.login_page)
        self.line_email_signup.returnPressed.connect(self.signup)
        self.line_pw_signup.returnPressed.connect(self.signup)
        self.line_confirm_pw.returnPressed.connect(self.signup)
        self.button_signup.clicked.connect(self.signup)
        self.to_login.clicked.connect(self.go_to_login)
        self.line_email.returnPressed.connect(self.login)
        self.line_pw.returnPressed.connect(self.login)
        self.button_login.clicked.connect(self.login)
        self.to_register.clicked.connect(self.go_to_signup)
        self.checkBox_login.stateChanged.connect(self.login_checkbox_click)
        self.checkBox_signup.stateChanged.connect(self.signup_checkbox_click)
    
    def login_checkbox_click(self):
        if self.checkBox_login.isChecked():
            self.line_pw.setEchoMode(QLineEdit.Normal)
        else:
            self.line_pw.setEchoMode(QLineEdit.Password)
    
    def signup_checkbox_click(self):
        if self.checkBox_signup.isChecked():
            self.line_pw_signup.setEchoMode(QLineEdit.Normal)
            self.line_confirm_pw.setEchoMode(QLineEdit.Normal)
        else:
            self.line_pw_signup.setEchoMode(QLineEdit.Password)
            self.line_confirm_pw.setEchoMode(QLineEdit.Password)
    
    def login(self):
        email = self.line_email.text()
        pw = self.line_pw.text()
        try:
            auth.sign_in_with_email_and_password(email, pw)
            self.line_email.clear()
            self.line_pw.clear()
            main_window = Window(email=email)
            widget.addWidget(main_window)
            widget.setCurrentIndex(1)
            self.label_confirm.setText("")
            self.label_confirm2.setText("")
        except:
            self.label_confirm2.setText("Login invalid!")
    
    def go_to_signup(self):
        self.stackedWidget_welcome.setCurrentWidget(self.register_page)
    
    def signup(self):
        email = self.line_email_signup.text()
        pw = self.line_pw_signup.text()
        confirm_pass = self.line_confirm_pw.text()
        if confirm_pass != pw :
            self.label_confirm.setText("Password does not match!")
        else:
            try:
                user = auth.create_user_with_email_and_password(email=email, password=pw)
                self.label_confirm.setText(misc.conf_msg.format(user['email']))
            except:
                self.label_confirm.setText("Sign up failed!")
            finally:
                self.line_email_signup.clear()
                self.line_pw_signup.clear()
                self.line_confirm_pw.clear()
    
    def go_to_login(self):
        self.stackedWidget_welcome.setCurrentWidget(self.login_page)
        self.line_email.clear()
        self.line_pw.clear()

class MplCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, email, parent=None):
        super().__init__(parent)
        loadUi("interface.ui", self)
        self.email = email
        self.stackedWidget_main.setCurrentWidget(self.page_home)
        self.canvas = MplCanvas()
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.graph_shop.addWidget(self.toolbar)
        self.graph_shop.addWidget(self.canvas)

        # notification msg setup
        self.notify(misc.welcome_message.format(self.email))

        # center menu
        self.center_menu.hide()

        # right menu
        self.right_menu.hide()

        # shop activity
        self.shop_start.clicked.connect(self.shop_start_onclick)

        # left menu stackedWidget signals
        self.button_sign.clicked.connect(self.button_sign_onclick)
        self.button_shop.clicked.connect(self.button_shop_onclick)
        self.button_pref.clicked.connect(self.button_pref_onclick)
        self.button_info.clicked.connect(self.button_info_onclick)
        self.button_help.clicked.connect(self.button_help_onclick)
        self.button_center_close.clicked.connect(self.button_center_close_onclick)
        self.MenuBtn.clicked.connect(self.menu_toggle)

        # top/right menu stackedWidget signals
        self.button_account.clicked.connect(self.button_account_onclick)
        self.button_more.clicked.connect(self.button_more_onclick)
        self.button_right_close.clicked.connect(self.button_right_close_onclick)
        self.button_notification.clicked.connect(self.button_notification_onclick)

        # right menu
        self.doc_ref = db.collection(u'activities')
        query = self.doc_ref.where("user", "==", self.email)
        self.signed_in_as.setText(misc.profile_msg.format(self.email))
        self.no_of_usage.setText(misc.usage_msg.format(len(query.get())))

        self.button_signout.clicked.connect(self.button_signout_onclick)
        
        # sign
        self.train = 1
        self.trainCnt = 0
        self.handData = [0]
        self.numGest = 0
        self.trainName = ''
        self.myGesture = 0
        self.sign_start.clicked.connect(self.start_frame)
        self.sign_stop.clicked.connect(self.stop_frame)
        self.sign_stop.setEnabled(False)
        self.groupBox_train.hide()
        self.recognizeBox.hide()
        self.pushButton.hide()
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.image = None
        self.textBox=''
        self.textBoxRecog = ''

        self.label_16.hide()
        self.label_17.hide()

        # Training and Recognize
        self.trainingBtn.setEnabled(False)
        self.trainingBtn.clicked.connect(self.training_box)
        self.pushButton.clicked.connect(self.gesture_name) #tombol buat masukin nama gestur
        self.pushButton_2.clicked.connect(self.gesture_done) #tombol selesai masukin nama gestur, buat bikin ga bisa nambahin gestur lagi
        self.pushButton_3.clicked.connect(self.file_name) #tombol buat simpen nama file
        self.pushButton_4.clicked.connect(self.start_train) #tombol buat mulai train, tapi masih belom tau caranya
        self.pushButton_5.hide()
        self.pushButton_5.clicked.connect(self.next_train)
        
        self.recognizeBtn.setEnabled(False)
        self.recognizeBtn.clicked.connect(self.recognize_box)
        self.search_button.clicked.connect(self.search_file)
        self.refresh_button.clicked.connect(self.refresh_recognize)
        self.resetTextBox_Button.clicked.connect(self.reset_textBox)
        self.resetTextBoxRecog_Button.clicked.connect(self.reset_textBoxRecog)

        # Notification
        self.button_notification_close.clicked.connect(self.button_notification_close_onclick)
    
    def menu_toggle(self):

        # GET WIDTH
        maxExtended = self.LeftMenu.width()
        width = 50
        standard = 160

        # SET MAX WIDTH
        if maxExtended == 160:
            widthExtended = width
        else:
            widthExtended = standard

        # ANIMATION
        self.animation = QPropertyAnimation(self.LeftMenu, b"maximumWidth")
        self.animation.setDuration(150)
        self.animation.setStartValue(maxExtended)
        self.animation.setEndValue(widthExtended)
        self.animation.start()

    def findDistances(self, handData):
        distMatrix = np.zeros([len(handData), len(handData)], dtype='float')
        palmSize = ((handData[0][0]-handData[9][0])**2 + (handData[0][1]-handData[9][1])**2)**(1./2.)
        for row in range(0, len(handData)):
            for column in range(0, len(handData)):
                distMatrix[row][column] = (((handData[row][0]-handData[column][0])**2 + (handData[row][1]-handData[column][1])**2)**(1./2.))/palmSize
        return distMatrix
        
    def findError(self, gestureMatrix, unknownMatrix, keyPoints):
        error = 0
        for row in keyPoints:
            for column in keyPoints:
                error = error+abs(gestureMatrix[row][column]-unknownMatrix[row][column])
        return error   

    def findGesture(self, unknownGesture, knownGestures, keyPoints, gestNames, toL):    
        errorArray = []
        for i in range(0, len(gestNames), 1):
            error = self.findError(knownGestures[i], unknownGesture, keyPoints)
            errorArray.append(error)
        errorMin = errorArray[0]
        minIndex = 0
        for i in range(0, len(errorArray), 1):
            if errorArray[i] < errorMin:
                errorMin = errorArray[i]
                minIndex = i
        if errorMin < toL:
            gesture = gestNames[minIndex]
        if errorMin >= toL:
            gesture = 'Unknown'
        return gesture
  
    def gesture_name(self):
        prompt = self.lineEdit.text() #masukin nama gestur, masukin ke variabel prompt
        
        gestNames.append(prompt) #array gestNames isinya nama nama gestur dari var prompt

        self.listWidget.addItem(prompt) #masukin inputan ke list box
        self.lineEdit.setText('') #clear text box

        self.numGest = self.listWidget.count() #menghitung ada berapa data di list
        self.label_14.setText(str(self.numGest)) #jumlah data ditampilin di numGest
        self.pushButton_2.setEnabled(True)

    def gesture_done(self):
        self.lineEdit.hide() #di hide biar ga bisa di isi lagi
        self.pushButton.hide()
        self.label_10.hide()
        self.pushButton_2.hide()
        self.pushButton_3.setEnabled(True)

    def file_name(self):
        self.trainName = self.lineEdit_2.text() 
        if self.trainName == '':
            self.trainName = 'Default'
        self.trainName = self.trainName +'.pkl'
        self.label_18.setText(str(self.trainName))
        self.lineEdit_2.hide()
        self.pushButton_3.hide()
        self.pushButton_4.setEnabled(True)

    def start_train(self, image):
        type_ = {
            "type" : "sign_language",
            "train" : "true"
        }
        self.send_payload(type_)
        self.pushButton_5.show()
        self.pushButton_5.setEnabled(True)
        self.pushButton_4.hide()

    def next_train(self): ####buat train data
        if self.trainCnt < self.numGest:
            self.trainCnt = self.trainCnt + 1
        self.handData = findHands.Marks(self.image)
        try:
            knownGesture = self.findDistances(self.handData[0])
        except IndexError:
            self.notify("Hands not detected.")
            return
        knownGestures.append(knownGesture)
        self.label_15.setText('Gesture No.' + str(int(self.trainCnt))) 
        if int(self.trainCnt) == int(self.numGest):
            self.pushButton_5.setText('Refresh')
            self.label_16.show()
            self.label_17.show()
            self.label_15.setText('Training Done') 
            self.train = 0
            with open(self.trainName, 'wb') as f:
                pickle.dump(gestNames, f)
                pickle.dump(knownGestures, f)
                        
        if self.train == 0:
            self.unknownGesture = self.findDistances(self.handData[0])
            self.myGesture = self.findGesture(self.unknownGesture, knownGestures, keyPoints, gestNames, tol)

            self.label_17.setText(str(self.myGesture))
            if str(self.myGesture) == ' ' : 
                self.label_17.setText('spacebar')

            if str(self.myGesture) == 'Unknown' : 
                self.myGesture = ''
            
            self.textBox = str(self.textBox) + str(self.myGesture)
            self.textBox_label.setText(str(self.textBox))
    
    def reset_textBox(self) : 
        self.textBox = ''
        self.textBox_label.setText('')

    def search_file(self):
        self.refresh_button.setEnabled(True)
        self.fileName = self.fileName_line.text()
        if self.fileName == '':
            self.fileName = 'Default'
        self.fileName = self.fileName +'.pkl'
        self.file_exist = os.path.exists(str(self.fileName))

        if self.file_exist == True:
            self.filleFound.setText('File Exists')
            # log after file is found
            type_ = {
                "type" : "sign_language",
                "train" : "false"
            }
            self.send_payload(type_)
        else:
            self.filleFound.setText('File NOT Found')
        
    def refresh_recognize(self):
        self.handData = findHands.Marks(self.image)
        self.train = 0
        self.recognizeName = self.fileName_line.text()
        if self.recognizeName == '':
            self.recognizeName = 'Default'
        self.recognizeName = self.recognizeName +'.pkl'
        self.file_exist = os.path.exists(str(self.recognizeName))

        if self.file_exist == True:
            self.refresh_button.setEnabled(True)
            self.resetTextBoxRecog_Button.setEnabled(True)
            with open(self.recognizeName, 'rb') as f:
                gestNames = pickle.load(f)
                knownGestures = pickle.load(f)
            if self.train == 0:
                self.unknownGesture = self.findDistances(self.handData[0])
                self.myGesture = self.findGesture(self.unknownGesture, knownGestures, keyPoints, gestNames, tol)
            self.detected_label.setText(str(self.myGesture))

            if str(self.myGesture) == 'Unknown' : 
                     self.myGesture = ''

            self.textBoxRecog = str(self.textBoxRecog) + str(self.myGesture)
            self.textBoxRecog_label.setText(str(self.textBoxRecog))
        
        if self.file_exist == False:
            self.refresh_button.setEnabled(False)
            self.resetTextBoxRecog_Button.setEnabled(False)

    def reset_textBoxRecog(self) :
        self.textBoxRecog = ''
        self.textBoxRecog_label.setText('')     

    def start_frame(self):
        self.sign_start.setEnabled(False)
        self.sign_stop.setEnabled(True)
        self.trainingBtn.setEnabled(True)
        self.recognizeBtn.setEnabled(True)
        self.button_shop.setEnabled(False) # disable shop analyzer
        self.timer.start(5)
        self.cap=cv2.VideoCapture(0,cv2.CAP_DSHOW)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT,width)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH,height)
        self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        self.pushButton_5.hide()
        self.search_button.hide()
        self.refresh_button.hide()
        self.label_sign.setText(misc.hand_prompt_start)
        self.notify(misc.cam_start)

    def update_frame(self):
        _, self.image = self.cap.read()
        self.image = cv2.flip(self.image,1)
        self.displayImage(self.image, 1)

    def stop_frame(self):
        self.sign_start.setEnabled(True)
        self.sign_stop.setEnabled(False)
        self.trainingBtn.setEnabled(False)
        self.recognizeBtn.setEnabled(False)
        self.timer.stop()
        self.cap.release()
        self.label_sign.setText(misc.hand_prompt_stop)
        self.button_shop.setEnabled(True) # re-enable shop analyzer
        self.pushButton.hide()
        self.pushButton_2.hide()
        self.pushButton_3.hide()
        self.pushButton_4.hide()
        self.pushButton_5.hide()
        self.search_button.hide()
        self.refresh_button.hide()
        self.notify(misc.cam_close)

    def displayImage(self, image, window=1):
        image = cv2.resize(image, (648, 432))
        handData = findHands.Marks(self.image)
        for hand in handData:   
            for ind in keyPoints:
                #bikin circle
                center_coordinates = hand[ind]
                radius = 25
                color = (255, 0, 255)
                thickness = 3
                image_output = cv2.circle(image, center_coordinates, radius , color, thickness)
                src = cv2.cvtColor(image_output, cv2.COLOR_BGR2RGB)
                h, w, ch = src.shape
                bytesPerLine = ch * w

                qimage = QImage(src.data, w, h, bytesPerLine, QImage.Format_RGB888)

                if window == 1:
                    self.label_sign.setPixmap(QPixmap.fromImage(qimage))
                    self.label_sign.setScaledContents(True)
          
    def training_box(self):
        self.recognizeBox.hide()
        self.groupBox_train.show()
        self.pushButton.show()
        self.pushButton_2.show()
        self.pushButton_3.show()
        self.pushButton_4.show()
        self.pushButton_5.show()
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.pushButton_5.setEnabled(False)
        self.label_sign.setText(misc.hand_prompt_start)
    
    def recognize_box(self):
        self.groupBox_train.hide()
        self.recognizeBox.show()
        self.search_button.show()
        self.refresh_button.show()
        self.refresh_button.setEnabled(False)
  
    def button_sign_onclick(self):
        self.button_sign.setStyleSheet(misc.button_selected)
        self.button_home.setStyleSheet(misc.button_deselected)
        self.button_shop.setStyleSheet(misc.button_deselected)
        self.stackedWidget_main.setCurrentWidget(self.page_sign)
        self.notify(misc.hand_welcome)
    
    def button_shop_onclick(self):
        self.button_shop.setStyleSheet(misc.button_selected)
        self.button_sign.setStyleSheet(misc.button_deselected)
        self.button_home.setStyleSheet(misc.button_deselected)
        self.stackedWidget_main.setCurrentWidget(self.page_shop)
        self.notify(misc.activity_welcome)
    
    def button_pref_onclick(self):
        if not self.center_menu.isVisible():
            self.center_menu.show()
        self.stackedWidget_side.setCurrentWidget(self.page_pref)
        self.button_pref.setStyleSheet(misc.button_selected)
        self.button_help.setStyleSheet(misc.button_deselected)
        self.button_info.setStyleSheet(misc.button_deselected)

    def button_info_onclick(self):
        if not self.center_menu.isVisible():
            self.center_menu.show()
        self.stackedWidget_side.setCurrentWidget(self.page_info)
        self.button_info.setStyleSheet(misc.button_selected)
        self.button_pref.setStyleSheet(misc.button_deselected)
        self.button_help.setStyleSheet(misc.button_deselected)

    def button_help_onclick(self):
        if not self.center_menu.isVisible():
            self.center_menu.show()
        self.stackedWidget_side.setCurrentWidget(self.page_help)
        self.button_help.setStyleSheet(misc.button_selected)
        self.button_info.setStyleSheet(misc.button_deselected)
        self.button_pref.setStyleSheet(misc.button_deselected)
    
    def button_center_close_onclick(self):
        self.center_menu.hide()
        self.button_pref.setStyleSheet(misc.button_deselected)
        self.button_help.setStyleSheet(misc.button_deselected)
        self.button_info.setStyleSheet(misc.button_deselected)

    def button_account_onclick(self):
        self.right_menu.show()
        self.stackedWidget_right.setCurrentWidget(self.page_profile)
    
    def button_more_onclick(self):
        self.right_menu.show()
        self.stackedWidget_right.setCurrentWidget(self.page_more)
    
    def button_signout_onclick(self):
        widget.setCurrentIndex(0)
        widget.removeWidget(widget.widget(1))
    
    def button_right_close_onclick(self):
        self.right_menu.hide()
    
    # shop activity
    def shop_start_onclick(self):
        self.button_sign.setEnabled(False) # disable sign language
        self.notify(misc.activity_start.format(
            datetime.now().strftime("%d %B %Y, %H:%M:%S")
        ))
        time, number = activity_cv.run()
        self.notify(misc.activity_end.format(
            datetime.now().strftime("%d %B %Y, %H:%M:%S")
        ))
        self.plot(time, "Average activity time", number, "No. of activity")
        self.button_sign.setEnabled(True) # re-enable sign language
        type_ = "shop_analyzer"
        self.send_payload(type_)
    
    def plot(self, x, x_label, y, y_label):
        self.canvas.axes.cla()
        self.canvas.axes.scatter(x, y)
        self.canvas.axes.set_xlabel(x_label)
        self.canvas.axes.set_ylabel(y_label)
        self.canvas.draw()
    
    def notify(self, msg):
        if not self.popup_container.isVisible():
            self.popup_container.show()
        self.label_notification.setText(msg)

    def send_payload(self, payload_type):
        now_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        payload = {
            "user" : self.email,
            "datetime" : now_str,
            "type" : payload_type
        }
        try:
            self.doc_ref.add(payload)
        except:
            self.notify(misc.log_failed)
    
    def button_notification_close_onclick(self):
        self.popup_container.hide()
    
    def button_notification_onclick(self):
        self.popup_container.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon("control-system-icon-15.jpg"))
    app.setApplicationName("Python GUI Project")
    widget = QStackedWidget()
    login_page = Login()
    widget.addWidget(login_page)
    widget.showMaximized()
    sys.exit(app.exec_())