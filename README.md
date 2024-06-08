# Projekt nr 2 - wtyczka do programu QGIS

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
     Program pobierze wtedy wartości z tabeli atrybutów w programie QGIS z ?kolumny o nazwie 'h_plevrf2007nh'?, w której znajdują się 
     wysokości tych punktów. Wtyczka odejmować będzie wysokość punktu początkowego od wysokości punktu końcowego, co da wynik o znaku 
     dodatnim bądź ujemnym - zależnie od tego w jakiej kolejności podamy nasze punkty. Na podstawie znaku uzyskanego przewyższenia 
     będzie można zatem stwierdzić, czy na wybranym odcinku nastąpił wzrost czy spadek terenu.
     
    
