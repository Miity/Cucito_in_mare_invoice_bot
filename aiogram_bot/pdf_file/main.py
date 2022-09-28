from .models import PDF
from .data import price_list
from fpdf.enums import XPos,YPos


f = PDF()
f.add_page()


f.set_a("Sig. Arturo Chiais Viale Mazzini 4, 00195 Roma")
f.set_oggetto("Preventivo lavori di tappezzeria APREA 16")
f.print_price_list(price_list)

f.s_footer()


f.output("./first.pdf")
