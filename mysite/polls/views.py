from django.shortcuts import render
from django.http import HttpResponse
from .models import DataDjango, DataDjango2
from collections import Counter
import numpy as np
import pandas as pd
from json import dumps

# Create your views here.
def index(request):

    context = {}

    # Emosi Bahagia Maps
    locationsArrayFix = []
    list_data = DataDjango.objects.all()
    for field in list_data:
        locationsArray= []
        locations = field.locations
        locationsArray.append(locations)
        with open('polls/provinsi-id.csv', 'r') as file:
            for line in file:
                clear_line = line.replace("\n", '').strip()
                province, code_province = clear_line.split(',')
                if province in locationsArray:
                    locationsArrayFix.append(code_province)
    counterArray = Counter(locationsArrayFix)
    valueArray = counterArray.values()
    text2 =[]
    for text in counterArray:
        text2.append(text)
    value2 =[]
    for value in valueArray:
        value2.append(value)
    fixVar = [[f,c] for f,c in zip(text2,value2)]
    context["happy_emotion_maps"] = fixVar

    # Emosi Tidak Bahagia Maps
    locationsArrayFix2 = []
    list_data2 = DataDjango2.objects.all()
    for field2 in list_data2:
        locationsArray2= []
        locations2 = field2.locations
        locationsArray2.append(locations2)
        with open('polls/provinsi-id.csv', 'r') as file2:
            for line2 in file2:
                clear_line2 = line2.replace("\n", '').strip()
                province2, code_province2 = clear_line2.split(',')
                if province2 in locationsArray2:
                    locationsArrayFix2.append(code_province2)
    counterArray2 = Counter(locationsArrayFix2)
    valueArray2 = counterArray2.values()
    text3 =[]
    for text2 in counterArray2:
        text3.append(text2)
    value3 =[]
    for value2 in valueArray2:
        value3.append(value2)
    fixVar2 = [[f2,c2] for f2,c2 in zip(text3,value3)]

    context["unhappy_emotion_maps"] = fixVar2

    # Month Data
    month = []
    with open('polls/month.csv', 'r') as file_month:
        for line_month in file_month:
            clear_line_month = line_month.replace("\n", '').strip()
            month.append(clear_line_month)    
    
    # Emosi Bahagia Bar
    arrayCreated =[]
    list_data_bar = DataDjango.objects.all()
    for field_bar in list_data_bar:
        created_at = field_bar.created_at
        punctuation_created_at = created_at.split()
        for tokenized_created_at in punctuation_created_at:
            if tokenized_created_at in month:
                arrayCreated.append(tokenized_created_at)

    countCreated = Counter(arrayCreated)
    valueArray = countCreated.values()

    valueCreated = []
    for value_created in valueArray:
        valueCreated.append(value_created)
    context["value_happy_bar"] = valueCreated

    monthCreated = []
    for month_created in countCreated:
        monthCreated.append(month_created)
    context["month_happy_bar"] = monthCreated

   
    # Emosi Tidak Bahagia Bar
    arrayCreated2 =[]
    list_data_bar2 = DataDjango2.objects.all()
    for field_bar2 in list_data_bar2:
        created_at2 = field_bar2.created_at
        punctuation_created_at2 = created_at2.split()
        for tokenized_created_at2 in punctuation_created_at2:
            if tokenized_created_at2 in month:
                arrayCreated2.append(tokenized_created_at2)

    countCreated2 = Counter(arrayCreated2)
    valueArray2 = countCreated2.values()

    valueCreated2 = []
    for value_created2 in valueArray2:
        valueCreated2.append(value_created2)
    context["value_unhappy_bar"] = valueCreated2

    monthCreated2 = []
    for month_created2 in countCreated2:
        monthCreated2.append(month_created2)
    context["month_unhappy_bar"] = monthCreated2


    # Emosi Bahagia Pie
    year = ['2020']
    arrayCreatedYear =[]
    list_data_pie = DataDjango.objects.all()
    for field_pie in list_data_pie:
        created_year = field_pie.created_at
        punctuation_created_year = created_year.split()
        for tokenized_created_year in punctuation_created_year:
            if tokenized_created_year in year:
                arrayCreatedYear.append(tokenized_created_year)
    countCreatedYear = Counter(arrayCreatedYear)
    valueArrayYear = countCreatedYear.values()
    for value_year_happy in valueArrayYear:
        print("Happy Emotion")

    # Emosi Tidak Bahagia Pie
    arrayCreatedYear2 =[]
    list_data_pie2 = DataDjango2.objects.all()
    for field_pie2 in list_data_pie2:
        created_year2 = field_pie2.created_at
        punctuation_created_year2 = created_year2.split()
        for tokenized_created_year2 in punctuation_created_year2:
            if tokenized_created_year2 in year:
                arrayCreatedYear2.append(tokenized_created_year2)
    countCreatedYear2 = Counter(arrayCreatedYear2)
    valueArrayYear2 = countCreatedYear2.values()
    for value_year_unhappy in valueArrayYear2:
        print("Unhappy Emotion")

    total = value_year_happy + value_year_unhappy
    percentHappy = (value_year_happy / total)*100
    percentUnhappy = (value_year_unhappy / total)*100

    context["value_happy_year_pie"] = percentHappy
    context["value_unhappy_year_pie"] = percentUnhappy


    return render(request, 'polls/index.html',context)



