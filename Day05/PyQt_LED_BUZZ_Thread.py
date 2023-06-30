import typing
from PyQt5.QtCore import *
from PyQt5.QtCore import QObject
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import RPi.GPIO as GPIO
import sys
import time

LED_State = 0
BUZZ_State = 0

class Ui_Form(QWidget):
    def setupUi(self, Form):
        if Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 230, 381, 61))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.Btn_buzz = QPushButton(self.horizontalLayoutWidget)
        self.Btn_buzz.setObjectName(u"Btn_buzz")

        self.horizontalLayout.addWidget(self.Btn_buzz)

        self.Btn_led = QPushButton(self.horizontalLayoutWidget)
        self.Btn_led.setObjectName(u"Btn_led")

        self.horizontalLayout.addWidget(self.Btn_led)

        self.grb_led = QGroupBox(Form)
        self.grb_led.setObjectName(u"grb_led")
        self.grb_led.setGeometry(QRect(10, 10, 381, 111))
        self.Lbl_LED = QLabel(self.grb_led)
        self.Lbl_LED.setObjectName(u"Lbl_LED")
        self.Lbl_LED.setGeometry(QRect(0, 30, 381, 71))
        self.grb_buuz = QGroupBox(Form)
        self.grb_buuz.setObjectName(u"grb_buuz")
        self.grb_buuz.setGeometry(QRect(10, 120, 381, 111))
        self.Lbl_BUZZ = QLabel(self.grb_buuz)
        self.Lbl_BUZZ.setObjectName(u"Lbl_BUZZ")
        self.Lbl_BUZZ.setGeometry(QRect(0, 30, 381, 71))
        self.retranslateUi(Form)
        QMetaObject.connectSlotsByName(Form)
        # setupUi

        self.Btn_led.clicked.connect(self.On_Off_Button)
        self.Btn_buzz.clicked.connect(self.On_Off_Button)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.Btn_buzz.setText(QCoreApplication.translate("Form", u"BUZZ", None))
        self.Btn_led.setText(QCoreApplication.translate("Form", u"LED", None))
        self.grb_led.setTitle(QCoreApplication.translate("Form", u"LED \uc0c1\ud0dc", None))
        self.Lbl_LED.setText(QCoreApplication.translate("Form", u"LED_State : OFF", None))
        self.grb_buuz.setTitle(QCoreApplication.translate("Form", u"BUZZ \uc0c1\ud0dc", None))
        self.Lbl_BUZZ.setText(QCoreApplication.translate("Form", u"BUZZ_State : OFF", None))
        # retranslateUi

    def On_Off_Button(self):
        btn = self.sender() 
        btnName = btn.objectName()
        Trig_Pin = 24
        Echo_Pin = 23
        LED_Pin = 22
        
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(Trig_Pin, GPIO.OUT) # Trig=24
        GPIO.setup(Echo_Pin, GPIO.IN)  # Echo=23    
        GPIO.setup(LED_Pin, GPIO.OUT)   # LED=22

        if btnName == "Btn_led":
            global LED_State		
            if(LED_State == 0):
                GPIO.output(LED_Pin, 1)
                LED_State = 1
                self.Lbl_LED.setText("LED_State : ON")
            else:
                GPIO.output(LED_Pin, 0)
                LED_State = 0
                self.Lbl_LED.setText("LED_State : OFF")

        elif btnName == "Btn_buzz":
            global BUZZ_State
            if BUZZ_State == 0:
                BUZZ_State = 1
                buzz = BUZZ_Thread()
                buzz.buzzStateChanged.connect(self.updateBuzzState)
                buzz.finished.connect(buzz.deleteLater)
                buzz.start()
            elif BUZZ_State == 1:
                BUZZ_State = 0

    def updateBuzzState(self, state):
        self.Lbl_BUZZ.setText(f"BUZZ_State : {state}")

class BUZZ_Thread(QThread):
    buzzStateChanged = pyqtSignal(str)

    def run(self):
        BUZZ_Pin = 25

        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(BUZZ_Pin, GPIO.OUT) # Buzzer=25

        buzz = GPIO.PWM(BUZZ_Pin, 440)
        global BUZZ_State
        if BUZZ_State == 1:
            self.buzzStateChanged.emit("ON")
            while BUZZ_State == 1:
                buzz.start(50)
                buzz.ChangeFrequency(1000)
                time.sleep(0.1)
            BUZZ_State = 0
        else:
            buzz.stop()

    def __del__(self):
        self.wait()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Form = QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())