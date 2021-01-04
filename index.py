import PySimpleGUI as sg
import os

layout = [[sg.Text("Choose a file:  ", size=(12, 1)), sg.FileBrowse(key="-FILE-", size=(8, 1))],
          [sg.Text("Encryption Key: ", size=(12, 1)), sg.In(size=(8, 1), enable_events=True, key="-KEY-")],
          [sg.Button("Ecrypt", key="-OK-"), sg.Text("File can't be empty", visible=False, key="-FileError-"),
           sg.Text("Key can't be empty", visible=False, key="-KeyError-"), sg.Text("Invalid key", visible=False, key="-Invalid-")]
        ]
window = sg.Window(title="Encrypt", layout=layout, margins=(100, 50))

while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == sg.WIN_CLOSED:
        break
    
    # The user Clicked Encrypt
    if event == "-OK-":
        # The File is Empty
        if not values["-KEY-"]:
            window["-FileError-"].update(visible=False)
            window["-KeyError-"].update(visible=True)
            continue

        # The Key is Empty
        elif not values["-FILE-"]:
            window["-KeyError-"].update(visible=False)
            window["-FileError-"].update(visible=True)
            continue
        
        key = values["-KEY-"]
        files = values["-FILE-"]
        
        # Check the Validity of Key MUST BE A NUMBER
        try:
            key = int(key)

        except:
            window["-FileError-"].update(visible=False)
            window["-KeyError-"].update(visible=False)
            window["-Invalid-"].update(visible=True)
            continue
        
        # Start Encrypting process
        else:
            f = open(files, "rb")
            reader = f.read()
            f.close()

            w = open(files, "wb")
            for l in reader:
                w.write(bytes([(l + key)%256]))
            w.close()

            # Add .encr Extension
            if (key > 0):
                os.rename(files, f"{files}.encr")

            # Remove .encr Extension
            elif (key < 0):
                os.rename(files, files[:-4])
        break

window.close()

