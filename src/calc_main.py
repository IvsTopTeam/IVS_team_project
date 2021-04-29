##
# @mainpage Program Documentation
# @tableofcontents
# @subsection TopTeam Calculator
# A simple implementation of arithmetic calculator for second IVS project with main purpose - focus on TEAM WORK.
#
# @subsection Documentation
# In this documentation you can find all the elements that our project is composed of.
#
# For quick access click on <a href="file:///home/xbubak01/Documents/IVS/project2/IVS_team_project/doc/html/files.html">Files</a>,
# choose one that you are interested in and learn more about all the functions, variables, etc. used.
#
# It includes mathematical library, main function structure with GUI essentials and tests having set the foundation of program development (TDD).
#
# @author Natalia Bubakova
# @date 28.4.2020
#

##
# @file calc_main.py
# @brief Essential file building the program
#

import calc_gui

app = calc_gui.QApplication([])
window = calc_gui.GUI()
app.setApplicationName("TopTeam calculator")
window.show()
app.exec_()

