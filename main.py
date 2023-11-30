import datetime
from abc import ABC, abstractmethod

class Szoba(ABC):
    _ar: int
    _szobaszam: int

    def get_ar(self):
        return self._ar

    def set_ar(self, ar: int):
        self._ar = ar

    ar = property(get_ar,set_ar)

    def get_szobaszam(self):
        return self._szobaszam

    def set_szobaszam(self, szobaszam: int):
        self._szobaszam = szobaszam

    szobaszam = property(get_szobaszam,set_szobaszam)

    @abstractmethod
    def Tipusnev(self):
        pass

class EgyagyasSzoba(Szoba):
    def __init__(self, szobaszam: int):
        self.ar = 16000
        self.szobaszam = szobaszam
        pass

    def Tipusnev(self):
        return "EgyagyasSzoba"

class KetagyasSzoba(Szoba):
    _lakosztaly: bool

    def __init__(self, szobaszam: int):
        self.ar = 23500
        self.szobaszam = szobaszam
        self._lakosztaly = False
        pass

    def Tipusnev(self):
        return "KetagyasSzoba"

    def get_lakosztaly(self):
        return self._lakosztaly

    def set_lakosztaly(self, lakosztaly: bool):
        self._lakosztaly = lakosztaly

    lakosztaly = property(get_lakosztaly,set_lakosztaly)


class Foglalas:
    _szoba: Szoba
    _datum: datetime

    def __init__(self, szoba: Szoba, datum: datetime):
        self._datum = datum
        self._szoba = szoba

class Szalloda:
    _szobak: list
    _foglalasok: list
    _nev: str

    def __init__(self):
        self._szobak = list()
        self._foglalasok = list()
        self._nev = "Szállj Szabadon Szálloda"

    def listSzobak(self):
        print(f'Szobák a {self._nev} szállodában.\n')
        for szoba in self._szobak:
            print(f'\tSzobaszám: {szoba.szobaszam} {szoba.Tipusnev()}  Ár: {szoba.ar}\n')
    def listFoglalasok(self):
        print(f'Foglalások a {self._nev} szállodában.\n')
        for foglalas in self._foglalasok:
            print(f'\tSzobaszám: {foglalas._szoba.szobaszam} {foglalas._szoba.Tipusnev()}  Dátum: {foglalas._datum}  Ár: {foglalas._szoba.ar}\n')
    def get_Foglalas(self, szobaszam: int, datum: datetime):
        for foglalas in self._foglalasok:
            if foglalas._szoba.szobaszam == szobaszam:
                if foglalas._datum == datum:
                    return foglalas
        return None

    def is_szobaFoglalt(self, szobaszam: int, datum: datetime):
        for foglalas in self._foglalasok:
            if foglalas._szoba.szobaszam == szobaszam:
                if foglalas._datum == datum:
                    return True
        return False

    def get_Szoba(self, szobaszam: int):
        for szoba in self._szobak:
            if szoba.szobaszam == szobaszam:
                return szoba
        return None

    def szobaLemond(self, szobaszam: int, datum: datetime):
        if datum <= datetime.date.today():
            print(f'A megadott dátum {datum} nem jó. Csak jövőbeni dátum adható meg!')
            return None

        if self.szobaszamLetezik(szobaszam):
            if self.is_szobaFoglalt(szobaszam,datum):
                szoba = self.get_Szoba(szobaszam)
                foglalas = self.get_Foglalas(szobaszam,datum)
                self._foglalasok.remove(foglalas)

                print(f'A szoba {szobaszam} erre a napra {datum} felszabadítva! Ára: {szoba.ar}.\n')
                return szoba.ar * -1
            else:
                print(f'A szoba {szobaszam} ezen a napon {datum} nem foglalt!\n')
            pass
        else:
            print(f'A szobaszám {szobaszam} nem létezik!\n')

        return None


    def szobaFoglal(self, szobaszam: int, datum: datetime):
        if datum <= datetime.date.today():
            print(f'A megadott dátum {datum} nem jó. Csak jövőbeni dátum adható meg!')
            return None

        if self.szobaszamLetezik(szobaszam):
            if not self.is_szobaFoglalt(szobaszam,datum):
                szoba = self.get_Szoba(szobaszam)
                self._foglalasok.append(Foglalas(szoba,datum))

                print(f'A szoba {szobaszam} erre a napra {datum} befoglalva! Ára: {szoba.ar}.\n')
                return szoba.ar
            else:
                print(f'A szoba {szobaszam} ezen a napon már {datum} foglalt!\n')
            pass
        else:
            print(f'A szobaszám {szobaszam} nem létezik!\n')

        return None

    def szobaszamLetezik(self, szobaszam):
        for szoba in self._szobak:
            if szoba.szobaszam == szobaszam:
                return True
        return False

    def szobaFelvesz(self, szoba: Szoba):
        if not self.szobaszamLetezik(szoba.szobaszam):
            self._szobak.append(szoba)
            print(f'Szoba felvéve:{szoba.szobaszam}\n')
        else:
            print(f'A szobaszám már foglalt:{szoba.szobaszam}\n')

    @property
    def nev(self):
        return self._nev







