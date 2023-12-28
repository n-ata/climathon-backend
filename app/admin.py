from django.contrib import admin
from django.apps import apps
from django.db.models import Count

class ModelAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site):
        self.list_display = [field.name for field in model._meta.fields]
        self.search_fields = [field.name for field in model._meta.fields]
        super().__init__(model, admin_site)


models = apps.get_models()
for model in models:
    try:
        admin.site.register(model, ModelAdmin)
    except admin.sites.AlreadyRegistered:
        pass
