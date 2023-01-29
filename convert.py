import PySimpleGUI as sg

layout = [[sg.Input(key = '-INPUT-')],[sg.Spin(values=["Km to Miles","kg to lbs"], key = '-TYPE-')],[sg.Button("Convert",key = '-CONVERT-')],
        [sg.Text("OUTPUT",key = '-TEXT-')]]

window = sg.Window('converter',layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        inputVal = values['-INPUT-']
        if inputVal.isnumeric():
            match values['-TYPE-']:
                case 'Km to Miles':
                    outVal = float(inputVal) * 0.06 
                    outDisplay = f'{inputVal} km is {outVal} Miles.'

            window['-INPUT-'].update(outDisplay)
    



window.close()