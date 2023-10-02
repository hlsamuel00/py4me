from random import choice

def selectFromList(options_dict: dict[str, str], question: str) -> str:
    options = list(options_dict.keys())
    print(f'Select from the options below: ')
    for idx, option in enumerate(options):
        print(f"{str(idx + 1).rjust(len(str(len(options))))}) {option}")
        if idx == len(options) - 1:
            print('')
    
    inputValid = False
    while not inputValid:
        inputRaw = input(f"{question}: ")
        inputIdx = int(inputRaw) - 1
        if inputIdx >= 0 and inputIdx < len(options):
            selected = options[inputIdx]
            print(f"You selected: {selected}\n=========================================")
            inputValid = True
            break
        else:
            print(f'Please select a valid response number.')

    if selected == 'you choose':
        selected = choice(options[:-1])

    return selected