import os
import csv
import statistics
from django.shortcuts import render
from teste.settings import APPS_DIR
from exemplo.models import Vunerability
from django.core.files.storage import FileSystemStorage


# Create your views here.

def upload_cartorios(request):
    arquivo = request.FILES['file']
    fs = FileSystemStorage()
    filename = fs.save(arquivo.name, arquivo )
    uploaded_file_url = fs.url(filename)
    diretorio = os.path.dirname(os.path.dirname(filename))
    diretorio_arquivo = '{}{}{}'.format(APPS_DIR,diretorio,uploaded_file_url)
    with open(diretorio_arquivo, encoding='utf-8') as f:
        csv_reader = csv.reader(f, delimiter=';')
        csv_reader.__next__()
        for row in csv_reader:
            dic = {
                'hostname': row[0],
                'ip_address': row[1], 
                'vulnerability_severity': row[2], 
                'vulnerability_cvss': row[3],
                'vulnerability_publication_date': row[4],
                }

            Vunerability(**dic).save()



def calculator(request):
    my_list = Vunerability.objects.all().values_list('vulnerability_severity')
    moda = statistics.mode(my_list)

    low = Vunerability.objects.filter(choices=0).count()
    medium = Vunerability.objects.filter(choices=1).count()
    high = Vunerability.objects.filter(choices=2).count()
    danger = Vunerability.objects.filter(choices=3).count()
    
    context = {
        'max_result': moda,
        'low': low,
        'medium': medium,
        'high': high,
        'danger': danger
    }

    return render(request,  context)