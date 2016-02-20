from django.contrib import admin
from .models import (
    Resume,
    CareerGoal,
    ContactInfo,
    Education,
    WorkExperience,
    ProgrammingSkills,
    Line
)
from django.core.urlresolvers import reverse_lazy
from django.utils.text import mark_safe
from common.utils import PdfKit


class ResumeAdmin(admin.ModelAdmin):
    model = Resume
    actions = ('render_as_pdf',)
    prepopulated_fields = {'slug': ('name',), }
    list_display = ('name', 'view')

    def render_as_pdf(self, request, queryset):
        for obj in queryset:
            url = '{}?q=static'.format(reverse_lazy('resume:index', kwargs={'slug': obj.slug}))
            print url
            PdfKit.create_pdf(url, obj.slug)

    def view(self, obj=None):
        return mark_safe(
            '<a href={}>view</a>'.format(reverse_lazy('resume:index', kwargs={'slug': obj.slug}))
        )


admin.site.register(Resume, ResumeAdmin)
admin.site.register(CareerGoal)
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(ContactInfo)
admin.site.register(ProgrammingSkills)
admin.site.register(Line)