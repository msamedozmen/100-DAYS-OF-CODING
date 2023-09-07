import PyPDF3
import pyttsx3



my_data = open("Cilvez_Özmen_SDP_FinalReport.pdf","rb")

pdfReader  = PyPDF3.PdfFileReader(my_data)

from_page = pdfReader.getPage(1)
text = from_page.extractText()
speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()