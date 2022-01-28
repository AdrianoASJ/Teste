import os
import csv
import statistics
from django.shortcuts import render
from teste.settings import APPS_DIR
from exemplo.models import Vunerability
from django.core.files.storage import FileSystemStorage
from rest_framework.response import Response
from datetime import datetime

# Create your views here.
def upload_cartorios(request):
    try:
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
                    'title': row[2],
                    'vulnerability_severity': row[3], 
                    'vulnerability_cvss': row[4],
                    'vulnerability_publication_date': datetime.strptime(row[5], '%Y-%m-%d'),
                    }

                Vunerability(**dic).save()

        return Response({"status": 200, "message": "importação realizada com sucesso"})
    except Exception as e:
        return Response({"status": 300, 'error': e})



def calculator(request):
    try:
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

        return Response({"status": 200, "result": context})
    except Exception as e:
        return Response({"status": 300, 'error': e})