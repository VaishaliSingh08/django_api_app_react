from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt, ensure_csrf_cookie
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from company_app.models import Company, Jobs, CompanyAppGallery, AllBenefits
from .serializers import TopCompaniesDataSerializer, FeaturedJobsDataSerializer, getJobsDatabyCompanyIdSerializer, \
    getGalleryDatabyCompanyIdSerializer, JobsDataSerializer, getBenefitsDataSerializer

from django.core.files.storage import default_storage


# Create your views here


# Function API to get top 100 companies data

@api_view(['GET','PUT'])
def TopCompaniesDataApi(request, id=0):
    if id:
        top_comp = Company.objects.get(id=id)
        top_company_serializer = TopCompaniesDataSerializer(top_comp)
    else:
        top_comp = Company.objects.all()
        top_company_serializer = TopCompaniesDataSerializer(top_comp, many=True)

    if request.method == 'GET':
        return JsonResponse(top_company_serializer.data, safe=False, status=200)

    elif request.method == 'PUT':
        company_data = JSONParser().parse(request)
        company = Company.objects.get(id=id)
        company_serializer = TopCompaniesDataSerializer(company, data=company_data)
        if company_serializer.is_valid():
            company_serializer.save()
            return JsonResponse(company_serializer.data, safe=False, status=200)
        return JsonResponse("Failed to Update.", safe=False)


# Function API to get jobs by company id data
@api_view(['GET'])
def getJobsDatabyCompanyIdApi(request, id=0):
    if request.method == 'GET':
        jobs_data = Jobs.objects.filter(company_id=id).values()
        jobs_data_serializer = getJobsDatabyCompanyIdSerializer(jobs_data, many=True)
        return JsonResponse(jobs_data_serializer.data, safe=False, status=200)

   
# Function API to get gallery images by company id data
@api_view(['GET'])
def getGalleryDatabyCompanyIdApi(request, id=0):
    if request.method == 'GET':
        gallery_data = CompanyAppGallery.objects.filter(company_id=id).values()
        print(gallery_data)
        gallery_data_serializer = getGalleryDatabyCompanyIdSerializer(gallery_data, many=True)
        return JsonResponse(gallery_data_serializer.data, safe=False, status=200)

# Function API to get benefits by company id data
@api_view(['GET'])
def getBenefitsDataApi(request):
    if request.method == 'GET':
        benefits_data = AllBenefits.objects.all()
        benefits_data_serializer = getBenefitsDataSerializer(benefits_data, many=True)
        return JsonResponse(benefits_data_serializer.data, safe=False, status=200)


# Function API to delete gallery images by company id data
@api_view(['DELETE'])
def getDeleteGaleryDatabyIdApi(request, id=0):
    if request.method == 'DELETE':
        gallery_data = CompanyAppGallery.objects.get(id=id)
        gallery_data.delete()
        return JsonResponse("Deleted successfully !!", safe=False, status=200)

@api_view(['GET', 'DELETE'])
def CompanyJobApi(request, id=0):
    if id:
        job_post = Jobs.objects.get(id=id)
        job_post_serializer = JobsDataSerializer(job_post)
    else:
        job_post = Jobs.objects.all()
        job_post_serializer = JobsDataSerializer(job_post, many=True)

    if request.method == 'GET':
        return JsonResponse(job_post_serializer.data, safe=False, status=200)


    elif request.method == 'DELETE':
        jobs = Jobs.objects.get(id=id)
        jobs.delete()
        return JsonResponse("Deleted Succeffully!!", safe=False)


@csrf_exempt
def EditCompanyPostJobApi(request, id=0):
   if request.method == 'PUT':
        jobs_data = JSONParser().parse(request)
        jobs = Jobs.objects.get(id=id)
        jobs_serializer = JobsDataSerializer(jobs, data=jobs_data)
        if jobs_serializer.is_valid():
            jobs_serializer.save()
            return JsonResponse(jobs_serializer.data, safe=False)

@csrf_exempt
def CompanyPostJobApi(request):
    if request.method == 'POST':
        job_post_data = JSONParser().parse(request)
        print(job_post_data)
        job_post_serializer = JobsDataSerializer(data = job_post_data)
        if job_post_serializer.is_valid():
            job_post_serializer.save()
            return JsonResponse(job_post_serializer.data, status=status.HTTP_201_CREATED, safe=False)
        return JsonResponse(job_post_serializer.errors, safe=False, status=status.HTTP_400_BAD_REQUEST)


# Function API to get featured jobs data
@api_view(['GET','PUT'])
def FeaturedJobsDataApi(request, id=0):
    if id:
        featured_jobs = Jobs.objects.get(id=id)
        featured_jobs_serializer = FeaturedJobsDataSerializer(featured_jobs)
    else:
        featured_jobs = Jobs.objects.all()
        featured_jobs_serializer = FeaturedJobsDataSerializer(featured_jobs, many=True)

    if request.method == 'GET':
        return JsonResponse(featured_jobs_serializer.data, safe=False, status=200)

    elif request.method == 'PUT':
        company_data = JSONParser().parse(request)
        company = Company.objects.get(id=id)
        company_serializer = TopCompaniesDataSerializer(company, data=company_data)
        if company_serializer.is_valid():
            company_serializer.save()
            return JsonResponse(company_serializer.data, safe=False, status=200)
        return JsonResponse("Failed to Update.", safe=False)