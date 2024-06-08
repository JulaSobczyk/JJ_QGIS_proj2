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

FUNKCJE WTYCZKI
  1. Różnica wysokości między dwoma punktami
     
     Użytkownik, aby policzyć różnicę wysokości między punktami wybiera dokładnie dwa z grupy punktów znajdujących się na tej samej warstwie.
     Program pobierze wtedy wartości z tabeli atrybutów w programie QGIS, w której znajdują się wysokości tych punktów. Wtyczka odejmować będzie wysokość punktu              początkowego od wysokości punktu końcowego, co da wynik o znaku dodatnim bądź ujemnym w metrach - zależnie od tego w jakiej kolejności podamy nasze punkty. Na           podstawie znaku uzyskanego przewyższenia będzie można zatem stwierdzić, czy na wybranym odcinku nastąpił wzrost czy spadek terenu.
     
  2. Liczenie pola powierzchni pomiędzy zaznaczonymi punktami
  
     Do obliczenia pola powierzchni między punktami należy z jednej warstwy wybrać przynajmniej trzy punkty. Następnie na podstawie współrzędnych tych 
     punktów, program metodą Gaussa policzy pole powierzchni zawarte między nimi i zapisze ten wynik w hektarach.

  3. Tworzenie poligonu

     Użytkownik wybiera ponownie minimum trzy punkty (mogą to być te same co w poprzedniej opcji) oraz jednostkę, w której chce otrzymać pole poligonu spośród                dostępnych: ary, metry kwadratowe, hektary. Wtyczka z wybranych punktów stworzy poligon, doda na nową warstwę oraz obliczy jego pole powierzchni.

  4. Czyszczenie wyboru
    Po wciśnieciu odpowiedniego przycisku wtyczka usuwa otrzymane wyniki (wybór warstwy oraz jednostki do liczenia poligonu zostaje ten sam) w oknie wtyczki i usuwa         zaznaczenie punktu na aktywnej we wtyczce warstwie.
     
     
 
     

    
