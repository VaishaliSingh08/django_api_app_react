from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=100, blank=True, null=True)
    company_type = models.CharField(max_length=20, blank=True, null=True)
    company_website = models.CharField(max_length=100, blank=True, null=True)
    company_size = models.CharField(max_length=20, blank=True, null=True)
    company_about = models.CharField(max_length=5000, blank=True, null=True)
    company_logo = models.CharField(max_length=1000, blank=True, null=True)
    company_banner = models.CharField(max_length=1000, blank=True, null=True)
    company_location = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.company_name

class CompanyAppGallery(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    gallery_image = models.CharField(max_length=200, blank=True, null=True)

class Jobs(models.Model):
    job_name = models.CharField(max_length=100, blank=True, null=True)
    job_experience = models.CharField(max_length=50, blank=True, null=True)
    job_type = models.CharField(max_length=50, blank=True, null=True)
    job_ctc = models.CharField(max_length=50, blank=True, null=True)
    job_about = models.CharField(max_length=2000, blank=True, null=True)
    job_skills = models.CharField(max_length=500, blank=True, null=True)
    job_locations = models.CharField(max_length=500, blank=True, null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    job_vacancies = models.CharField(max_length=10, blank=True, null=True)
    job_qualification_required = models.CharField(max_length=100, blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    profile = models.ForeignKey(Company, related_name="job_profiles", on_delete=models.CASCADE)

    def __str__(self):
        return self.job_name

class AllBenefits(models.Model):
    benefit_name = models.CharField(max_length=100, blank=True, null=True)
    benefit_image = models.CharField(max_length=200, blank=True, null=True)

class CompanyBenefits(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    benefit = models.ForeignKey(AllBenefits, on_delete=models.CASCADE)