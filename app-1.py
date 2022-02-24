"""
    Pliki o rozszerzeniu .ini to proste pliki do
    przechowania danych konfiguracyjnych Twojej aplikacji.
    Charakteryzuje je prosta struktura i możliwość
    przejrzystego grupowania danych w sekcje.
    Zawartość plików o rozszerzeniu .ini w Python możesz
    odczytać za pomocą wbudowanej biblioteki
    configparser.
    Odczytajmy zawartość przykładowego pliku data.ini
"""

from configparser import ConfigParser
from typing import Final

if __name__ == '__main__':
    INI_FILENAME: Final = 'data.ini'

    # Tworzymy specjalny obiekt o nazwie config
    # i wypełniamy go danymi pobranymi z pliku o
    # rozszerzeniu .ini
    config = ConfigParser()
    config.read(INI_FILENAME)

    print("=============== (1) ===============")
    # odczytujemy nazwy sekcji z pliku
    print(config.sections())

    print("=============== (2) ===============")
    # odczytujemy konkretne dane z pliku
    print(config.get('DATABASE', 'USERNAME'))
    print(config['DATABASE']['USERNAME'])

    print("=============== (3) ===============")
    # Pobieranie danych z pliku za pomoca funkcji
    # specyfikujących typ danych
    print(config.getfloat('APP', 'VERSION'))
    print(config.getint('DATABASE', 'PORT'))