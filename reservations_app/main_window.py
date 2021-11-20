import PySimpleGUI as sg
import reservations_window

# Future Tutorial - https://betterprogramming.pub/how-to-generate-and-decode-qr-codes-in-python-a933bce56fd0
# Multiple windows
# Multiple files
sg.theme('Black')

layout = [[sg.Text("Enter full name:"), sg.Input(key='-NAME-', do_not_clear=True, size=(20, 1))],
          [sg.Text("Enter your passport number:"), sg.Input(key='-PASSPORT_NUMBER-', do_not_clear=True, size=(10, 1))],
          # "RADIO" makes the radio buttons part of the same group, so when you click one, the other will be unchecked
          [sg.Radio("Male", "RADIO", key='-MALE-'), sg.Radio("Female", "RADIO", key='-FEMALE-')],
          [sg.Input(key='-DEPARTURE-', size=(20,1)), sg.CalendarButton("DATE OF DEPARTURE", close_when_date_chosen=True,  target='-DEPARTURE-', location=(0,0), no_titlebar=False )],
          [sg.Input(key='-ARRIVAL-', size=(20,1)), sg.CalendarButton("DATE OF ARRIVAL", close_when_date_chosen=True,  target='-ARRIVAL-', location=(0,0), no_titlebar=False )],
          [sg.Text('Choose your destination:',size=(30, 1), font='Lucida',justification='left')],
          # Formatting is weird on Mac - also need to change number of rows based on desired appearance
          [sg.Listbox(values=['Havana', 'Moscow', 'Beijing', 'Tehran', 'Damascus', 'Tripoli', 'Sanaa'], size=(40, 5), select_mode='single', key='-DESTINATION-')],
          [sg.Button('Reserve Ticket'), sg.Button('See Reservations'), sg.Exit()]
]

reservations_array = []

window = sg.Window('привет Airlines', layout, size=(300, 300))

while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        break
    elif event == 'Reserve Ticket':
        reservations_window.submit(values, reservations_array)
        sg.popup("Reservation submitted!")
    elif event == 'See Reservations':
        reservations_window.create(reservations_array)

window.close()