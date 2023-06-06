from django.http import HttpResponse
from django.template.loader import get_template
from io import BytesIO

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.platypus import Table, TableStyle

from pharmacy.models import Billing

def generate_pdf(request):
    # get the billing data
    billing = Billing.objects.all()

    # create a buffer to receive PDF data
    buffer = BytesIO()

    # create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=landscape(letter))

    # draw the Medical Name, Address and Logo
    p.drawString(1 * inch, 10.5 * inch, 'Nagrik Medical')
    p.drawString(1 * inch, 10.25 * inch, 'Karad')
    p.drawInlineImage('static/images/logo.png', 7 * inch, 10.25 * inch, width=1.5*inch, height=0.75*inch)


    # create a list of lists for the table
    data = [['Patient Name', 'Age', 'Mobile','Tablets', 'Quantity', 'Price', 'Total']]
    for bill in billing:
        data.append([
            bill.patient_name,
            bill.age,
            bill.mobile,
            bill.tablet,
            bill.quantity,
            bill.price,
            bill.total
        ])

    # create the table and style
    table = Table(data)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, 0), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('ALIGN', (0, 1), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('BOTTOMPADDING', (0, 1), (-1, -1), 8),
    ]))

    # draw the table
    table.wrapOn(p, 0, 0)
    table.drawOn(p, 0, 7.5 * inch)

    # calculate the total
    total = sum([float(bill.total) for bill in billing])

    # draw the total
    p.drawString(6 * inch, 0.5 * inch, f'Total: {total}')

    # Close the PDF object
    p.showPage()

    # get the buffer value
    pdf = buffer.getvalue()
    buffer.close()

    # create the HTTP response with PDF mime type
    response = HttpResponse(content_type='application/pdf')

    # set the Content-Disposition header to force download
    response['Content-Disposition'] = 'attachment; filename="billing.pdf"'

    # set the PDF content as response's content
    response.write(pdf)

    return response