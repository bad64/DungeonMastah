import sys, os
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QFrame
from PyQt5.QtWidgets import QVBoxLayout, QHBoxLayout, QGridLayout
from PyQt5.QtWidgets  import QLabel, QLineEdit, QPushButton, QSpinBox

class EntityData(QWidget):
    def __init__(self):
        super().__init__()

        ## Grid layout
        self.layout = QGridLayout()
        self.setFixedWidth(200)

        ## Entity attributes
        self.name = QLineEdit("----")       # Row 0, Col 0, Colspan 4

        self.currentHP = QLabel("0")        # Row 1, Col 0
        self.maxHP = QLineEdit("0")         # Row 1, Col 1
        self.HPPlus = QPushButton("+")      # Row 1, Col 2
        self.HPMinus = QPushButton("-")     # Row 1, Col 3
        self.HPtoMax = QPushButton("MAX")   # Row 1, Col 4

        self.currentMP = QLabel("0")        # Row 2, Col 0
        self.maxMP = QLineEdit("0")         # Row 2, Col 1
        self.MPPlus = QPushButton("+")      # Row 2, Col 2
        self.MPMinus = QPushButton("-")     # Row 2, Col 3
        self.MPtoMax = QPushButton("MAX")   # Row 2, Col 4

        self.labelStr = QLabel("STR: ")     # Row 3, Col 0
        self.boxStr = QLineEdit("0")        # Row 3, Col 1

        self.labelDex = QLabel("DEX: ")     # Row 4, Col 0
        self.boxDex = QLineEdit("0")        # Row 4, Col 1

        self.labelCon = QLabel("CON: ")     # Row 5, Col 0
        self.boxCon = QLineEdit("0")        # Row 5, Col 1
        
        self.labelInt = QLabel("INT: ")     # Row 6, Col 0
        self.boxInt = QLineEdit("0")        # Row 6, Col 1

        self.labelChr = QLabel("CHR: ")     # Row 7, Col 0
        self.boxChr = QLineEdit("0")        # Row 7, Col 1
        
        ## Signals
        self.HPPlus.clicked.connect(lambda: self.HPMod(1))
        self.HPMinus.clicked.connect(lambda: self.HPMod(-1))
        self.MPPlus.clicked.connect(lambda: self.MPMod(1))
        self.MPMinus.clicked.connect(lambda: self.MPMod(-1))
        self.HPtoMax.clicked.connect(lambda: self.MaxOut("HP"))
        self.MPtoMax.clicked.connect(lambda: self.MaxOut("MP"))

        ## Layout setup
        
        self.layout.addWidget(self.name, 0, 0, 1, 6)

        # HP row
        self.layout.addWidget(QLabel("HP:"), 1, 0, 1, 1)
        self.layout.addWidget(self.currentHP, 1, 1, 1, 1)
        self.layout.addWidget(QLabel("/"), 1, 2, 1, 1)
        self.layout.addWidget(self.maxHP, 1, 3, 1, 1)
        self.layout.addWidget(self.HPMinus, 1, 4, 1, 1)
        self.layout.addWidget(self.HPPlus, 1, 5, 1, 1)
        self.layout.addWidget(self.HPtoMax, 1, 6, 1, 1)

        # MP row
        self.layout.addWidget(QLabel("MP:"), 2, 0, 1, 1)
        self.layout.addWidget(self.currentMP, 2, 1, 1, 1)
        self.layout.addWidget(QLabel("/"), 2, 2, 1, 1)
        self.layout.addWidget(self.maxMP, 2, 3, 1, 1)
        self.layout.addWidget(self.MPMinus, 2, 4, 1, 1)
        self.layout.addWidget(self.MPPlus, 2, 5, 1, 1)
        self.layout.addWidget(self.MPtoMax, 2, 6, 1, 1)

        # Character stats
        self.layout.addWidget(self.labelStr, 3, 0, 1, 3)
        self.layout.addWidget(self.boxStr, 3, 3, 1, 4)

        self.layout.addWidget(self.labelDex, 4, 0, 1, 3)
        self.layout.addWidget(self.boxDex, 4, 3, 1, 4)

        self.layout.addWidget(self.labelCon, 5, 0, 1, 3)
        self.layout.addWidget(self.boxCon, 5, 3, 1, 4)

        self.layout.addWidget(self.labelInt, 6, 0, 1, 3)
        self.layout.addWidget(self.boxInt, 6, 3, 1, 4)

        self.layout.addWidget(self.labelChr, 7, 0, 1, 3)
        self.layout.addWidget(self.boxChr, 7, 3, 1, 4)

        ## Set widget layout
        self.setLayout(self.layout)

    def HPMod(self, mod):
        maxValue = int( self.maxHP.text() )
        minValue = maxValue * -1
        currentValue = int( self.currentHP.text() )
        if currentValue + mod >= minValue and currentValue + mod <= maxValue:
            self.currentHP.setText(str(currentValue + mod))
        else:
            return
    
    def MPMod(self, mod):
        maxValue = int( self.maxMP.text() )
        currentValue = int( self.currentMP.text() )
        
        if currentValue + mod <= maxValue:
            self.currentMP.setText(str(currentValue + mod))
        else:
            return

    def MaxOut(self, stat):
        if stat == "HP":
            self.currentHP.setText(self.maxHP.text())
        elif stat == "MP":
            self.currentMP.setText(self.maxMP.text())

