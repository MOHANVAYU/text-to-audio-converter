#book to mp3 convertor
#import pyttsx3 library using pip install pyttsx3 in cmd
import pyttsx3

book=open(r"py_book.txt")
book_text=book.readlines()

engine=pyttsx3.init()

engine.save_to_file(book_text,'book.mp3')
engine.runAndWait()