szobaszam = 0

def GetNextSzobaszam():
    global szobaszam
    szobaszam = szobaszam + 1
    return szobaszam



szallodam = Szalloda()
szallodam.szobaFelvesz(EgyagyasSzoba(GetNextSzobaszam()))
szallodam.szobaFelvesz(EgyagyasSzoba(GetNextSzobaszam()))
szallodam.szobaFelvesz(KetagyasSzoba(GetNextSzobaszam()))

#Szobaszám teszt
szallodam.szobaFoglal(0,datetime.datetime.strptime('2099.12.21', '%Y.%m.%d').date())

#Múltidő teszt
szallodam.szobaFoglal(0,datetime.datetime.strptime('2001.12.21', '%Y.%m.%d').date())


print('A foglalás eredménye:' + str(szallodam.szobaFoglal(1,datetime.datetime.strptime('2023.12.21', '%Y.%m.%d').date())))
print('A foglalás eredménye:' + str(szallodam.szobaFoglal(2,datetime.datetime.strptime('2023.12.22', '%Y.%m.%d').date())))
print('A foglalás eredménye:' + str(szallodam.szobaFoglal(3,datetime.datetime.strptime('2023.12.23', '%Y.%m.%d').date())))
print('A foglalás eredménye:' + str(szallodam.szobaFoglal(2,datetime.datetime.strptime('2023.12.27', '%Y.%m.%d').date())))
print('A foglalás eredménye:' + str(szallodam.szobaFoglal(3,datetime.datetime.strptime('2023.12.29', '%Y.%m.%d').date())))

#Újrafoglalás teszt
szallodam.szobaFoglal(1,datetime.datetime.strptime('2023.12.21', '%Y.%m.%d').date())
szallodam.szobaFoglal(2,datetime.datetime.strptime('2023.12.22', '%Y.%m.%d').date())
szallodam.szobaFoglal(3,datetime.datetime.strptime('2023.12.23', '%Y.%m.%d').date())

#Lemondás tesztelése
print('A foglalás eredménye:' + str(szallodam.szobaFoglal(1,datetime.datetime.strptime('2023.12.31', '%Y.%m.%d').date())))
print('A foglalás eredménye:' + str(szallodam.szobaFoglal(2,datetime.datetime.strptime('2023.12.31', '%Y.%m.%d').date())))

print('A lemondás eredménye:' + str(szallodam.szobaLemond(1,datetime.datetime.strptime('2001.12.31', '%Y.%m.%d').date())))
print('A lemondás eredménye:' + str(szallodam.szobaLemond(1,datetime.datetime.strptime('2099.12.31', '%Y.%m.%d').date())))

print('A lemondás eredménye:' + str(szallodam.szobaLemond(1,datetime.datetime.strptime('2023.12.31', '%Y.%m.%d').date())))
print('A lemondás eredménye:' + str(szallodam.szobaLemond(2,datetime.datetime.strptime('2023.12.31', '%Y.%m.%d').date())))

szallodam.listFoglalasok()

#print(datetime.datetime.strptime('1976.12.01', '%Y.%m.%d').date())
#print(datetime.date.today())
#print(szallodam)

def FoglalUser():
    print('Foglalás menü:')
    str_szobaszam = input('Adja meg a szobaszámot:')
    str_datum = input('Adja meg a dátumot (ÉÉÉÉ.HH.NN):')

    try:
        i_szoba = int(str_szobaszam)
        try:
            d_datum = datetime.datetime.strptime(str_datum, '%Y.%m.%d').date()
            szallodam.szobaFoglal(i_szoba,d_datum)
        except:
            print('A dátum nem tűnik jónak...')
    except:
        print('A szobaszám nem tűnik jónak...')

    pass

def LemondUser():
    print('Lemondás menü:')
    str_szobaszam = input('Adja meg a szobaszámot:')
    str_datum = input('Adja meg a dátumot (ÉÉÉÉ.HH.NN):')

    try:
        i_szoba = int(str_szobaszam)
        try:
            d_datum = datetime.datetime.strptime(str_datum, '%Y.%m.%d').date()
            szallodam.szobaLemond(i_szoba,d_datum)
        except:
            print('A dátum nem tűnik jónak...')
    except:
        print('A szobaszám nem tűnik jónak...')

    pass


while True:
    print(f'Szálloda {szallodam.nev} ...')
    print('0: Listázás (szobák)')
    print('1: Listázás (foglalások)')
    print('2: Foglalás')
    print('3: Lemondás')
    print('4: Kilép')
    inputresult = input('Válasszon funkciót:')
    if inputresult == '4':
        break
    elif inputresult == '0':
        szallodam.listSzobak()
        pass
    elif inputresult == '1':
        szallodam.listFoglalasok()
        pass
    elif inputresult == '2':
        FoglalUser()
        pass
    elif inputresult == '3':
        LemondUser()
        pass
    pass

