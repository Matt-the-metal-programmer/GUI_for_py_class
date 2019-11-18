import PySimpleGUI as sg
import statistics
layout = [
            [sg.Text('Please enter your GPAs for the following classes.')],
            [sg.Text('Bus Analytics I', size=(15, 1)), sg.InputText('', key='_COB191_')],
            [sg.Text('Interpersonal skills', size=(15, 1)), sg.InputText('', key='_COB202_')],
            [sg.Text('Computer Information Systems', size=(15, 1)), sg.InputText('', key='_COB204_')],
            [sg.Text('Financial Accouting', size=(15, 1)), sg.InputText('', key='_COB241_')],
            [sg.Text('Managerial Accounting', size=(15, 1)), sg.InputText('', key='_COB242_')],
            [sg.Text('Business Analytics II', size=(15, 1)), sg.InputText('', key='_COB291_')],
            [sg.Text('Introduction to Microeconomics', size=(15, 1)), sg.InputText('', key='_ECON201_')],
            [sg.Text('Introduction to Macroeconomics', size=(15, 1)), sg.InputText('', key='_ECON200_')],
            [sg.Text('Calculus', size=(15, 1)), sg.InputText('', key='_MATH205_')],
            [sg.Submit(),sg.Cancel()]
            ]

window = sg.Window('Simple data entry window', layout)
event, values = window.read()
window.Close()
int_list = [int(values['_COB191_']),int(values['_COB202_']),int(values['_COB204_']),int(values['_COB204_']),int(values['_COB241_']),int(values['_COB242_']),int(values['_COB291_']),int(values['_ECON201_']),int(values['_ECON200_']),int(values['_MATH205_'])]

k = statistics.mean(int_list)
if k > 2.7:
    kek = True
    f = "You will be accepted into the College of business as of right now."
else:
    kek = False
    f = "You will not be accepted into the College of business as of right now."
sg.Popup("College of Business GPA's", "COB 191 " + values['_COB191_'], "COB 202 " + values['_COB202_'], "COB 204 " +values['_COB204_'], "COB 241 " + values['_COB241_'],"COB 242 " +values['_COB242_'],"COB 291 " + values["_COB291_"],"ECON 201 "+ values['_ECON201_'],"ECON 200 " + values['_ECON200_'],"MATH 205 " + values['_MATH205_'],"Average GPA : " +str(k),f)
