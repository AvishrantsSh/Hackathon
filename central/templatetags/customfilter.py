from django import template
from django.contrib.auth import get_user_model
from central.models import Hospital_Records
register = template.Library()

@register.filter
def bed(value):
    try:
        lst = list(map(int, value.split(',')))
        bed = {"General":lst[0], "Emergency":lst[1], "Isolation":lst[2]}
        return bed

    except:
        return None

@register.filter
def blood(value):
    try:
        lst = list(map(int, value.split(',')))
        blood = {
                "A+":lst[0],
                "O+":lst[1],
                "B+":lst[2],
                "AB+":lst[0],
                "A-":lst[1],
                "O-":lst[2],
                "B-":lst[1],
                "AB-":lst[2]
                }
        return blood
    
    except:
        return None

@register.filter
def safe(value):
    return Hospital_Records.objects.get(id=value).name

@register.filter
def region(value):
    return Hospital_Records.objects.get(id=value).region

@register.filter
def safefont(value):
    return str(value)[:50]

@register.filter
def address(value):
    return Hospital_Records.objects.get(id=value).address
    
@register.filter
def contact(value):
    return Hospital_Records.objects.get(id=value).contact

@register.filter
def email(value):
    return Hospital_Records.objects.get(id=value).email