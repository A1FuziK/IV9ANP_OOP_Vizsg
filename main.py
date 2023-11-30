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

    def szobaszamFoglalt(self, szobaszam):
        for szoba in self._szobak:
            if szoba.szobaszam == szobaszam:
                return True
        return False

    def szobaFelvesz(self, szoba: Szoba):
        if not self.szobaszamFoglalt(szoba.szobaszam):
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

print(szallodam)









def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


