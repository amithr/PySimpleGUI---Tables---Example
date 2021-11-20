import PySimpleGUI as sg

def submit(input_values, reservations_array):
    gender = 'Male' if input_values['-MALE-'] else 'Female'

    reservation = [
        input_values['-NAME-'],
        input_values['-PASSPORT_NUMBER-'],
        gender,
        input_values['-DEPARTURE-'],
        input_values['-ARRIVAL-'],
        input_values['-DESTINATION-'][0],
    ]

    #reservations_array should be a 2D array
    reservations_array.append(reservation)
    print(reservations_array)


def create(reservations_array):
    headings = ['Name', 'Passport Number', 'Gender', 'Departure Date', 'Arrival Date', 'Destination']

    reservations_window_layout = [
        [sg.Table(values=reservations_array, headings=headings, max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=10,
                    key='-TABLE-',
                    row_height=35,
                    tooltip='Reservations Table')],
        [sg.Button("Exit")]
    ]

    reservations_window = sg.Window("Reservations Window", reservations_window_layout, modal=True)

    while True:
        event, values = reservations_window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        
    reservations_window.close() 