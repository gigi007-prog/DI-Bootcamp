matrix = [
    ['7', 'i', 'i'],
    ['T', 's', 'x'],
    ['h', '%', '?'],
    ['i', ' ', '#'],
    ['s', 'M', ' '],
    ['$', 'a', ' '],
    ['#', 't', '%'],
    ['^', 'r', '!']
]

def solve_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    decoded_message = ""
    
    for column in range(cols):
        temp = ""  
        
        for row in range(rows):
            structure = matrix[row][column]
            
            if structure.isalpha():
                temp += structure
            elif temp:  
                temp += " " 
        
        decoded_message += temp

    return decoded_message


decoded_message = solve_matrix(matrix)
print(decoded_message)

            