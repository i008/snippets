# get pdf metadata 
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
fp = open('46675457_3596.pdf', 'rb')
# fp = open('userIncome Sandra Höcker - 24.06.2016 (1).pdf', 'rb')
parser = PDFParser(fp)
doc = PDFDocument(parser)
print doc.info  # The "Info" metadata
