## Projekt nr 2 - wtyczka do programu QGIS

WYMAGANIA SYSTEMOWE:
  - system Windows 10 lub 11
  - program QGIS (w wersji minimum 3.22)
  - python 3.11
  - biblioteka qgis.PyQt
  - biblioteka qgis.utils
  - biblioteka qgis.core
  - biblioteka os
  - biblioteka numpy


NAZWA WTYCZKI: Lenght and Area Counter


FUNKCJE WTYCZKI
  1. Różnica wysokości między dwoma punktami:
     
     Użytkownik, aby policzyć różnicę wysokości między punktami wybiera dokładnie dwa z grupy punktów znajdujących się na tej samej warstwie.
     Program pobierze wtedy wartości z tabeli atrybutów w programie QGIS, w której znajdują się wysokości tych punktów. Wtyczka odejmować będzie wysokość punktu              początkowego od wysokości punktu końcowego, co da wynik o znaku dodatnim bądź ujemnym w metrach - zależnie od tego w jakiej kolejności podamy nasze punkty. Na           podstawie znaku uzyskanego przewyższenia będzie można zatem stwierdzić, czy na wybranym odcinku nastąpił wzrost czy spadek terenu.
     
  2. Liczenie pola powierzchni pomiędzy zaznaczonymi punktami:
  
     Do obliczenia pola powierzchni między punktami należy z jednej warstwy wybrać przynajmniej trzy punkty. Następnie na podstawie współrzędnych tych 
     punktów, program metodą Gaussa policzy pole powierzchni zawarte między nimi i zapisze ten wynik w hektarach.

  3. Tworzenie poligonu:

     Użytkownik wybiera ponownie minimum trzy punkty (mogą to być te same co w poprzedniej opcji) oraz jednostkę, w której chce otrzymać pole poligonu spośród                dostępnych: ary, metry kwadratowe, hektary. Wtyczka z wybranych punktów stworzy poligon, doda na nową warstwę oraz obliczy jego pole powierzchni.

  4. Czyszczenie wyboru:
    Po wciśnieciu odpowiedniego przycisku wtyczka usuwa otrzymane wyniki (wybór warstwy oraz jednostki do liczenia poligonu zostaje ten sam) w oknie wtyczki i usuwa zaznaczenie punktu na aktywnej we wtyczce warstwie.

SPOSÓB UŻYCIA WTYCZKI:

1) Na samym początku należy pobrać wtyczkę i umieścić ją w folderze z wtyczkami (prawdopodobna ścieżka z wtyczkami Twojego urządzenia: "C:\Users\XXX\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins" ---- NALEŻY ZMIENIĆ "XXX" NA TWOJĄ NAZWĘ UŻYTKOWNIKA) a następnie załadować wtyczkę w programie QGIS.
2) Następnie wczytać trzeba mapę lub warstwę z punktami, która zawiera w tabeli atrybutów kolumnę o nazwie 'wysokosc' w której zapisane są wysokosci punktów, gdyż tylko przy takim zapisie wtyczka policzy przewyższenie między punktami.
3) Po wczytaniu mapy należy zaznaczyć na mapie odpowiednią liczbę punktów narzędziem o nazwie 'Zaznacz obiekty prostokątem lub kliknięciem'
4) Następnie w okienku wtyczki wybrać trzeba odpowiednią warstwę (najlepiej tą na której znajdują się zaznaczone punkty)
5) Po kliknięciu odpowiedniej funkcji, wtyczka wykona wybrane polecenie i policzy wybraną wartość. Jeśli użytkownik nie wybierze wymaganej do wykonania wybranej operacji liczby punktów program wyświetli komunikat o powstałym błędzie.
 
UWAGI KOŃCOWE:
Wtyczka w swoim opisie w QGIS ma błędnie zapisane, że liczy ona długość między punktami, a nie przewyższenie. Jest to błąd powstały przy tworzeniu plików wtyczki i który zauważony został dopiero po napisaniu całego kodu wtyczki, dlatego nie został on niestety zmieniony.

    
