from django import template
from django.contrib.auth import get_user_model

register = template.Library()

@register.filter
def bed(value):
    try:
        lst = list(map(int, value[1:-1].split(',')))
        bed = {"General":lst[0], "Emergency":lst[1], "Isolation":lst[2]}
        return bed

    except:
        return None

@register.filter
def blood(value):
    try:
        lst = list(map(int, value[1:-1].split(',')))
        blood = {
                "A+":lst[0],
                "AB+":lst[1],
                "B+":lst[2],
                "O+":lst[0],
                "A-":lst[1],
                "AB-":lst[2],
                "B-":lst[1],
                "O-":lst[2]
                }
        return blood
    
    except:
        return None
