from django.shortcuts import render
from django.http import HttpResponse
import datetime

def filters(request):
    context={'val':8, 'list':[1,2,3,4,4,45,5,6,6,6,],
             'name':'piash', 'dat' : datetime.datetime.now(),
             'empty':'', 'esc':'<p>You are <em>pretty</em> smart!</p>',
             'lower':'My Name IS PIASH','upper':'i love coding ',
             'title': 'this is germany', 'joi':[1,2,3,4,5,6,7,8,9,0],
             'ad_slash':"I'm md saiful",'center':"piash",
             'cutting':[12,4,0,99,80,6,0,9,4,0.5,3,4,3,2,0],
             'dictsort':[{'name':'piash', 'age': 12},
                         {'name':'asifaaa', 'age': 9},
                         {'name': 'tanjil', 'age': 6}], 'div':30,
                         'convert' : 123456789, 'ab':['ab', 'b', 'c'],
                         "serial":"first\nsecond\nthird\nfive",
                         'slugify':"Learn D-jango with piash ",
                          "blog_date": datetime.datetime(2006, 6, 1, 0, 0),
                          "menu": [
            "Courses",
            [
                "Python",
                ["Django", "Flask"],
                "JavaScript"
            ],
            "Contact"
        ]
             }
 
    return render(request,'template_filters/filters.html',context)