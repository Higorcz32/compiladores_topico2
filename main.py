import re


#text = 'guihss.cs@gmail.com'

#print(re.split(r'\w+', text))
#print(re.fullmatch(r'[\w.]+@[\w.]+', text) is not None)
#print(re.search(r'[\w.]+@[\w.]+', text))
#print(re.finditer(r'[\w.]+@[\w.]+', text))

#for m in re.finditer(r'([\w.])+@([\w.])+', text):
    #print(m.group(2) + '@' + m.group(1))



#text = 'hoje o dia foi lindo'

#print(re.sub(r'([ao])\b', 'e'), text)

def questao01(texto):
    return texto.split(" ")

def questao02(texto):
    texto = re.sub("a", "o", texto)
    return texto

def questao03(texto):
    texto = re.sub("o\s", "os", texto)
    return texto

#def questao04(texto):
    #for i in reversed(list(re.finditer(r"([0-9]+)", texto))):

def questao05(numero):
    return (True if re.fullmatch(r"[0-9]+[.,][0-9]+", numero) is not None else False)

def questao06(texto):
    return [m.group(1) for m in re.finditer(r"<(\w+)", texto)]

def questao07(texto):
    return [m.group(1) for m in re.finditer(r".*/\*(.+)\*/.*", texto)]

def questao08(texto):
    for m in re.finditer(r"(.*): (.*)", texto):
        return m.group(2) + ": " + m.group(1)

def questao11(texto):
    contador = 0
    for m in re.finditer(r"a", texto):
        contador += 1

    return True if contador%2==1 else False

if __name__ == '__main__':

    texto1 = "Hoje o dia esta lindo."
    print("1: " + str(questao01(texto1)))

    texto2 = "A maria esta bonita."
    print("2: " + questao02(texto2))

    texto3 = "tolo, bobo, roxo."
    print("3: " + questao03(texto3))

    texto5 = ["5", "4.6", "20", "1.8", "3", "8.5"]

    print("\n5:")
    print(texto5)
    for n in texto5:
        print(questao05(n))
    print("")

    texto6 = """<html>
                <head>
                        <title>Título da página</title>
                        <meta charset="utf-8"/>
                </head>
                <body>

                </body>
                </html>"""
    print("6: " + str(questao06(texto6)))

    texto7 = """texto texto 
        /*bloco 1 */
        texto texto /*bloco 2*/ texto texto"""
    print("7: " + str(questao07(texto7)))

    texto8 = ["Key1: 11224", "Key2: 524", "Key3: 5125", "Abc: 51252"]

    print("\n8:")
    for i in texto8:
        print(questao08(i))
    print("")

    texto11 = "balas, frutas, amoras"
    print("11: " + str(questao11(texto11)))