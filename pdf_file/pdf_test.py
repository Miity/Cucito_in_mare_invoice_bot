from pdf_file.models import PDF
from aiogram_bot.data.test_data import price_list

f = PDF()
f.add_page()

f.set_client_name("Anna Paone")
f.set_client_adress("Sig. Arturo Chiais Viale Mazzini 4, 00195 Roma")
f.set_oggetto("Preventivo lavori di tappezzeria APREA 16")
f.print_price_list(price_list)
f.s_footer()


f.set_filename('newfile_name')
f.output(f.filename)
