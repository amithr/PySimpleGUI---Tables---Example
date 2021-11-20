import PySimpleGUI as sg

contact_information_array = [
    ['Amith', '161 Magnolia St', '331-569'],
    ['John', '392 Butcher St', '243-897'],
    ['Amith', '3341 Columbus Ave', '998-731']
]

headings = ['Full Name', 'Address', 'Phone Number']

layout = [
        [sg.Table(values=contact_information_array, 
        headings=headings, 
        max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=10,
                    key='-TABLE-',
                    row_height=35)]
    ]

window = sg.Window("Contact Information Window", layout)

while True:
    event, values = window.read()
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
        
window.close()