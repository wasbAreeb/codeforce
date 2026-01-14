

def is_rxc_format(s):
    if len(s) < 4 or s[0] != 'R' or not s[1].isdigit():
        return False
    
    c_index = s.find('C')
    if c_index == -1:
        return False

    row_part = s[1:c_index]
    col_part = s[c_index+1:]

    return row_part.isdigit() and col_part.isdigit() and row_part!="" and col_part != ""

def excel_to_rxc(s):
    col_letters = ""
    row = ""

    for char in s:
        if char.isalpa():
            col_letters += char
        else:
            row += char
        
    col_num = 0
    for letter in col_letters:
        col_num = col_num * 26 + ord(letter) - ord('A') + 1
    
    return f"R{row}C{col_num}"

def rxc_to_excel(s):
    c_index = s.find('C'
                     )
print(is_rxc_format(s))




