import sys
import PyPDF2
import pandas as pd
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QLabel

class PDFtoExcelApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 400, 200)
        self.setWindowTitle('PDF to Excel')

        self.label = QLabel(self)
        self.label.setText('Selecione um arquivo PDF:')
        self.label.move(20, 20)

        self.btn_select_pdf = QPushButton('Selecionar PDF', self)
        self.btn_select_pdf.move(20, 50)
        self.btn_select_pdf.clicked.connect(self.selectPDF)

        self.btn_convert = QPushButton('Converter para Excel', self)
        self.btn_convert.move(20, 80)
        self.btn_convert.setEnabled(False)
        self.btn_convert.clicked.connect(self.convertToExcel)

    def selectPDF(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        pdf_file, _ = QFileDialog.getOpenFileName(self, 'Selecionar PDF', '', 'PDF Files (*.pdf)', options=options)

        if pdf_file:
            self.pdf_file = pdf_file
            self.btn_convert.setEnabled(True)

    def convertToExcel(self):
        pdf_reader = PyPDF2.PdfFileReader(open(self.pdf_file, 'rb'))
        num_pages = pdf_reader.numPages

        df = pd.DataFrame(columns=['Page', 'Text'])

        for page_num in range(num_pages):
            page = pdf_reader.getPage(page_num)
            text = page.extractText()
            df = df.append({'Page': page_num + 1, 'Text': text}, ignore_index=True)

        excel_file = 'output.xlsx'
        df.to_excel(excel_file, index=False)

        self.label.setText(f'PDF convertido para Excel em {excel_file}')

def main():
    app = QApplication(sys.argv)
    ex = PDFtoExcelApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
