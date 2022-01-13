import psutil
import sys
from win10toast import ToastNotifier
import os
import json
import threading
import platform
from PyQt5 import QtWidgets
from ui import Ui_MainWindow

class App(QtWidgets.QMainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.batteryInformation = tuple()

        self.numberOfNotifications=0
        self.lowerLimitValue=0
        self.upperLimitValue=0
        
        self.notifier=ToastNotifier()

        self.ui.sliderLowerLimit.valueChanged.connect(self.setLowVal)
        self.ui.sliderUpperLimit.valueChanged.connect(self.setUpVal)
        self.ui.numberOfNotifications.valueChanged.connect(self.setNumberOfNotifications)
        self.ui.latencyTime.valueChanged.connect(self.setLatencyTime)

        self.firstControl()


    def firstControl(self): #Controlling existence of data
        if not os.path.exists("data.txt"):
            data={"sliderLowerLimit":"45","sliderUpperLimit":"75","latencyTime":"10","numberOfNotifications":"5"}
            with open('data.txt','w') as file:
                json.dump(data, file)
        else:
            with open("data.txt","r",encoding="utf-8") as file:
                data=json.load(file)
        
        self.ui.sliderLowerLimit.setValue(int(data["sliderLowerLimit"]))
        self.ui.lowerLimitValue.setText("Value: "+str(self.ui.sliderLowerLimit.value()))
        self.lowerLimitValue=self.ui.sliderLowerLimit.value()

        self.ui.sliderUpperLimit.setValue(int(data["sliderUpperLimit"]))
        self.ui.upperLimitValue.setText("Value: "+str(self.ui.sliderUpperLimit.value()))
        self.upperLimitValue=self.ui.sliderUpperLimit.value()

        self.ui.latencyTime.setValue(int(data["latencyTime"]))

        self.ui.numberOfNotifications.setValue(int(data["numberOfNotifications"]))
        self.numberOfNotifications=self.ui.numberOfNotifications.value()

        self.refreshData()
        self.checkBattery()
        self.checkSystem()
        
        self.secondThread = threading.Thread(target=self.pushNotification)
        self.secondThread.daemon=True
        self.event = threading.Event()
        self.secondThread.start()


    def checkBattery(self): #Controlling whether psutil.sensors_battery() returns None
        if self.batteryInformation == None:
            dialog = QtWidgets.QMessageBox(self)
            dialog.setWindowTitle("ERROR!")
            dialog.setText("Battery can't be determined!")

            if dialog.exec() == QtWidgets.QMessageBox.Ok:
                sys.exit()


    def checkSystem(self):
        self.system = platform.uname()
        if self.system.release != "10":
            sysDialog = QtWidgets.QMessageBox(self)
            sysDialog.setWindowTitle("ERROR!")
            sysDialog.setText("This app is for Windows 10!")

            if sysDialog.exec() == QtWidgets.QMessageBox.Ok:
                sys.exit()


    def setLowVal(self,value):
        self.ui.lowerLimitValue.setText("Value: "+str(value))
        self.lowerLimitValue=value
        if self.ui.sliderLowerLimit.value()>=self.ui.sliderUpperLimit.value()-4:
            self.ui.sliderUpperLimit.setValue(self.ui.sliderLowerLimit.value()+5)
        with open("data.txt","r",encoding="utf-8") as file:
            data=json.load(file)
        with open("data.txt","w",encoding="utf-8") as file:
            data["sliderLowerLimit"]=value
            json.dump(data,file)


    def setUpVal(self,value):
        self.ui.upperLimitValue.setText("Value: "+str(value))
        self.upperLimitValue=value
        if self.ui.sliderUpperLimit.value()<=self.ui.sliderLowerLimit.value()+4:
            self.ui.sliderLowerLimit.setValue(self.ui.sliderUpperLimit.value()-5)
        with open("data.txt","r",encoding="utf-8") as file:
            data=json.load(file)
        with open("data.txt","w",encoding="utf-8") as file:
            data["sliderUpperLimit"]=value
            json.dump(data,file)


    def setNumberOfNotifications(self,value):
        self.numberOfNotifications=value
        with open("data.txt","r",encoding="utf-8") as file:
            data=json.load(file)
        with open("data.txt","w",encoding="utf-8") as file:
            data["numberOfNotifications"]=value
            json.dump(data,file)


    def setLatencyTime(self,value):
        with open("data.txt","r",encoding="utf-8") as file:
            data=json.load(file)
        with open("data.txt","w",encoding="utf-8") as file:
            data["latencyTime"]=value
            json.dump(data,file)


    def refreshData(self):
        self.batteryInformation=psutil.sensors_battery()


    def pushNotification(self):
        try:
            while True:


                self.refreshData()
                if self.batteryInformation.power_plugged==False and self.batteryInformation.percent<=self.lowerLimitValue:
                    i=0
                    while i<self.numberOfNotifications and self.batteryInformation.power_plugged==False and self.batteryInformation.percent<=self.lowerLimitValue:
                        i+=1
                        print(f"{i}")
                        if i == self.numberOfNotifications:
                            self.close()
                        print("Low Battery Notification")
                        self.notifier.show_toast("Attention!",f"Low battery! Plug in. Charge level: {self.batteryInformation.percent}",icon_path=None, duration=5)
                        self.event.wait((self.ui.latencyTime.value()))
                        self.refreshData() #Just in case power_plugged or percentage change during while loop


                elif self.batteryInformation.power_plugged==True and self.batteryInformation.percent>=self.upperLimitValue:
                    i=0
                    while i<self.numberOfNotifications and self.batteryInformation.power_plugged==True and self.batteryInformation.percent>=self.upperLimitValue:
                        i+=1
                        print(f"{i}")
                        if i == self.numberOfNotifications:
                            self.close()
                        print("Charged Battery Notification")
                        self.notifier.show_toast("Attention!",f"Charged battery! Plug out. Charge level: {self.batteryInformation.percent}",icon_path=None, duration=5)
                        self.event.wait((self.ui.latencyTime.value()))
                        self.refreshData()
                        

                else:
                    print("Waiting")
                    self.event.wait((self.ui.latencyTime.value()))

        except Exception as ex:
            print(ex)
  

def program():
    program = QtWidgets.QApplication(sys.argv)
    win = App()
    win.show()
    sys.exit(program.exec_())

program()