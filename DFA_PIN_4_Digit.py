def get_char_type(char):
    if char.isdigit():
        return 'D'  
    else:
        return 'O'  

def validate_pin_4_digit(input_string):
    transition_table = {
        'q0': {'D': 'q1', 'O': 'q5'},
        'q1': {'D': 'q2', 'O': 'q5'},
        'q2': {'D': 'q3', 'O': 'q5'},
        'q3': {'D': 'q4', 'O': 'q5'},
        'q4': {'D': 'q5', 'O': 'q5'}, 
        'q5': {'D': 'q5', 'O': 'q5'}  
    }
   
    current_state = 'q0'
    if not input_string:
        return "TIDAK VALID", "q0"
       
    jejak = f"{current_state}"
    for char in input_string:
        char_type = get_char_type(char)
        current_state = transition_table[current_state][char_type]
        jejak += f" -({char})-> {current_state}"
       
    if current_state == 'q4':
        return "VALID", jejak
    else:
        return "TIDAK VALID", jejak

def main():
    print("=== DFA Validasi PIN Angka 4 Digit === \n(Ketik 'q' untuk keluar)")
   
    while True:
        string_input = input("\nInput PIN: ")
       
        if string_input.lower() == 'q':
            break
           
        status, jejak = validate_pin_4_digit(string_input)
       
        print(f"Alur State  : {jejak}")
        print(f"Status      : {status}")

if __name__ == "__main__":
    main()