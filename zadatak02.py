#Korisnik unosi rečenicu koja mora biti minimalne duljine 10 znakova
#Napišite funkciju koja broji samoglasnike unutar te rečenice

def prebrojiSamoglasnike(recenica):
    samoglasnici = ['a', 'e','i','o','u']
    testiranje = recenica.lower()
    brojac = 0
    for i in testiranje:
        for j in samoglasnici:
            if i == j:
                #print(i)
                brojac+=1
    return brojac

def prebrojiSamoglasnike2(recenica):
    samoglasnici = ['a', 'e','i','o','u']
    testiranje = recenica.lower()
    for samoglasnici in testiranje:
        print(testiranje)

unos = str(input("Molimo vas unesite rečenicu, minimalna dužina je 10 znakova!: "))
if len(unos) <= 10:
    print("Unesena rečenica je premala!")


duzina = prebrojiSamoglasnike(unos)
#print(duzina)
prebrojiSamoglasnike2(unos)