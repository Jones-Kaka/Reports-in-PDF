import jinja2
import pdfkit 
from wkhtmltopdf.views import PDFTemplateView
from datetime import datetime

client_name = "Frank Andrade"
item1 = "Balls"
item2 = "Players Jazzy"
item3 = "Playing Trainers"
item4 = "Players Travel Budget"
item5 = "Players Allowance"

subtotal1 = 250
subtotal2 = 450
subtotal3 = 500
subtotal4 = 15000
subtotal5 = 30500
total = subtotal1 + subtotal2 + subtotal3 + subtotal4 + subtotal5

today_date = datetime.today().strftime("%d %b, %Y")
month = datetime.today().strftime("%B")

context = {'client_name': client_name, 'today_date': today_date, 'total': f'${total:.2f}', 'month': month,
           'item1': item1, 'subtotal1': f'${subtotal1:.2f}',
           'item2': item2, 'subtotal2': f'${subtotal2:.2f}',
           'item3': item3, 'subtotal3': f'${subtotal3:.2f}',
           'item4': item4, 'subtotal4': f'${subtotal4:.2f}',
           'item5': item5, 'subtotal5': f'${subtotal5:.2f}'
           }

template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

html_template = 'invoice.html'
template = template_env.get_template(html_template)
output_text = template.render(context)

config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')
output_pdf = 'invoice.pdf'
pdfkit.from_string(output_text, output_pdf, configuration=config, css='invoice.css')