def abecedario():
    abcd = 'abcdefghijklmnñopqrstuvwxyz'
    return abcd

def cesar_decode(t, a):
    final_code = ''
    list_code = []
    t = t.lower()
    
    for x in range(28):
        if final_code != '':
            list_code.append(final_code)
        final_code = ''
        for i in range(len(t)):
            char = t[i]
            if char == ' ':
                final_code+=' '
            elif char == ',':
                final_code+=','
            else:
                pos = a.index(char)
                final_char = a[pos-x]
                final_code+=final_char
            
    return list_code

## PROGRAMA ##

texto_a_decodificar = 'xjw t rt xjw, jxf jx pf hzjxyntr'
abc = abecedario()
results = cesar_decode(texto_a_decodificar, abc)
print('='*len(texto_a_decodificar))
for result in results:
    print (result)
print('='*len(texto_a_decodificar))