import os
from fpdf import FPDF
from fpdf.enums import XPos,YPos
import datetime


class PDF(FPDF):
    # unit='mm'
    format='A4'
    pdf_w=210
    pdf_h=297
    font="helvetica"
    filename = 'file'

    def lines(self):
        self.set_line_width(0.0)
        self.line(5.0,self.pdf_h-45.0,self.pdf_w-5.0,self.pdf_h-45.0) # bottom one


    def header(self):
        logo_width = 75
        self.x = self.pdf_w / 2 - logo_width/2
        self.y =10
        # Rendering logo:
        self.image("./logo.png", w=logo_width)

    
    def footer(self):
        self.lines()
        foot_text = "Tappezzeria Nautica Itinerante di Paone Francesco"
        foot_text_2 = "Sede LEGALE: Via del Colle Km 0,400 snc - 04024 Gaeta (LT) \nP.IVA: 03157820592"
        foot_text_3 = "BANCA: Monte dei Paschi di SIENA \n" + \
                    "SWIFT/BIC: PASCITMMGAE \n" + \
                    "IBAN: IT88M0103073990000001883187 intestato a Francesco Paone"

        self.set_y(self.pdf_h-40)

        self.set_font(self.font, "B", 8)
        self.cell(txt=foot_text)
        self.ln(3)
        self.set_font(self.font, "I", 6)
        self.multi_cell(w=100, txt=foot_text_2,)
        
        self.set_xy(x=-80,y=-40)
        self.set_font(self.font, size=8)
        self.multi_cell(w=0,h=None, txt=foot_text_3)
    
    def set_a(self, text):
        self.set_xy(x=80,y=40)
        self.set_font(self.font, size=12)
        self.cell(txt="A: " + text)
        
    
    def set_oggetto(self, text):
        self.set_xy(x=10,y=60)
        self.set_font("helvetica", size=12)
        self.cell(txt="Oggetto: " + text )
    
    def print_price_list(self, price_list):
        y_start = 80
        x_start = 10
        self.set_y(y_start)
        self.set_x(x_start)
        self.set_font(self.font, size=12)
        num = 1
        
        for obj in price_list:
            if self.y >= self.pdf_h - 100:
                self.add_page()
                self.x = 10
            txt = f'{num}. ' + obj['txt']
            width = self.pdf_w - x_start*2 - 30
            self.multi_cell(txt=txt, w=width, new_x=XPos.RIGHT, new_y=YPos.LAST)

            width = self.pdf_w - width - 10*2
            self.cell(w=width,align="R",txt=str(obj['price']) + ' euro', new_x=XPos.LEFT, new_y=YPos.NEXT)

            num += 1
            self.y += 5 
            self.x = x_start

        # Sum of price
        self.x = self.pdf_w - 10
        sum = 0
        for item in price_list:
            sum += item['price']
        txt = "Total price: " + str(sum)+ ' euro'
        self.x -= self.get_string_width(txt)
        self.cell(txt=txt, align="R")
        
        self.x = 10
        self.y += 10


    def s_footer(self):
        txt = "Prezzi senza applicazione dell IVA, effettuata ai sensi dell articolo 1, commi da 54 a 89, l. n. 190 del 2014 così come modificato dalla l. n. 208 del 2015 e dalla l. n. 145 del 2018"
        self.set_font("helvetica","I", size=10)
        self.multi_cell( w = self.pdf_w-10*2 , txt= txt, new_x=XPos.LEFT, new_y=YPos.NEXT)

        txt ="Condizioni di pagamento: acconto 50% inizio lavori, 50% a saldo alla consegna."
        self.y += 2
        self.set_font("helvetica", size=12)
        self.multi_cell( w = self.pdf_w-10*2 , txt= txt, new_x=XPos.LEFT, new_y=YPos.NEXT)

        txt = 'Date: ' + str(datetime.datetime.now().strftime("%Y.%m.%d"))
        print(txt)
        self.y += 5
        self.multi_cell(w= self.get_string_width(txt)+10 ,txt=txt, new_x=XPos.LEFT, new_y=YPos.NEXT)
