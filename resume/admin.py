from django.contrib import admin
from .models import (
    Resume,
    CareerGoal,
    ContactInfo,
    Education,
    WorkExperience,
    ProgrammingSkills,
    Line,
    ResumeCategory
)
from django.core.urlresolvers import reverse_lazy
from django.utils.text import mark_safe
from common.utils import PdfKit, truncate_chars


class ResumeAdmin(admin.ModelAdmin):
    model = Resume
    actions = ('render_as_pdf',)
    prepopulated_fields = {'slug': ('name',), }
    list_display = ('name', 'all_categories', 'view')

    def render_as_pdf(self, request, queryset):
        for obj in queryset:
            url = '{}?q=static'.format(reverse_lazy('resume:index', kwargs={'slug': obj.slug}))
            print url
            PdfKit.create_pdf(url, obj.slug)

    def view(self, obj=None):
        return mark_safe(
            '<a href={}>view</a>'.format(reverse_lazy('resume:index', kwargs={'slug': obj.slug}))
        )

    def all_categories(self, obj):
        return ', '.join(obj.categories
                         .values_list('category',
                                      flat=True))


class CategoryAdminMixin(admin.ModelAdmin):
    list_display = ('text', 'all_categories',)

    def text(self, obj):
        return truncate_chars(obj.__unicode__(), 100)

    def all_categories(self, obj):
        return ', '.join(obj.categories
                         .values_list('category',
                                      flat=True))


class SortingValueAdminMixin(admin.ModelAdmin):
    list_editable = ('sorting_value',)


class ResumeModelMixin(CategoryAdminMixin,
                       SortingValueAdminMixin):
    list_display = ('text', 'all_categories', 'sorting_value',)


admin.site.register(Resume, ResumeAdmin)
admin.site.register(CareerGoal, ResumeModelMixin)
admin.site.register(Education, ResumeModelMixin)
admin.site.register(WorkExperience, ResumeModelMixin)
admin.site.register(ContactInfo)
admin.site.register(ProgrammingSkills, ResumeModelMixin)
admin.site.register(Line)
admin.site.register(ResumeCategory)