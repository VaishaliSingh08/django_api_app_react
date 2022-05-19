from django.contrib import admin
from .models import Company, Jobs, AllBenefits, CompanyAppGallery


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('id','company_name', 'company_type', 'company_website', 'company_size',
                    'company_logo','company_banner','company_location', 'created_date','updated_date')


class JobsAdmin(admin.ModelAdmin):
    list_display = ('id','company_id')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Jobs, JobsAdmin)
admin.site.register(CompanyAppGallery)
admin.site.register(AllBenefits)