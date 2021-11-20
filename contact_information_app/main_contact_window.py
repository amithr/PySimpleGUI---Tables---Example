import PySimpleGUI as sg
import contact_information_table_window

contact_information_array = []
headings = ['Full Name', 'Address', 'Phone Number']

layout = [[sg.Text("Enter full name:"), sg.Input(key='-NAME-', do_not_clear=True, size=(20, 1))],
          [sg.Text("Enter address:"), sg.Input(key='-ADDRESS-', do_not_clear=True, size=(10, 1))],
          [sg.Text("Enter phone number:"), sg.Input(key='-PHONE_NUMBER-', do_not_clear=True, size=(10, 1))],
          [sg.Button('Submit Contact Information'), sg.Button('Show Table'), sg.Exit()]]

window = sg.Window("Submit Contact Information", layout)

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Submit Contact Information':
        contact_information = [values['-NAME-'], values['-ADDRESS-'], values['-PHONE_NUMBER-']]
        contact_information_array.append(contact_information)
        sg.popup("Contact Information Submitted!")
    elif event == 'Show Table':
        contact_information_table_window.create(contact_information_array, headings)