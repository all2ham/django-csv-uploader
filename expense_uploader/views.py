from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import File, Expense
import csv
from django.db import transaction
from .forms import UploadForm
import datetime
# Create your views here.

from django.http import HttpResponse


def index(request):
    expense_query = Expense.objects.all()
    context = {'expense_query' : expense_query}

    form = UploadForm()
    context['form'] = form

    return render(request, "expense_uploader/index.html", context)

# handles file upload and storage in database
def upload(request):
    f = request.FILES['csv_file']
    filedata = File(filename = f.name, raw = f)
    filedata.save()
    reader = csv.DictReader(f, delimiter = ',')
    with transaction.atomic():
        for row in reader:
            pre_tax_f = format_money_string(row['pre-tax amount'])
            tax_f = format_money_string(row['tax amount'])
            date_f = format_date_string(row['date'])
            record = Expense(
                date = date_f,
                category = row['category'],
                employee_name = row['employee name'],
                employee_address = row['employee address'],
                expense_description = row['expense description'],
                pre_tax_amount = pre_tax_f,
                tax_name = row['tax name'],
                tax_amount = tax_f,
                file = filedata
            )
            record.save()

            print(row['date'])

    return HttpResponseRedirect(reverse('e_up:index'))

# helper functions
def format_money_string(moneystring):
    s = moneystring.translate(None, ' ,$')
    return float(s)

def format_date_string(datestring):
    return datetime.datetime.strptime(datestring, '%m/%d/%Y')
