from random import choice

def selectFromList(options_dict: dict[str, str], question: str) -> str:
    options = list(options_dict.keys())
    print(f'\nSelect from the options below: ')
    for idx, option in enumerate(options):
        print(f"{str(idx + 1).rjust(len(str(len(options))))}) {option}")
        if idx == len(options) - 1:
            print('')
    
    inputValid = False
    while not inputValid:
        inputRaw = input(f"{question}: ")
        if inputRaw.isdigit() and 0 <= (inputIdx := int(inputRaw) - 1) < len(options):
            selected = options[inputIdx]
            print(f"\nYou selected: {selected}\n=========================================")
            inputValid = True
            break
        else:
            print(f'\n===================\nPlease select a valid response number.\n===================\n')

    if selected == 'you choose':
        selected = choice(options[:-1])

    return selected