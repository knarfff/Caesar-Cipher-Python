def abecedario():
    abcd = 'abcdefghijklmnñopqrstuvwxyz'
    return abcd

 
def cesar_code(t, a, m):
    final_code = ''
    t = t.lower()
    
    for i in range(len(t)):
        char = t[i]
        if char == ' ':
            final_code+=' '
        elif char == ',':
            final_code+=','
        else:
            pos = a.index(char)
            if (pos + m) >= 27:
                j = 1
                while (pos + j) <= 27:
                    j+=1
                final_char = a[m-j+1] 
                final_code+=final_char
            else:
                final_char = a[(pos+m)]
                final_code+=final_char
    return final_code

# PROGRAMA #

texto_a_cifrar = 'Ser o no ser, esa es la cuestion'
movimiento = 5
abc = abecedario()
result = cesar_code(texto_a_cifrar, abc, movimiento)
print('='*len(texto_a_cifrar))
print(result)
print('='*len(texto_a_cifrar))