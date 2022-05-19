from rest_framework import serializers
from company_app.models import Company, Jobs, CompanyAppGallery, AllBenefits


class TopCompaniesDataSerializer(serializers.ModelSerializer):
    job_profiles = serializers.SlugRelatedField(
        many=True,
        read_only=True,
        slug_field='job_name'
    )
    class Meta:
        model = Company
        fields = ('id',
                  'company_name',
                  'company_logo',
                  'company_type',
                  'company_website',
                  'company_size',
                  'company_about',
                  'company_banner',
                  'company_location',
                  'created_date',
                  'job_profiles'
                  )

class FeaturedJobsDataSerializer(serializers.ModelSerializer):
    company = TopCompaniesDataSerializer(many=False)
    class Meta:
        model = Jobs
        fields = ('id',
                  'job_name',
                  'job_experience',
                  'job_type',
                  'job_ctc',
                  'job_about',
                  'job_skills',
                  'job_locations',
                  'created_date',
                  'job_vacancies',
                  'job_qualification_required',
                  'company'
                  )


class getJobsDatabyCompanyIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ('id',
                  'job_name',
                  'job_experience',
                  'job_type',
                  'job_ctc',
                  'job_about',
                  'job_skills',
                  'job_locations',
                  'created_date',
                  'job_vacancies',
                  'job_qualification_required'
                  )

class JobsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = ('id',
                  'job_name',
                  'job_experience',
                  'job_type',
                  'job_ctc',
                  'job_about',
                  'job_skills',
                  'job_locations',
                  'created_date',
                  'job_vacancies',
                  'job_qualification_required',
                  'company',
                  'profile'
                  )


class getGalleryDatabyCompanyIdSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyAppGallery
        fields = ('id',
                  'gallery_image'
                  )

class getBenefitsDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllBenefits
        fields = ('id',
                  'benefit_name',
                  'benefit_image'
                  )