class Separator(QWidget):
    def __init__(self, separatorType):
        super().__init__()

        self.line = QFrame()

        HLine = 0
        VLine = 1

        if separatorType == 0:
            self.line.setFrameShape(QFrame.HLine)
        elif separatorType == 1:
            self.line.setFrameShape(QFrame.VLine)
        else:
            self.line.setFrameShape(QFrame.NoFrame)
            
        self.line.setFrameShadow(QFrame.Sunken)

class TabLayout(QWidget):
    def __init__(self, toplabel):
        super().__init__()

        ## Get label from ctor args
        self.label = QLabel(toplabel)

        ## Create and bind spinbox to update function
        self.spinbox = QSpinBox()
        self.spinbox.setMinimum(1)
        self.spinbox.valueChanged.connect(self.update)

        ## Keep track of how many elements we have in sublayout 2
        self.counter = 1

        ## Layouts
        self.toplayout = QVBoxLayout()
        self.sublayout1 = QHBoxLayout()
        self.sublayout2 = QHBoxLayout()

        ## Build the first line with label and spinbox
        self.sublayout1.addWidget(self.label)
        self.sublayout1.addWidget(self.spinbox)

        ## Build the entity container
        self.sublayout2.addWidget( EntityData() )

        ## Build top level layout
        self.toplayout.addLayout(self.sublayout1)
        self.toplayout.addLayout(self.sublayout2)

        ## Display
        self.setLayout(self.toplayout)

    def update(self):        
        if self.spinbox.value() > self.counter:
            for i in range( 0, self.spinbox.value() - self.counter ):
                self.sublayout2.addWidget( EntityData() )
        elif self.spinbox.value() < self.counter:
            # Delete all widgets
            while self.sublayout2.count() > 0:
                item = self.sublayout2.takeAt(0)

                if not item:
                    continue

                w = item.widget()
                if w:
                    w.setParent(None)

            # Recreate all widgets
            for i in range( 0, self.spinbox.value() ):
                self.sublayout2.addWidget( EntityData() )

        self.sublayout2.update()
        self.toplayout.update()
        self.counter = self.spinbox.value()

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dungeon Mastah")

        ## Root tab widget
        self.rootTabLayout = QTabWidget()

        ## Root tab layout
        self.layout0 = QHBoxLayout()
        
        ## TAB 1
        ## Contains the player data
        self.playersTab = TabLayout("Players: ")
        
        ## TAB 2
        ## Contains enemy data
        self.enemiesTab = TabLayout("Enemies: ")

        ## TAB 3
        ## Contains music !
        self.musicTab = QWidget()
        self.musicTabInit()

        ## Construct tab layout
        self.rootTabLayout.addTab(self.playersTab, "Players")
        self.rootTabLayout.addTab(self.enemiesTab, "Enemies")
        self.rootTabLayout.addTab(self.musicTab, "Music")

        ## Add tab layout to root window
        self.layout0.addWidget(self.rootTabLayout)
        self.setLayout(self.layout0)
        
        ## Show window
        self.show()
        
    def musicTabInit(self):
        layout = QGridLayout()        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    context = MainWindow()
    sys.exit(app.exec_())
