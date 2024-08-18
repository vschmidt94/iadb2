"""
Audits app - views module
"""
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, ModelFormMixin
from django.views.generic.list import ListView
from .forms import AuditTemplateDetailForm, ScheduleAuditForm
from .models import AuditHeader, AuditPeriod, AuditTemplate


class AuditListView(ListView):
    """
    List view of all the Audits

    The list will contain completed, in-progress, and scheduled audits
    """
    model = AuditHeader
    context_object_name = 'audits'

    template_name = 'common/generic_list_inquiry_page.html'

    def get_context_data(self, **kwargs):
        """
        Load the context with what is needed for list display.
        """
        ctx = super().get_context_data(**kwargs)
        ctx['page_heading'] = 'Audit Inquiry'
        ctx['table_heading'] = 'Audits'
        ctx['objects'] = AuditHeader.objects.all()
        ctx['fields'] = AuditHeader.inquiry_fields()
        ctx['about_text'] = AuditHeader.page_params.about_text
        ctx['show_edit_link'] = AuditHeader.page_params.show_edit_link

        return ctx


class AuditPeriodListView(ListView):
    """
    List view of all the Audit Periods
    """
    model = AuditPeriod
    context_object_name = 'audit_periods'

    template_name = 'common/generic_list_inquiry_page.html'

    def get_context_data(self, **kwargs):
        """
        Load the context with what is needed for list display.
        """
        ctx = super().get_context_data(**kwargs)
        ctx['page_heading'] = 'Audit Period Inquiry'
        ctx['table_heading'] = 'Audit Periods'
        ctx['objects'] = AuditPeriod.objects.all()
        ctx['fields'] = AuditPeriod.inquiry_fields()
        ctx['about_text'] = AuditPeriod.page_params.about_text
        ctx['show_edit_link'] = AuditPeriod.page_params.show_edit_link

        return ctx


class AuditTemplateDetailView(DetailView):
    """
    Generic class-based detail view for Audit Template
    """
    model = AuditTemplate
    fields = '__all__'
    template_name = 'audits/audit_template_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation to get a context
        ctx = super().get_context_data(**kwargs)

        # Add in the extra context variables we want
        ctx['pageHeading'] = 'Audit Template Detail View'

        return ctx


class AuditTemplateListView(ListView):
    """
    List view of all the Audit Templates
    """
    model = AuditTemplate
    queryset = AuditTemplate.objects.prefetch_related(
        'documents', 'requirements')

    template_name = 'audits/audit_template_list_inquiry_page.html'

    def get_context_data(self, **kwargs):
        """
        Load the context with what is needed for list display.
        """
        ctx = super().get_context_data(**kwargs)
        ctx['page_heading'] = 'Audit Template Inquiry'
        ctx['table_heading'] = 'Audit Templates'
        ctx['fields'] = AuditTemplate.inquiry_fields()
        ctx['objects'] = AuditTemplate.objects.all()
        ctx['about_text'] = AuditTemplate.page_params.about_text
        ctx['show_edit_link'] = AuditTemplate.page_params.show_edit_link

        return ctx


class AuditTemplateUpdateView(SuccessMessageMixin, UpdateView):
    """
    Detail view for a single Audit Template.
    Allows editing for Audit Template Notes, but anything further requires use
    of Admin interface.
    """
    model = AuditTemplate
    form_class = AuditTemplateDetailForm
    template_name = 'common/generic_detail_page.html'
    success_url = reverse_lazy('audit_template_inquiry')
    success_message = '%s Audit Template was updated.'

    def get_context_data(self, **kwargs):
        """
        Override the default implementation so we can load additional data to
        the context.
        """
        # Call the base implementation to get a context
        ctx = super().get_context_data(**kwargs)

        # Extend the context with stuff IADB2 generic_detail_page.html
        # template needs.
        ctx['page_heading'] = '{} Details'.format(
            AuditTemplate._meta.verbose_name)
        ctx['alert_text'] = """Audit Template Notes can be updated here. Any
                               other maintenance to the Audit Template record
                               must be via the admin interface."""

        return ctx

    def get_success_message(self, cleaned_data):
        """
        Create a more informative success message.
        """
        return self.success_message % str(self.object)


class AuditScheduleListView(ListView, ModelFormMixin):
    """
    View that allows user to add audit to schedule.
    Note scheduling an audit does not initiate the audit.
    """
    model = AuditHeader
    form_class = ScheduleAuditForm
    context_object_name = 'audits'
    success_url = reverse_lazy('audit_schedule')

    # Does not use the generic list template due to having ability to
    # schedule a new audit & the modal for that is unique.
    template_name = 'audits/audit_schedule.html'

    def get(self, request, *args, **kwargs):
        """
        Handle GET request
        """
        self.object = None
        self.form = self.get_form(self.form_class)
        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """
        Handle POST request
        """
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save()

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Load the context
        """
        ctx = super().get_context_data(**kwargs)
        ctx['page_heading'] = 'Audit Schedule'
        ctx['table_heading'] = 'Scheduled Audits'
        ctx['about_text'] = '''Audit Schedule Inqury view will display any currently
                               scheduled or in-progress audits, and allows for
                               new audits to be added to the schedule.'''
        ctx['fields'] = AuditHeader.inquiry_fields()
        ctx['objects'] = AuditHeader.objects.all()
        ctx['show_edit_link'] = True
        ctx['form'] = self.form

        return ctx
