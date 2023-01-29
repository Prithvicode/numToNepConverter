import PySimpleGUI as sg

layout = [[sg.Input(key = '-INPUT-')],[sg.Spin(values=["Num to Nepali" , "Km to Miles"], key = '-TYPE-')],
         [sg.Button("Convert",key = '-CONVERT-')]]

window = sg.Window('Converter',layout)

numToNep = {"1":"१","2":"२","3":"३","4":"४","5":"५","6":"६","7":"७", "8":"८","9":"९","0":"०" }

def numToNepali(strings):
    nepDigit = ''
    for num in strings:
       nepDigit = f"{nepDigit}{numToNep[num]}"

    return nepDigit


while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break

    if event == '-CONVERT-':
        inputVal = values['-INPUT-']
        if inputVal.isnumeric():
            match values['-TYPE-']:
                case 'Km to Miles':
                    outVal = float(inputVal) * 0.062
                    outDisplay = f'{inputVal} Km is {outVal} Miles.'
                
                case 'Num to Nepali':
                    outVal = numToNepali(inputVal)
                    outDisplay = outVal

            window['-INPUT-'].update(outDisplay)

    
window.close()