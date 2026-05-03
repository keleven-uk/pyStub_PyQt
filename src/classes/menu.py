###############################################################################################################
#    menu   Copyright (C) <2025-26>  <Kevin Scott>                                                            #
#                                                                                                             #
#    Constructs the main menu.                                                                                #
#                                                                                                             #
#    For changes see history.txt                                                                              #
#                                                                                                             #
###############################################################################################################
#                                                                                                             #
#    This program is free software: you can redistribute it and/or modify it under the terms of the           #
#    GNU General Public License as published by the Free Software Foundation, either Version 3 of the         #
#    License, or (at your option) any later Version.                                                          #
#                                                                                                             #
#    This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without        #
#    even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the               #
#    GNU General Public License for more details.                                                             #
#                                                                                                             #
#    You should have received a copy of the GNU General Public License along with this program.               #
#    If not, see <http://www.gnu.org/licenses/>.                                                              #
#                                                                                                             #
###############################################################################################################

from PyQt6.QtWidgets import QMenuBar, QMenu
from PyQt6.QtGui     import QAction, QIcon

from src.projectPaths import RESOURCE_PATH

class Menu(QMenuBar):
    """  Constructs the main menu.

         self.myMenu.setVisible(self.menu_bar)  -  Creates the menu object.
         self.myMenu = self.menu.buildMenu()    -  Builds the main menu.
         self.menu.buildToolBar()               -  Builds the tool Bar.
         menu.buildContextMenu()                -  Builds the Context Menu.

         To add the main menu  - setMenuBar(self.myMenu)  I save a reference, so I can alter the visibility of the menu.
         To add the Tool bar   - self.addToolBar(self.menu.buildToolBar())  Creates a reference to the tool bar.

    """

    def __init__(self, myConfig, myLogger, parent=None):
        super().__init__(parent)

        self.config      = myConfig
        self.logger      = myLogger
        self.parent      = parent

        self.buildActions()

    # ----------------------------------------------------------------------------------------------------------------------- buildActions() --------
    def buildActions(self):
        """  Set up menu actions.
        """
        self.logger.info(" Building Menu Actions.")

        path = f"{RESOURCE_PATH}/cross.png"
        self.actClose = QAction(QIcon(path),"Close", self)
        self.actClose.triggered.connect(self.parent.close)                #  Close the app, which call the closeEvent (overridden).
        self.actClose.setCheckable(False)
    # ----------------------------------------------------------------------------------------------------------------------- buildMenu() -----------
    def buildMenu(self):
        # Set up main menu
        self.logger.info(" Building Menu")
        menu = QMenuBar()

        mnuFile    = menu.addMenu("&File")

        #  Set up menu actions.
        mnuFile.addAction(self.actClose)

        return menu

