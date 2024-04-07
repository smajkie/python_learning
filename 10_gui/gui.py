import fib as f
import PySimpleGUI

label = PySimpleGUI.Text('Kliknij po nastepnego FIbka')                       # text 
input_box = PySimpleGUI.InputText()                                           # okienko inputu
button = PySimpleGUI.Button("FIBEK")

#window = PySimpleGUI.Window('FIBONACHI', layout=[[label, input_box]])        # korzystamy z obiektu tej klasy i nadajemy mu tytul, layout oczekuje listy i jest per wiersz
window = PySimpleGUI.Window('FIBONACHI', layout=[[label, button], [input_box]])       # jak zrobimy tak to label z wierszem i input beda w osobnych wierszach
window.read()                                                                 # wyswietla stworzone okno
window.close()


