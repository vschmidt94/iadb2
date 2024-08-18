"""
Process app - views modules
"""
# from django.shortcuts import render, get_list_or_404, get_object_or_404
# from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView, ModelFormMixin
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .forms import ProcessForm
from .models import Process


class ProcessList(ListView, ModelFormMixin):
    """
    List view of all the Processes
    """
    model = Process
    form_class = ProcessForm
    context_object_name = 'processes'

    template_name = 'common/generic_list_inquiry_page.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        return ListView.get(self, request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Load the context with what is needed for list display.
        """
        ctx = super().get_context_data(**kwargs)
        ctx['page_heading'] = 'Process Inquiry'
        ctx['table_heading'] = 'Processes'
        ctx['fields'] = Process.inquiry_fields()
        ctx['about_text'] = Process.page_params.about_text
        ctx['show_edit_link'] = Process.page_params.show_edit_link
        ctx['form'] = self.form

        return ctx


class ProcessUpdate(SuccessMessageMixin, UpdateView):
    """
    class-based Process record update view
    Allows editing for Process Notes, but anything further requires use of Admin
    interface.
    """
    model = Process
    fields = ['name', 'frequency', 'note']
    template_name = 'common/generic_update_page.html'
    success_url = reverse_lazy('processes')
    success_message = 'Updated the %s process.'

    def get_context_data(self, **kwargs):
        """
        Override the default implementation so we can load additional data to the context.
        """
        # Call the base implementation to get a context
        ctx = super().get_context_data(**kwargs)

        # Extend the context with stuff IADB2 generic_detail_page.html template needs.
        ctx['page_heading'] = '{} Details'.format(Process._meta.verbose_name)
        ctx['alert_text'] = """Process Notes can be updated here. Any other maintenance to
                               the Process record must be via the admin interface."""

        return ctx

    def get_success_message(self, cleaned_data):
        """
        Create a more informative success message.
        """
        return self.success_message % str(self.object)
