def get_char_type(char):
    if char.isalpha() or char == '_':
        return 'a'  
    elif char.isdigit():
        return 'b'  
    else:
        return 'c'  

def validate_variable_name(input_string):
    transition_table = {
        'q0': {'a': 'q1', 'b': 'q2', 'c': 'q2'},
        'q1': {'a': 'q1', 'b': 'q1', 'c': 'q2'},
        'q2': {'a': 'q2', 'b': 'q2', 'c': 'q2'}
    } 
    
    current_state = 'q0'
    if not input_string:
        return "TIDAK VALID", "q0"
        
    jejak = f"{current_state}"
    for char in input_string:
        char_type = get_char_type(char)
        current_state = transition_table[current_state][char_type]
        jejak += f" -({char})-> {current_state}"
        
    if current_state == 'q1':
        return "VALID", jejak
    else:
        return "TIDAK VALID", jejak

def main():
    print("=== DFA Validasi Variabel === \n(Ketik 'q' untuk keluar)")
    
    while True:
        string_input = input("\nInput Variabel: ")
        
        if string_input.lower() == 'q':
            break
            
        status, jejak = validate_variable_name(string_input)
        
        print(f"Alur State  : {jejak}")
        print(f"Status : {status}")

if __name__ == "__main__":
    main()