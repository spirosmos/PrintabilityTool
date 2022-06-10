from PyQt5 import QtCore, QtGui, QtWidgets
import printabilityComputation as pScore
import json

class Ui_MainWindow(object):

    def addChild(self,value,errorValue,parentID,childID):
        _translate = QtCore.QCoreApplication.translate

        if  parentID == 1 and self.treeWidget.topLevelItem(parentID).child(0).childCount() == 0 and childID == 1:           
            QtWidgets.QMessageBox(self).critical(self, "Computation Error", "Add 'CAD area' first in order to add 'STL area'.")
            return  
        elif parentID == 1 and  childID == 0 and value == 0.0:
            QtWidgets.QMessageBox(self).critical(self, "Computation Error", "'CAD area' cannot be zero.")
            return  




        if parentID == 1 and self.treeWidget.topLevelItem(parentID).child(childID).childCount() >= 1:
            self.treeWidget.topLevelItem(parentID).child(childID).removeChild(self.treeWidget.topLevelItem(parentID).child(childID).child(0))
            item_buff = QtWidgets.QTreeWidgetItem(self.treeWidget.topLevelItem(parentID).child(childID)).setText(0, _translate("MainWindow", str(value)))

        elif parentID == 1:
            item_buff = QtWidgets.QTreeWidgetItem(self.treeWidget.topLevelItem(parentID).child(childID)).setText(0, _translate("MainWindow", str(value)))
        else:
            item_buff = QtWidgets.QTreeWidgetItem(self.treeWidget.topLevelItem(parentID).child(childID)).setText(0, _translate("MainWindow", str(value) + "  (+- " + str(errorValue) + ")"))

        self.treeWidget.topLevelItem(parentID).setExpanded(True)
        self.treeWidget.topLevelItem(parentID).child(childID).setExpanded(True)
        self.updateLCD_printabilityScore()





    def updateLCD_per_Feature(self):
        data = self.getDataFromTree_withError()
        buffer_data = {"Holes":[], "Pins":[], "Supported_walls":[], "Unsupported_walls":[], "Embossed_details_Width":[], "Embossed_details_Height":[], "Engraved_details_Width":[], "Engraved_details_Height":[], "Thin_Features":[], "Area_STL":[], "Area_CAD":[]}       
        technology = self.tech_comboBox.currentIndex()
        application = self.app_comboBox_2.currentIndex()
        
        if (not(data["Holes"] == [])):
            buffer_data["Holes"] = data["Holes"]

            pf_score = pScore.computePFperChar(buffer_data, technology, application)
            if pf_score >= 50 and pf_score <=100:
                self.holes_PF_score.setStyleSheet("""QLCDNumber{ background-color: green;color: yellow;}""")
            elif pf_score < 50 and pf_score > 0:
                self.holes_PF_score.setStyleSheet("""QLCDNumber{ background-color: red;color: white;}""")
            self.holes_PF_score.display(str(round(pf_score,3)))
        else:
            self.holes_PF_score.setStyleSheet("""QLCDNumber{ background-color: white;color: black;}""")
            self.holes_PF_score.display('-')
        buffer_data["Holes"] = []

        
        if (not(data["Pins"] == [])):
            buffer_data["Pins"] = data["Pins"]

            pf_score = pScore.computePFperChar(buffer_data, technology, application)
            if pf_score >= 50 and pf_score <=100:
                self.pins_PF_score.setStyleSheet("""QLCDNumber{ background-color: green;color: yellow;}""")
            elif pf_score < 50 and pf_score > 0:
                self.pins_PF_score.setStyleSheet("""QLCDNumber{ background-color: red;color: white;}""")
            self.pins_PF_score.display(str(round(pf_score,3)))
        else:
            self.pins_PF_score.setStyleSheet("""QLCDNumber{ background-color: white;color: black;}""")
            self.pins_PF_score.display('-')
        buffer_data["Pins"] = []



        if (not(data["Supported_walls"] == [])):
            buffer_data["Supported_walls"] = data["Supported_walls"]

            pf_score = pScore.computePFperChar(buffer_data, technology, application)
            if pf_score >= 50 and pf_score <=100:
                self.supp_PF_score.setStyleSheet("""QLCDNumber{ background-color: green;color: yellow;}""")
            elif pf_score < 50 and pf_score > 0:
                self.supp_PF_score.setStyleSheet("""QLCDNumber{ background-color: red;color: white;}""")
            self.supp_PF_score.display(str(round(pf_score,3)))
        else:
            self.supp_PF_score.setStyleSheet("""QLCDNumber{ background-color: white;color: black;}""")
            self.supp_PF_score.display('-')
        buffer_data["Supported_walls"] = []



        if (not(data["Unsupported_walls"] == [])):
            buffer_data["Unsupported_walls"] = data["Unsupported_walls"]

            pf_score = pScore.computePFperChar(buffer_data, technology, application)
            if pf_score >= 50 and pf_score <=100:
                self.unsupp_PF_score.setStyleSheet("""QLCDNumber{ background-color: green;color: yellow;}""")
            elif pf_score < 50 and pf_score > 0:
                self.unsupp_PF_score.setStyleSheet("""QLCDNumber{ background-color: red;color: white;}""")
            self.unsupp_PF_score.display(str(round(pf_score,3)))
        else:
            self.unsupp_PF_score.setStyleSheet("""QLCDNumber{ background-color: white;color: black;}""")
            self.unsupp_PF_score.display('-')
        buffer_data["Unsupported_walls"] = []




        if (not(data["Embossed_details_Width"] == [])):
            buffer_data["Embossed_details_Width"] = data["Embossed_details_Width"]
            buffer_data["Embossed_details_Height"] = data["Embossed_details_Height"]

            pf_score = pScore.computePFperChar(buffer_data, technology, application)
            if pf_score >= 50 and pf_score <=100:
                self.embossed_PF_score.setStyleSheet("""QLCDNumber{ background-color: green;color: yellow;}""")
            elif pf_score < 50 and pf_score > 0:
                self.embossed_PF_score.setStyleSheet("""QLCDNumber{ background-color: red;color: white;}""")
            self.embossed_PF_score.display(str(round(pf_score,3)))
        else:
            self.embossed_PF_score.setStyleSheet("""QLCDNumber{ background-color: white;color: black;}""")
            self.embossed_PF_score.display('-')
        buffer_data["Embossed_details_Width"] = []
        buffer_data["Embossed_details_Height"] = []



        if (not(data["Engraved_details_Width"] == [])):
            buffer_data["Engraved_details_Width"] = data["Engraved_details_Width"]
            buffer_data["Engraved_details_Height"] = data["Engraved_details_Height"]

            pf_score = pScore.computePFperChar(buffer_data, technology, application)
            if pf_score >= 50 and pf_score <=100:
                self.engraved_PF_score.setStyleSheet("""QLCDNumber{ background-color: green;color: yellow;}""")
            elif pf_score < 50 and pf_score > 0:
                self.engraved_PF_score.setStyleSheet("""QLCDNumber{ background-color: red;color: white;}""")
            self.engraved_PF_score.display(str(round(pf_score,3)))
        else:
            self.engraved_PF_score.setStyleSheet("""QLCDNumber{ background-color: white;color: black;}""")
            self.engraved_PF_score.display('-')
        buffer_data["Engraved_details_Width"] = []
        buffer_data["Engraved_details_Height"] = []
    

        if (not(data["Thin_Features"] == [])):
            buffer_data["Thin_Features"] = data["Thin_Features"]
           
            pf_score = pScore.computePFperChar(buffer_data, technology, application)
            if pf_score >= 50 and pf_score <=100:
                self.thinF_PF_score.setStyleSheet("""QLCDNumber{ background-color: green;color: yellow;}""")
            elif pf_score < 50 and pf_score > 0:
                self.thinF_PF_score.setStyleSheet("""QLCDNumber{ background-color: red;color: white;}""")
            self.thinF_PF_score.display(str(round(pf_score,3)))
        else:
            self.thinF_PF_score.setStyleSheet("""QLCDNumber{ background-color: white;color: black;}""")
            self.thinF_PF_score.display('-')
        buffer_data["Thin_Features"] = []
        





    def updateLCD_printabilityScore(self):
        data = self.getDataFromTree_withError()
        self.updateLCD_per_Feature()

        technology = self.tech_comboBox.currentIndex()
        print("technology ",technology)
        application = self.app_comboBox_2.currentIndex()
        print("application ",application)
        score = pScore.computePrintability(data, technology, application)
        if score >= 50 and score <=100:
            self.lcdNumber.setStyleSheet("""QLCDNumber 
                                           { background-color: green; 
                                             color: yellow;
                                           }""")
        elif score < 50 and score >= 0:
            self.lcdNumber.setStyleSheet("""QLCDNumber 
                                           { background-color: red; 
                                             color: white;
                                           }""")
        else:
            self.lcdNumber.setStyleSheet("""QLCDNumber 
                                       { background-color: red; 
                                         color: white;
                                       }""")
            self.lcdNumber.display('error')
            return

        self.lcdNumber.display(str(round(score,3)))

        print(score)
    
 
    def saveFile(self ):
        self.options = QtWidgets.QFileDialog.Options()
    
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,"QFileDialog.getOpenFileNames()", "","Text Files (*.txt)", options=self.options)
        print(fileName)
       
        data = self.getDataFromTree_withError()
        appNames = ["Biomedical", "Mechanical", "Artistic"]
        techNames = ["Fused Deposition Modeling", "Material Jetting", "Binder Jetting"] 
        if fileName != '':
            file = open(fileName,"w+")
            for i in range(0,3):
                for j in range(0,3):
                    score = pScore.computePrintability(data, i, j)
                    toWrite = techNames[i] + " / " + appNames[j] + " : " + str(round(score,4)) + "\n"

                    file.write(toWrite)
            file.close()

        return



    def helpMessage(self):
        msg = QtWidgets.QMessageBox(0, "Help", "'Printability tool' is created to predict the probability of a successful 3D model printing. This tool integrates all necessary parameters according to 3D printing technology intended application and geometrical part characteristics to measure the final success printability score (%) for a specific 3D model. Based on: \nI. Fudos, M. Ntousia, V. Stamati, P. Charalampous, T. Kontodina, I. Kostavelis, D. Tzovaras.'A characterization of 3d printability', Computer Aided Design and Applications (2020) 363–367.", QtWidgets.QMessageBox.Ok)
        msg.setStyleSheet("QLabel {min-width: 500px; min-height: 300px;}")
        msg.setTextFormat(3)
        msg.exec()
        

    def getDataFromTree_withError(self):
       
        root = self.treeWidget.invisibleRootItem()
        signal_count = root.childCount()
        buff = []
      
       

        data = {"Holes":[], "Pins":[], "Supported_walls":[], "Unsupported_walls":[], "Embossed_details_Width":[], "Embossed_details_Height":[], "Engraved_details_Width":[], "Engraved_details_Height":  [], "Thin_Features":[], "Area_STL":[], "Area_CAD":[]}       




        keys = ["Holes", "Pins", "Supported walls", "Unsupported walls", "Embossed details", "Engraved details", "Thin features", "CAD area", "STL area"]
        for i in range(signal_count):
            signal = root.child(i)
            checked_sweeps = list()
            num_children = signal.childCount()
            
            for n in range(num_children):
                child_cat = signal.child(n)
                num_children = child_cat.childCount()
               
                buff = []
                buff_2 = []
                error_buff = []
                if child_cat.text(0) == keys[0]:
                    for j in range(num_children):
                        value = child_cat.child(j)
                        dat = value.text(0).split("  (+- ")[0]
                        error = value.text(0).split("  (+- ")[1].replace(')','')                      
                        buff.append([float(dat), float(error)])
                        
                    data["Holes"] = buff


                elif child_cat.text(0) == keys[1]:
                    for j in range(num_children):
                        value = child_cat.child(j)
                        dat = value.text(0).split("  (+- ")[0]
                        error = value.text(0).split("  (+- ")[1].replace(')','')                      
                        buff.append([float(dat), float(error)])
                    data["Pins"] = buff

                elif child_cat.text(0) == keys[2]:
                    for j in range(num_children):
                        value = child_cat.child(j)
                        dat = value.text(0).split("  (+- ")[0]
                        error = value.text(0).split("  (+- ")[1].replace(')','')                      
                        buff.append([float(dat), float(error)])
                    data["Supported_walls"] = buff


                elif child_cat.text(0) == keys[3]:
                    for j in range(num_children):
                        value = child_cat.child(j)
                        dat = value.text(0).split("  (+- ")[0]
                        error = value.text(0).split("  (+- ")[1].replace(')','')                      
                        buff.append([float(dat), float(error)])
                    data["Unsupported_walls"] = buff

                elif child_cat.text(0) == keys[4]:
                    for j in range(num_children):
                        value = child_cat.child(j)
                        dat = value.text(0).split("  (+- ")[0]
                        error = value.text(0).split("  (+- ")[1].replace(')','')   
                        buff.append([float(dat.split(" / ")[0]),  float(error)])

                        buff_2.append([float(dat.split(" / ")[1]),  float(error)])
                    data["Embossed_details_Width"] = buff
                    data["Embossed_details_Height"] = buff_2

                elif child_cat.text(0) == keys[5]:
                    for j in range(num_children):
                        value = child_cat.child(j)
                        dat = value.text(0).split("  (+- ")[0]
                        error = value.text(0).split("  (+- ")[1].replace(')','')
                        buff.append([float(dat.split(" / ")[0]),  float(error)])

                        buff_2.append([float(dat.split(" / ")[1]),  float(error)])
                    data["Engraved_details_Width"] = buff
                    data["Engraved_details_Height"] = buff_2

                elif child_cat.text(0) == keys[6]:
                    for j in range(num_children):
                        value = child_cat.child(j)
                        dat = value.text(0).split("  (+- ")[0]
                        error = value.text(0).split("  (+- ")[1].replace(')','')                      
                        buff.append([float(dat), float(error)])
                    data["Thin_Features"] = buff


                elif child_cat.text(0) == keys[7]:
                    for j in range(num_children):
                        value = child_cat.child(j)
                        buff.append(float(value.text(0)))
                    data["Area_CAD"] = buff

                elif child_cat.text(0) == keys[8]:
                    for j in range(num_children):
                        value = child_cat.child(j)
                        buff.append(float(value.text(0)))
                    data["Area_STL"] = buff
                

        return (data)



    def readProfile(self):
        self.options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileNames()", "","Text Files (*.json)", options=self.options)
        print(fileName)
       
   
        
        if fileName != '':
            fileData = open(fileName, "r")
            jsonData = json.load(fileData)
            self.setTreeItems(jsonData)

    def saveProfile(self):
        self.options = QtWidgets.QFileDialog.Options()
        fileName, _ = QtWidgets.QFileDialog.getSaveFileName(self,"QFileDialog.getOpenFileNames()", "","Text Files (*.json)", options=self.options)
        print(fileName)


        

        jsonSkeleton ='{"Probability":{"PF":{"Holes":[],"Pins":[],"Supported_walls":[],"Unsupported_walls":[],"Embossed_details_Width":[],"Embossed_details_Height":[],"Engraved_details_Width":[],"Engraved_details_Height":[],"Thin_Features":[]},"PG":{"Area_CAD":[],"Area_STL":[] } } }'
        ex = json.loads(jsonSkeleton)
        
        if fileName != '':
            fileData = open(fileName, "w+")
            data = self.getDataFromTree_withError()
            ex["Probability"]["PF"]["Holes"]= data["Holes"]
            
            ex["Probability"]["PF"]["Pins"] = data["Pins"]

            ex["Probability"]["PF"]["Supported_walls"] = data["Supported_walls"]

            ex["Probability"]["PF"]["Unsupported_walls"] = data["Unsupported_walls"]

            ex["Probability"]["PF"]["Embossed_details_Width"]= data["Embossed_details_Width"]
            ex["Probability"]["PF"]["Embossed_details_Height"]= data["Embossed_details_Height"]

            ex["Probability"]["PF"]["Engraved_details_Width"] = data["Engraved_details_Width"]
            ex["Probability"]["PF"]["Engraved_details_Height"] = data["Engraved_details_Height"]

            ex["Probability"]["PF"]["Thin_Features"]= data["Thin_Features"]

            ex["Probability"]["PG"]["Area_CAD"] = data["Area_CAD"]
            ex["Probability"]["PG"]["Area_STL"] = data["Area_STL"]

            json_string = json.dumps(ex)
            fileData.write(json_string)



    def setTreeItems(self, jsonData):
        self.Tree_clear()
        print(jsonData)

        data = {"Holes":[], "Pins":[], "Supported_walls":[], "Unsupported_walls":[], "Embossed_details_Width":[], "Embossed_details_Height":[], "Engraved_details_Width":[], "Engraved_details_Height":  [], "Thin_Features":[], "Area_STL":[], "Area_CAD":[]}       

        for i in range(0,len(jsonData["Probability"]["PF"]["Holes"])):
            self.addChild(jsonData["Probability"]["PF"]["Holes"][i][0], jsonData["Probability"]["PF"]["Holes"][i][1], 0, 0)
        
        for i in range(0,len(jsonData["Probability"]["PF"]["Pins"])):
            self.addChild(jsonData["Probability"]["PF"]["Pins"][i][0], jsonData["Probability"]["PF"]["Pins"][i][1], 0, 1)
        
        for i in range(0,len(jsonData["Probability"]["PF"]["Supported_walls"])):
            self.addChild(jsonData["Probability"]["PF"]["Supported_walls"][i][0], jsonData["Probability"]["PF"]["Supported_walls"][i][1], 0, 2)
       
        for i in range(0,len(jsonData["Probability"]["PF"]["Unsupported_walls"])):
            self.addChild(jsonData["Probability"]["PF"]["Unsupported_walls"][i][0], jsonData["Probability"]["PF"]["Unsupported_walls"][i][1], 0, 3)
        
        for i in range(0,len(jsonData["Probability"]["PF"]["Embossed_details_Width"])):
            inputString = str(jsonData["Probability"]["PF"]["Embossed_details_Width"][i][0]) + " / " + str(jsonData["Probability"]["PF"]["Embossed_details_Height"][i][0])
            
            self.addChild(inputString ,jsonData["Probability"]["PF"]["Embossed_details_Width"][i][1], 0, 4)
        
        for i in range(0,len(jsonData["Probability"]["PF"]["Engraved_details_Width"])):
            inputString = str(jsonData["Probability"]["PF"]["Engraved_details_Width"][i][0]) + " / " + str(jsonData["Probability"]["PF"]["Engraved_details_Height"][i][0])
            self.addChild(inputString ,jsonData["Probability"]["PF"]["Engraved_details_Width"][i][1], 0, 5)
        
        for i in range(0,len(jsonData["Probability"]["PF"]["Thin_Features"])):
            self.addChild(jsonData["Probability"]["PF"]["Thin_Features"][i][0], jsonData["Probability"]["PF"]["Thin_Features"][i][1], 0, 6)

        for i in range(0,len(jsonData["Probability"]["PG"]["Area_CAD"])):
            self.addChild(jsonData["Probability"]["PG"]["Area_CAD"][i], None, 1, 0)
        
        for i in range(0,len(jsonData["Probability"]["PG"]["Area_STL"])):
            self.addChild(jsonData["Probability"]["PG"]["Area_STL"][i], None, 1, 1)
       



    

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        screen_height = QtWidgets.QApplication.primaryScreen().size().height()
        print(screen_height)

        if screen_height < 2160:
            app_height = 800
        else:
            app_height = 1000


        MainWindow.resize(1400, app_height)

        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        layout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        layout.addWidget(self.scrollArea)
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1380, 990))
        self.scrollAreaWidgetContents.setStyleSheet('background-color: white')
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        layout = QtWidgets.QHBoxLayout(self.scrollAreaWidgetContents)










        #self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setGeometry(QtCore.QRect(30, 20,741, 880))
        self.groupBox.setObjectName("groupBox")
      
        self.groupBox.setStyleSheet("""QGroupBox 
                                           { background-color: white;                                  
                                           }""")

        MainWindow.setStyleSheet("""QMainWindow 
                                           { background-color: white;    
                                             
                                           }""")


        self.groupBoxScores = QtWidgets.QGroupBox(self.groupBox)
        self.groupBoxScores.setGeometry(QtCore.QRect(620, 0, 115, 825))
        self.groupBoxScores.setObjectName("groupBoxScores")



        menuBar = self.menuBar()
        # Creating menus using a QMenu object
        fileMenu = QtWidgets.QMenu("&File", self)
        menuBar.addMenu(fileMenu)
        
        self.actionLoad = QtWidgets.QAction("Load profile")
        fileMenu.addAction(self.actionLoad)
        self.actionLoad.triggered.connect(self.readProfile)
        
        self.actionSave = QtWidgets.QAction("Save profile")
        fileMenu.addAction(self.actionSave)
        
        self.actionSave.triggered.connect(self.saveProfile)
        
        fileMenu.addSeparator()
        self.actionQuit = QtWidgets.QAction("Quit")
        fileMenu.addAction(self.actionQuit)

        self.actionQuit.triggered.connect(QtCore.QCoreApplication.quit)
        
       


        self.holesLabel = QtWidgets.QLabel(self.groupBox)
        self.holesLabel.setGeometry(QtCore.QRect(10, 60, 91, 31))
        self.holesLabel.setObjectName("holesLabel")
        self.holes_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.holes_doubleSpinBox.setGeometry(QtCore.QRect(170, 60, 71, 22))
        self.holes_doubleSpinBox.setMaximum(1000.0)
        self.holes_doubleSpinBox.setSingleStep(0.5)
        self.holes_doubleSpinBox.setObjectName("holes_doubleSpinBox")

        self.holesLabelInfo = QtWidgets.QLabel(self.groupBox)
        self.holesLabelInfo.setGeometry(QtCore.QRect(170, 85, 100, 22))
        self.holesLabelInfo.setObjectName("holesLabelInfo")


        self.holesError_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.holesError_doubleSpinBox.setGeometry(QtCore.QRect(280, 60, 91, 22))
        self.holesError_doubleSpinBox.setMaximum(1000.0)
        self.holesError_doubleSpinBox.setSingleStep(0.005)
        self.holesError_doubleSpinBox.setDecimals(4)
        self.holesError_doubleSpinBox.setObjectName("holesError_doubleSpinBox")

        self.holesErrorLabelInfo = QtWidgets.QLabel(self.groupBox)
        self.holesErrorLabelInfo.setGeometry(QtCore.QRect(280, 85, 140, 22))
        self.holesErrorLabelInfo.setObjectName("holesErrorLabelInfo")


        self.holes_pushButton = QtWidgets.QPushButton(self.groupBox)
        self.holes_pushButton.setGeometry(QtCore.QRect(380, 60, 75, 23))
        self.holes_pushButton.setObjectName("holes_pushButton")
        self.holes_pushButton.clicked.connect(lambda: self.addChild(self.holes_doubleSpinBox.value(), self.holesError_doubleSpinBox.value(), 0, 0))

        self.holes_pixmap = QtWidgets.QLabel(self.groupBox)
        pixmapHoles = QtGui.QPixmap('holes.jpg')


        self.holes_pixmap.setPixmap(pixmapHoles)
        self.holes_pixmap.move(500,30)
        self.holes_pixmap.setToolTip('Add the diameter in mm.')
        self.holes_pixmap.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        

        self.holes_PF_score = QtWidgets.QLCDNumber(self.groupBoxScores)
        self.holes_PF_score.setGeometry(QtCore.QRect(15, 50, 80, 35))
        self.holes_PF_score.setObjectName("holes_PF_score")
        self.holes_PF_score.display("-")
        self.holes_PF_score.setDigitCount(7)
        self.holes_PF_score.setToolTip('Part Characteristic Probability Score (%) for all Holes.')
        self.holes_PF_score.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))



        self.pins_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.pins_doubleSpinBox.setGeometry(QtCore.QRect(170, 180, 71, 22))
        self.pins_doubleSpinBox.setMaximum(1000.0)
        self.pins_doubleSpinBox.setSingleStep(0.5)
        self.pins_doubleSpinBox.setObjectName("pins_doubleSpinBox")

        self.pinsLabelInfo = QtWidgets.QLabel(self.groupBox)
        self.pinsLabelInfo.setGeometry(QtCore.QRect(170, 205, 100, 22))
        self.pinsLabelInfo.setObjectName("pinsLabelInfo")


        self.pinsError_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.pinsError_doubleSpinBox.setGeometry(QtCore.QRect(280, 180, 91, 22))
        self.pinsError_doubleSpinBox.setMaximum(1000.0)
        self.pinsError_doubleSpinBox.setSingleStep(0.005)
        self.pinsError_doubleSpinBox.setDecimals(4)
        self.pinsError_doubleSpinBox.setObjectName("pinsError_doubleSpinBox")

        self.pinsErrorLabelInfo = QtWidgets.QLabel(self.groupBox)
        self.pinsErrorLabelInfo.setGeometry(QtCore.QRect(280,205, 140, 22))
        self.pinsErrorLabelInfo.setObjectName("pinsErrorLabelInfo")

        self.pins_pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pins_pushButton_2.setGeometry(QtCore.QRect(380, 180, 75, 23))
        self.pins_pushButton_2.setObjectName("pins_pushButton_2")
        self.pinsLabel = QtWidgets.QLabel(self.groupBox)
        self.pinsLabel.setGeometry(QtCore.QRect(10, 180, 91, 31))
        self.pinsLabel.setObjectName("pinsLabel")       
        self.pins_pushButton_2.clicked.connect(lambda: self.addChild(self.pins_doubleSpinBox.value(), self.pinsError_doubleSpinBox.value(), 0, 1))     

        self.pins_pixmap = QtWidgets.QLabel(self.groupBox)
        pixmapPins = QtGui.QPixmap('pins.jpg')
        self.pins_pixmap.setPixmap( pixmapPins)
        self.pins_pixmap.move(500,140)
        self.pins_pixmap.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.pins_pixmap.setToolTip('Add the diameter in mm.')

        self.pins_PF_score = QtWidgets.QLCDNumber(self.groupBoxScores)
        self.pins_PF_score.setGeometry(QtCore.QRect(15, 170, 80, 35))
        self.pins_PF_score.setObjectName("pins_PF_score")
        self.pins_PF_score.display("-")
        self.pins_PF_score.setDigitCount(7)
        self.pins_PF_score.setToolTip('Part Characteristic Probability Score (%) for all Pins.')
        self.pins_PF_score.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))



        self.supp_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.supp_doubleSpinBox.setGeometry(QtCore.QRect(170, 300, 71, 22))
        self.supp_doubleSpinBox.setMaximum(1000.0)
        self.supp_doubleSpinBox.setSingleStep(0.5)
        self.supp_doubleSpinBox.setObjectName("supp_doubleSpinBox")


        self.suppLabelInfo = QtWidgets.QLabel(self.groupBox)
        self.suppLabelInfo.setGeometry(QtCore.QRect(170, 325, 110, 22))
        self.suppLabelInfo.setObjectName("suppLabelInfo")


        self.suppError_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.suppError_doubleSpinBox.setGeometry(QtCore.QRect(280, 300, 91, 22))
        self.suppError_doubleSpinBox.setMaximum(1000.0)
        self.suppError_doubleSpinBox.setSingleStep(0.005)
        self.suppError_doubleSpinBox.setDecimals(4)
        self.suppError_doubleSpinBox.setObjectName("suppError_doubleSpinBox")

        self.suppErrorLabelInfo = QtWidgets.QLabel(self.groupBox)
        self.suppErrorLabelInfo.setGeometry(QtCore.QRect(280,325, 140, 22))
        self.suppErrorLabelInfo.setObjectName("suppErrorLabelInfo")

        self.supp_pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.supp_pushButton_3.setGeometry(QtCore.QRect(380, 300, 75, 23))
        self.supp_pushButton_3.setObjectName("supp_pushButton_3")
        self.suppLabel = QtWidgets.QLabel(self.groupBox)
        self.suppLabel.setGeometry(QtCore.QRect(10, 300, 160, 31))
        self.suppLabel.setObjectName("suppLabel")
        self.supp_pushButton_3.clicked.connect(lambda: self.addChild(self.supp_doubleSpinBox.value(), self.suppError_doubleSpinBox.value(), 0, 2))

        self.supp_pixmap = QtWidgets.QLabel(self.groupBox)
        pixmapSupp = QtGui.QPixmap('supp_walls.jpg')
        self.supp_pixmap.setPixmap(pixmapSupp)
        self.supp_pixmap.move(500,260)
        self.supp_pixmap.setToolTip('Add the thickness in mm.')
        self.supp_pixmap.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        

        self.supp_PF_score = QtWidgets.QLCDNumber(self.groupBoxScores)
        self.supp_PF_score.setGeometry(QtCore.QRect(15, 290, 80, 35))
        self.supp_PF_score.setObjectName("supp_PF_score")
        self.supp_PF_score.display("-")
        self.supp_PF_score.setDigitCount(7)
        self.supp_PF_score.setToolTip('Part Characteristic Probability Score (%) for all Supported walls.')
        self.supp_PF_score.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))





        self.unsuppLabel = QtWidgets.QLabel(self.groupBox)
        self.unsuppLabel.setGeometry(QtCore.QRect(10, 420, 160, 31))
        self.unsuppLabel.setObjectName("unsuppLabel")
        self.unsupp_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.unsupp_doubleSpinBox.setGeometry(QtCore.QRect(170, 420, 71, 22))
        self.unsupp_doubleSpinBox.setMaximum(1000.0)
        self.unsupp_doubleSpinBox.setSingleStep(0.5)
        self.unsupp_doubleSpinBox.setObjectName("unsupp_doubleSpinBox")   
    
        self.unsuppLabelInfo = QtWidgets.QLabel(self.groupBox)
        self.unsuppLabelInfo.setGeometry(QtCore.QRect(170, 445, 110, 22))
        self.unsuppLabelInfo.setObjectName("unsuppLabelInfo")


        self.unsuppError_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.unsuppError_doubleSpinBox.setGeometry(QtCore.QRect(280, 420, 91, 22))
        self.unsuppError_doubleSpinBox.setMaximum(1000.0)
        self.unsuppError_doubleSpinBox.setSingleStep(0.005)
        self.unsuppError_doubleSpinBox.setDecimals(4)
        self.unsuppError_doubleSpinBox.setObjectName("unsuppError_doubleSpinBox")

        self.unsuppErrorLabelInfo = QtWidgets.QLabel(self.groupBox)
        self.unsuppErrorLabelInfo.setGeometry(QtCore.QRect(280,445, 140, 22))
        self.unsuppErrorLabelInfo.setObjectName("unsuppErrorLabelInfo")

        self.unsupp_pushButton_4 = QtWidgets.QPushButton(self.groupBox)
        self.unsupp_pushButton_4.setGeometry(QtCore.QRect(380, 420, 75, 23))
        self.unsupp_pushButton_4.setObjectName("unsupp_pushButton_4")
        self.unsupp_pushButton_4.clicked.connect(lambda: self.addChild(self.unsupp_doubleSpinBox.value(), self.unsuppError_doubleSpinBox.value(), 0, 3))

        self.unsupp_pixmap = QtWidgets.QLabel(self.groupBox)
        pixmapUnsupp = QtGui.QPixmap('unsupp_walls.jpg')
        self.unsupp_pixmap.setPixmap(pixmapUnsupp)
        self.unsupp_pixmap.move(500,380)
        self.unsupp_pixmap.setToolTip('Add the thickness in mm.')
        self.unsupp_pixmap.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))

        self.unsupp_PF_score = QtWidgets.QLCDNumber(self.groupBoxScores)
        self.unsupp_PF_score.setGeometry(QtCore.QRect(15, 410, 80, 35))
        self.unsupp_PF_score.setObjectName("unsupp_PF_score")
        self.unsupp_PF_score.display("-")
        self.unsupp_PF_score.setDigitCount(7)
        self.unsupp_PF_score.setToolTip('Part Characteristic Probability Score (%) for all Unsupported walls.')
        self.unsupp_PF_score.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))


        self.embossedLabel = QtWidgets.QLabel(self.groupBox)
        self.embossedLabel.setGeometry(QtCore.QRect(10, 540, 160, 31))
        self.embossedLabel.setObjectName("embossedLabel")
        self.embossedHeightSpinbox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.embossedHeightSpinbox.setGeometry(QtCore.QRect(170, 565, 71, 22))
        self.embossedHeightSpinbox.setMaximum(1000.0)
        self.embossedHeightSpinbox.setSingleStep(0.5)
        self.embossedHeightSpinbox.setObjectName("embossedHeightSpinbox")
        self.embossedWidthSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.embossedWidthSpinBox.setGeometry(QtCore.QRect(170, 515, 71, 22))
        self.embossedWidthSpinBox.setMaximum(1000.0)
        self.embossedWidthSpinBox.setSingleStep(0.5)
        self.embossedWidthSpinBox.setObjectName("embossedWidthSpinBox")
        
        self.embossedWidthLabelInfo = QtWidgets.QLabel(self.groupBox)
        self.embossedWidthLabelInfo.setGeometry(QtCore.QRect(170, 540, 100, 22))
        self.embossedWidthLabelInfo.setObjectName("embossedWidthLabelInfo")

        self.embossedHeightLabelInfo = QtWidgets.QLabel(self.groupBox)
        self.embossedHeightLabelInfo.setGeometry(QtCore.QRect(170, 590, 100, 22))
        self.embossedHeightLabelInfo.setObjectName("embossedHeightLabelInfo")

        self.embossedError_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.embossedError_doubleSpinBox.setGeometry(QtCore.QRect(280, 540, 91, 22))
        self.embossedError_doubleSpinBox.setMaximum(1000.0)
        self.embossedError_doubleSpinBox.setSingleStep(0.005)
        self.embossedError_doubleSpinBox.setDecimals(4)
        self.embossedError_doubleSpinBox.setObjectName("embossedError_doubleSpinBox")

        self.embossedErrorLabelInfo = QtWidgets.QLabel(self.groupBox)
        self.embossedErrorLabelInfo.setGeometry(QtCore.QRect(280,565, 140, 22))
        self.embossedErrorLabelInfo.setObjectName("embossedErrorLabelInfo")


        self.embossed_pushButton_5 = QtWidgets.QPushButton(self.groupBox)
        self.embossed_pushButton_5.setGeometry(QtCore.QRect(380, 540, 75, 23))
        self.embossed_pushButton_5.setObjectName("embossed_pushButton_5")
        self.embossed_pushButton_5.clicked.connect(lambda: self.addChild((str(self.embossedWidthSpinBox.value()) + " / " + str(self.embossedHeightSpinbox.value())), self.embossedError_doubleSpinBox.value(), 0, 4))
       
        self.embossed_pixmap = QtWidgets.QLabel(self.groupBox)
        pixmapEmbossed = QtGui.QPixmap('embossed.jpg')
        self.embossed_pixmap.setPixmap(pixmapEmbossed)
        self.embossed_pixmap.move(500,500)
        self.embossed_pixmap.setToolTip('Add the width and height in mm.')
        self.embossed_pixmap.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))

        self.embossed_PF_score = QtWidgets.QLCDNumber(self.groupBoxScores)
        self.embossed_PF_score.setGeometry(QtCore.QRect(15, 530, 80, 35))
        self.embossed_PF_score.setObjectName("embossed_PF_score")
        self.embossed_PF_score.display("-")
        self.embossed_PF_score.setDigitCount(7)
        self.embossed_PF_score.setToolTip('Part Characteristic Probability Score (%) for all Embossed details.')
        self.embossed_PF_score.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        



        self.engraved_pushButton_6 = QtWidgets.QPushButton(self.groupBox)
        self.engraved_pushButton_6.setGeometry(QtCore.QRect(380, 660, 75, 23))
        self.engraved_pushButton_6.setObjectName("engraved_pushButton_6")
        self.engravedWidthSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.engravedWidthSpinBox.setGeometry(QtCore.QRect(170, 635, 71, 22))
        self.engravedWidthSpinBox.setMaximum(1000.0)
        self.engravedWidthSpinBox.setSingleStep(0.5)
        self.engravedWidthSpinBox.setObjectName("engravedWidthSpinBox")
        self.engravedHeightSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.engravedHeightSpinBox.setGeometry(QtCore.QRect(170, 685, 71, 21))
        self.engravedHeightSpinBox.setMaximum(1000.0)
        self.engravedHeightSpinBox.setSingleStep(0.5)
        self.engravedHeightSpinBox.setObjectName("engravedHeightSpinBox")


        self.engravedError_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.engravedError_doubleSpinBox.setGeometry(QtCore.QRect(280, 660, 91, 22))
        self.engravedError_doubleSpinBox.setMaximum(1000.0)
        self.engravedError_doubleSpinBox.setSingleStep(0.005)
        self.engravedError_doubleSpinBox.setDecimals(4)
        self.engravedError_doubleSpinBox.setObjectName("engravedError_doubleSpinBox")

        self.engravedErrorLabelInfo = QtWidgets.QLabel(self.groupBox)
        self.engravedErrorLabelInfo.setGeometry(QtCore.QRect(280,685, 140, 22))
        self.engravedErrorLabelInfo.setObjectName("engravedErrorLabelInfo")

        
        self.engravedWidthLabelInfo = QtWidgets.QLabel(self.groupBox)
        self.engravedWidthLabelInfo.setGeometry(QtCore.QRect(170, 660, 100, 22))
        self.engravedWidthLabelInfo.setObjectName("engravedWidthLabelInfo")

        self.engravedHeightLabelInfo = QtWidgets.QLabel(self.groupBox)
        self.engravedHeightLabelInfo.setGeometry(QtCore.QRect(170, 710, 100, 22))
        self.engravedHeightLabelInfo.setObjectName("engravedHeightLabelInfo")


        self.engravedLabel = QtWidgets.QLabel(self.groupBox)
        self.engravedLabel.setGeometry(QtCore.QRect(10, 660, 160, 31))
        self.engravedLabel.setObjectName("engravedLabel")
        self.engraved_pushButton_6.clicked.connect(lambda: self.addChild((str(self.engravedWidthSpinBox.value()) + " / " + str(self.engravedHeightSpinBox.value())), self.engravedError_doubleSpinBox.value(), 0, 5))

        self.engraved_pixmap = QtWidgets.QLabel(self.groupBox)
        pixmapEngraved = QtGui.QPixmap('engraved.jpg')
        self.engraved_pixmap.setPixmap(pixmapEngraved)
        self.engraved_pixmap.move(500,620)
        self.engraved_pixmap.setToolTip('Add the width and depth in mm.')
        self.engraved_pixmap.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))


        self.engraved_PF_score = QtWidgets.QLCDNumber(self.groupBoxScores)
        self.engraved_PF_score.setGeometry(QtCore.QRect(10, 650, 80, 35))
        self.engraved_PF_score.setObjectName("engraved_PF_score")
        self.engraved_PF_score.display("-")
        self.engraved_PF_score.setDigitCount(7)
        self.engraved_PF_score.setToolTip('Part Characteristic Probability Score (%) for all Engraved details.')
        self.engraved_PF_score.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))


        self.thinFLabel = QtWidgets.QLabel(self.groupBox)
        self.thinFLabel.setEnabled(True)
        self.thinFLabel.setGeometry(QtCore.QRect(10, 780, 160, 31))
        self.thinFLabel.setObjectName("thinFLabel")     
        self.thinF_pushButton_7 = QtWidgets.QPushButton(self.groupBox)
        self.thinF_pushButton_7.setGeometry(QtCore.QRect(380, 780, 75, 23))
        self.thinF_pushButton_7.setObjectName("thinF_pushButton_7")    
        self.thinFSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.thinFSpinBox.setGeometry(QtCore.QRect(170, 780, 71, 22))
        self.thinFSpinBox.setMaximum(1000.0)
        self.thinFSpinBox.setSingleStep(0.5)
        self.thinFSpinBox.setObjectName("thinFSpinBox")

        self.thinFLabelInfo = QtWidgets.QLabel(self.groupBox)
        self.thinFLabelInfo.setGeometry(QtCore.QRect(170, 805, 110, 22))
        self.thinFLabelInfo.setObjectName("thinFLabelInfo")



        self.thinFError_doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox)
        self.thinFError_doubleSpinBox.setGeometry(QtCore.QRect(280, 780, 91, 22))
        self.thinFError_doubleSpinBox.setMaximum(1000.0)
        self.thinFError_doubleSpinBox.setSingleStep(0.005)
        self.thinFError_doubleSpinBox.setDecimals(4)
        self.thinFError_doubleSpinBox.setObjectName("thinFError_doubleSpinBox")

        self.thinFErrorLabelInfo = QtWidgets.QLabel(self.groupBox)
        self.thinFErrorLabelInfo.setGeometry(QtCore.QRect(280,805, 140, 22))
        self.thinFErrorLabelInfo.setObjectName("thinFErrorLabelInfo")

        self.thinF_pushButton_7.clicked.connect(lambda: self.addChild(self.thinFSpinBox.value(),self.thinFError_doubleSpinBox.value(), 0, 6))

        self.thinF_pixmap = QtWidgets.QLabel(self.groupBox)
        pixmapThinF = QtGui.QPixmap('thinFeature.jpg')
        self.thinF_pixmap.setPixmap(pixmapThinF)
        self.thinF_pixmap.move(500,740)
        self.thinF_pixmap.setToolTip('Add thickness in mm.')
        self.thinF_pixmap.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        
        self.thinF_PF_score = QtWidgets.QLCDNumber(self.groupBoxScores)
        self.thinF_PF_score.setGeometry(QtCore.QRect(15, 770, 80, 35))
        self.thinF_PF_score.setObjectName("thinF_PF_score")
        self.thinF_PF_score.display("-")
        self.thinF_PF_score.setDigitCount(7)
        self.thinF_PF_score.setToolTip('Part Characteristic Probability Score (%) for all Thin features.')
        self.thinF_PF_score.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))



        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setGeometry(QtCore.QRect(840, 20, 480, 111))
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setStyleSheet("""QGroupBox 
                                   { background-color: white                                            
                                   }""")

        self.stlAreaSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.stlAreaSpinBox.setGeometry(QtCore.QRect(228, 75, 106, 21))
        self.stlAreaSpinBox.setMaximum(10000.0)
        self.stlAreaSpinBox.setSingleStep(0.5)
        self.stlAreaSpinBox.setObjectName("stlAreaSpinBox")
        self.stlAreaSpinBox.setDecimals(5)
        self.stlAreaLabel = QtWidgets.QLabel(self.groupBox_2)
        self.stlAreaLabel.setGeometry(QtCore.QRect(10, 70, 100, 31))
        self.stlAreaLabel.setObjectName("stlAreaLabel")
        self.stlArea_pushButton_9 = QtWidgets.QPushButton(self.groupBox_2)
        self.stlArea_pushButton_9.setGeometry(QtCore.QRect(339, 75, 75, 23))
        self.stlArea_pushButton_9.setObjectName("stlArea_pushButton_9")
        self.stlArea_pushButton_9.clicked.connect(lambda: self.addChild(self.stlAreaSpinBox.value(), None, 1, 1))
       

        self.stlArea_pixmap = QtWidgets.QLabel(self.groupBox_2)
        pixmapStlArea = QtGui.QPixmap('icons8-help-24.png')
        self.stlArea_pixmap.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.stlArea_pixmap.setPixmap(pixmapStlArea)
        self.stlArea_pixmap.setGeometry(QtCore.QRect(440, 75,24,24))
        self.stlArea_pixmap.setToolTip('Add the boundary surface area of the STL model in mm^2.')
        

        self.cadAreaSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.cadAreaSpinBox.setGeometry(QtCore.QRect(230, 30, 106, 22))
        self.cadAreaSpinBox.setMaximum(10000.0)
        self.cadAreaSpinBox.setSingleStep(0.5)
        self.cadAreaSpinBox.setObjectName("cadAreaSpinBox") 
        self.cadAreaSpinBox.setDecimals(5)      
        self.cadArea_pushButton_8 = QtWidgets.QPushButton(self.groupBox_2)
        self.cadArea_pushButton_8.setGeometry(QtCore.QRect(339, 30, 75, 23))
        self.cadArea_pushButton_8.setObjectName("cadArea_pushButton_8")
        self.cadAreaLabel = QtWidgets.QLabel(self.groupBox_2)
        self.cadAreaLabel.setGeometry(QtCore.QRect(10, 25, 100, 31))
        self.cadAreaLabel.setObjectName("cadAreaLabel")
        self.cadArea_pushButton_8.clicked.connect(lambda: self.addChild(self.cadAreaSpinBox.value(), None, 1, 0))
        

        self.cadArea_pixmap = QtWidgets.QLabel(self.groupBox_2)
        pixmapCadArea = QtGui.QPixmap('icons8-help-24.png')
        self.cadArea_pixmap.setCursor(QtGui.QCursor(QtCore.Qt.WhatsThisCursor))
        self.cadArea_pixmap.setPixmap(pixmapCadArea)
        self.cadArea_pixmap.setGeometry(QtCore.QRect(440, 30,24,24))
        self.cadArea_pixmap.setToolTip('Add the boundary surface area of the CAD model in mm^2.')


        self.treeWidget = QtWidgets.QTreeWidget(self.scrollAreaWidgetContents)

        self.treeWidget.setGeometry(QtCore.QRect(840, 160, 480, 500))
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        


        self.clear_Button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.clear_Button.setGeometry(QtCore.QRect(1258, 608, 33, 33))
        self.clear_Button.setObjectName("clear_Button")
        self.clear_Button.clicked.connect(self.Tree_clear)
        icon  = QtGui.QIcon('trash_bin_icon.png')
        self.clear_Button.setIcon(icon)



        self.tech_comboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.tech_comboBox.setGeometry(QtCore.QRect(1080, 685, 240, 22))
        self.tech_comboBox.setObjectName("tech_comboBox")
        self.tech_comboBox.addItem("")
        self.tech_comboBox.addItem("")
        self.tech_comboBox.addItem("")
        self.tech_comboBox.setStyleSheet('selection-background-color: rgb(0,100,255)')

        self.app_comboBox_2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.app_comboBox_2.setGeometry(QtCore.QRect(1080, 755, 240, 22))
        self.app_comboBox_2.setObjectName("app_comboBox_2")
        self.app_comboBox_2.addItem("")
        self.app_comboBox_2.addItem("")
        self.app_comboBox_2.addItem("")
        self.app_comboBox_2.setStyleSheet('selection-background-color: rgb(0,100,255)')
        

        self.techLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.techLabel.setGeometry(QtCore.QRect(840, 680, 180, 31))
        self.techLabel.setObjectName("techLabel")
        

        self.appLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.appLabel.setGeometry(QtCore.QRect(840, 750, 180, 31))
        self.appLabel.setObjectName("appLabel")
        

        self.lcdNumber = QtWidgets.QLCDNumber(self.scrollAreaWidgetContents)
        self.lcdNumber.setGeometry(QtCore.QRect(1200, 820, 104, 41))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.display("0.0")
        self.lcdNumber.setDigitCount(7)
        
        self.score_Label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.score_Label.setGeometry(QtCore.QRect(840, 820, 251, 31))
        self.score_Label.setObjectName("score_Label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        myFont=QtGui.QFont()
        myFont.setBold(True)

        myFont2=QtGui.QFont('Arial', 7)
        myFont2.setItalic(True)

        self.setFont(QtGui.QFont('Arial', 12))

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Printability Tool"))
        self.groupBox.setTitle(_translate("MainWindow", "Part Characteristics"))
        self.groupBoxScores.setTitle(_translate("MainWindow", "PF Score (%)"))
        self.groupBoxScores.setFont(myFont)
        self.holesLabel.setText(_translate("MainWindow", "Holes"))
        
        self.holesLabelInfo.setText(_translate("MainWindow", "*Diameter (mm)"))
        self.holesLabelInfo.setFont(myFont2)

        self.holesErrorLabelInfo.setText(_translate("MainWindow", "*Mean Error (mm)"))
        self.holesErrorLabelInfo.setFont(myFont2)

        
        self.pinsLabelInfo.setText(_translate("MainWindow", "*Diameter (mm)"))
        self.pinsLabelInfo.setFont(myFont2)

        self.pinsErrorLabelInfo.setText(_translate("MainWindow", "*Mean Error (mm)"))
        self.pinsErrorLabelInfo.setFont(myFont2)

        self.suppLabelInfo.setText(_translate("MainWindow", "*Thickness (mm)"))
        self.suppLabelInfo.setFont(myFont2)
        
        self.suppErrorLabelInfo.setText(_translate("MainWindow", "*Mean Error (mm)"))
        self.suppErrorLabelInfo.setFont(myFont2)
        
        self.unsuppLabelInfo.setText(_translate("MainWindow", "*Thickness (mm)"))
        self.unsuppLabelInfo.setFont(myFont2)

        self.unsuppErrorLabelInfo.setText(_translate("MainWindow", "*Mean Error (mm)"))
        self.unsuppErrorLabelInfo.setFont(myFont2)

        
        self.embossedWidthLabelInfo.setText(_translate("MainWindow", "*Width (mm)"))
        self.embossedWidthLabelInfo.setFont(myFont2)

        self.embossedHeightLabelInfo.setText(_translate("MainWindow", "*Height (mm)"))
        self.embossedHeightLabelInfo.setFont(myFont2)


        self.embossedErrorLabelInfo.setText(_translate("MainWindow", "*Mean Error (mm)"))
        self.embossedErrorLabelInfo.setFont(myFont2)

        self.engravedWidthLabelInfo.setText(_translate("MainWindow", "*Width (mm)"))
        self.engravedWidthLabelInfo.setFont(myFont2)

        self.engravedHeightLabelInfo.setText(_translate("MainWindow", "*Depth (mm)"))
        self.engravedHeightLabelInfo.setFont(myFont2)


        self.engravedErrorLabelInfo.setText(_translate("MainWindow", "*Mean Error (mm)"))
        self.engravedErrorLabelInfo.setFont(myFont2)


        self.thinFLabelInfo.setText(_translate("MainWindow", "*Thickness (mm)"))
        self.thinFLabelInfo.setFont(myFont2)

        self.thinFErrorLabelInfo.setText(_translate("MainWindow", "*Mean Error (mm)"))
        self.thinFErrorLabelInfo.setFont(myFont2)

        self.holes_pushButton.setText(_translate("MainWindow", "ADD"))
        self.pins_pushButton_2.setText(_translate("MainWindow", "ADD"))
        self.pinsLabel.setText(_translate("MainWindow", "Pins"))
        self.unsuppLabel.setText(_translate("MainWindow", "Unsupported walls"))
        self.supp_pushButton_3.setText(_translate("MainWindow", "ADD"))
        self.unsupp_pushButton_4.setText(_translate("MainWindow", "ADD"))
        self.suppLabel.setText(_translate("MainWindow", "Supported walls"))
        self.engraved_pushButton_6.setText(_translate("MainWindow", "ADD"))
        self.embossedLabel.setText(_translate("MainWindow", "Embossed details"))
        self.thinFLabel.setText(_translate("MainWindow", "Thin features"))
        self.thinF_pushButton_7.setText(_translate("MainWindow", "ADD"))
        self.engravedLabel.setText(_translate("MainWindow", "Engraved details"))
        self.embossed_pushButton_5.setText(_translate("MainWindow", "ADD"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Global Characteristics"))
        self.stlAreaLabel.setText(_translate("MainWindow", "STL area"))
        self.cadArea_pushButton_8.setText(_translate("MainWindow", "ADD"))
        self.cadAreaLabel.setText(_translate("MainWindow", "CAD area"))
        self.stlArea_pushButton_9.setText(_translate("MainWindow", "ADD"))

        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Printability Inputs :"))

       
        __sortingEnabled = self.treeWidget.isSortingEnabled()


        self.treeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.treeWidget.customContextMenuRequested.connect(self.openMenu)

        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("MainWindow", "Part Characteristics"))
        self.treeWidget.topLevelItem(0).setFont(0,myFont)

        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("MainWindow", "Holes"))
        self.treeWidget.topLevelItem(0).child(0).setFont(0,myFont)
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("MainWindow", "Pins"))
        self.treeWidget.topLevelItem(0).child(1).setFont(0,myFont)
        self.treeWidget.topLevelItem(0).child(2).setText(0, _translate("MainWindow", "Supported walls"))
        self.treeWidget.topLevelItem(0).child(2).setFont(0,myFont)
        self.treeWidget.topLevelItem(0).child(3).setText(0, _translate("MainWindow", "Unsupported walls"))
        self.treeWidget.topLevelItem(0).child(3).setFont(0,myFont)
        self.treeWidget.topLevelItem(0).child(4).setText(0, _translate("MainWindow", "Embossed details"))
        self.treeWidget.topLevelItem(0).child(4).setFont(0,myFont)
        self.treeWidget.topLevelItem(0).child(5).setText(0, _translate("MainWindow", "Engraved details"))
        self.treeWidget.topLevelItem(0).child(5).setFont(0,myFont)
        self.treeWidget.topLevelItem(0).child(6).setText(0, _translate("MainWindow", "Thin features"))
        self.treeWidget.topLevelItem(0).child(6).setFont(0,myFont)
        self.treeWidget.topLevelItem(1).setText(0, _translate("MainWindow", "Global Characteristics"))
        self.treeWidget.topLevelItem(1).setFont(0,myFont)

        self.treeWidget.topLevelItem(1).child(0).setText(0, _translate("MainWindow", "CAD area"))
        self.treeWidget.topLevelItem(1).child(0).setFont(0,myFont)
        self.treeWidget.topLevelItem(1).child(1).setText(0, _translate("MainWindow", "STL area"))
        self.treeWidget.topLevelItem(1).child(1).setFont(0,myFont)
        self.treeWidget.setSortingEnabled(__sortingEnabled)

       
        self.tech_comboBox.setItemText(0, _translate("MainWindow", "Fused Deposition Modeling"))
        self.tech_comboBox.setItemText(1, _translate("MainWindow", "Material Jetting"))
        self.tech_comboBox.setItemText(2, _translate("MainWindow", "Binder Jetting"))
        self.tech_comboBox.currentIndexChanged.connect(self.updateLCD_printabilityScore)
        self.app_comboBox_2.setItemText(0, _translate("MainWindow", "Biomedical"))
        self.app_comboBox_2.setItemText(1, _translate("MainWindow", "Mechanical"))
        self.app_comboBox_2.setItemText(2, _translate("MainWindow", "Artistic"))
        self.app_comboBox_2.currentIndexChanged.connect(self.updateLCD_printabilityScore)
        self.techLabel.setText(_translate("MainWindow", "Printing technology"))
        self.techLabel.setFont(myFont)
        self.appLabel.setText(_translate("MainWindow", "Application"))
        self.appLabel.setFont(myFont)
        self.score_Label.setText(_translate("MainWindow", "PRINTABILITY SCORE (%) :"))
        self.score_Label.setFont(myFont)

        self.updateLCD_printabilityScore()


    def openMenu(self, position):
        invalid_options = ["Holes", "Pins", "Supported walls", "Unsupported walls", "Embossed details", "Engraved details", "Thin features", "CAD area", "STL area"]
        indexes = self.sender().selectedIndexes()

        mdlIdx = self.treeWidget.indexAt(position)
        if not mdlIdx.isValid():
            return
        item = self.treeWidget.itemFromIndex(mdlIdx)
        if len(indexes) > 0:
            level = 0
            index = indexes[0]
            itemID =  index.row()
            mainParentID = index.parent().row()
            
            while index.parent().isValid():
                
                index = index.parent()
     
                level += 1
        else:
            level = 0

        right_click_menu = QtWidgets.QMenu()
        if item.parent() != None and (item.text(0) not in invalid_options):

            act_del = right_click_menu.addAction(self.tr("Delete"))
            act_del.triggered.connect( lambda: self.TreeItem_Delete(itemID, index.row(), mainParentID) )

            right_click_menu.exec_(self.sender().viewport().mapToGlobal(position))
           

    def TreeItem_Delete(self, itemID, parentID,mainParentID):
        if  parentID == 1 and self.treeWidget.topLevelItem(parentID).child(1).childCount() == 1 and mainParentID == 0:
            
            QtWidgets.QMessageBox.critical(self, "Computation Error", "Delete 'STL area' first in order to delete 'CAD area'.")
            return  
        self.treeWidget.topLevelItem(parentID).child(mainParentID).takeChild(itemID)
        self.updateLCD_printabilityScore()  

    def Tree_clear(self):


        topLevelItem_IDs = [0,1]
        for toplvlID in topLevelItem_IDs:
            for chID in range (self.treeWidget.topLevelItem(toplvlID).childCount()):
                for itemID in range (self.treeWidget.topLevelItem(toplvlID).child(chID).childCount(),-1,-1):
                    self.treeWidget.topLevelItem(toplvlID).child(chID).takeChild(itemID)
        self.updateLCD_printabilityScore()  