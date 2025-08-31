from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Gift)
class GiftAdmin(admin.ModelAdmin):
    model = Gift

@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    model = Claim