from django.conf.urls import url
from . import views
from django.urls import path


from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    url(r'^api/TopCompaniesData$',views.TopCompaniesDataApi),
    url(r'^api/TopCompaniesData/([0-9]+)$',views.TopCompaniesDataApi),
    url(r'^api/FeaturedJobsData$',views.FeaturedJobsDataApi),
    url(r'^api/FeaturedJobsData/([0-9]+)$',views.FeaturedJobsDataApi),
    url(r'^api/JobsDatabyCompanyId/([0-9]+)$',views.getJobsDatabyCompanyIdApi),
    url(r'^api/GalleryDatabyCompanyId/([0-9]+)$',views.getGalleryDatabyCompanyIdApi),
    url(r'^api/getBenefitsDataApi$',views.getBenefitsDataApi),
    url(r'^api/DeleteGalleryDatabyId/([0-9]+)$',views.getDeleteGaleryDatabyIdApi),
    url(r'^api/CompanyJobApi/([0-9]+)$',views.CompanyJobApi),
    url(r'^api/EditCompanyPostJobApi/([0-9]+)$',views.EditCompanyPostJobApi),
    url(r'^api/CompanyPostJobApi$',views.CompanyPostJobApi),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)