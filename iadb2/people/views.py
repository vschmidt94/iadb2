"""
People app - views module
"""
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic.edit import ModelFormMixin
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from .forms import DepartmentForm, PersonForm
from .models import Person, Department


class DepartmentListView(ListView, ModelFormMixin):
    """
    Generic class-based view for a list of departments.
    """
    model = Department
    form_class = DepartmentForm
    context_object_name = 'departments'

    # Does not use the generic list template (templates/common/generic_list_*)
    # due to having ability to add new department & the modal is unique.
    template_name = 'people/depts.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save()

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Load the context with what is needed for list display
        """
        ctx = super().get_context_data(**kwargs)
        ctx['page_heading'] = 'Department Inquiry'
        ctx['table_heading'] = 'Departments'
        ctx['fields'] = Department.inquiry_fields()
        ctx['about_text'] = Department.page_params.about_text
        ctx['show_edit_link'] = Department.page_params.show_edit_link
        ctx['form'] = self.form

        return ctx


class DepartmentUpdate(SuccessMessageMixin, UpdateView):
    """
    class-based Department record update view
    """
    model = Department
    fields = ['dept_name', 'note']
    template_name = 'common/generic_update_page.html'
    success_url = reverse_lazy('departments')
    success_message = '%s was updated.'

    def get_context_data(self, **kwargs):
        # Call the base implementation to get a context
        ctx = super().get_context_data(**kwargs)

        # Add in the extra contect variables we want
        ctx['page_heading'] = 'Edit Department Record'

        return ctx

    def get_success_message(self, cleaned_data):
        return self.success_message % str(self.object)


class PeopleListView(ListView, ModelFormMixin):
    """
    Generic class-based view for a list of people.
    """
    model = Person
    form_class = PersonForm
    context_object_name = 'people'

    # Does not use the generic list template due to having ability to
    # add new person & the modal is unique.
    template_name = 'people/people.html'

    def get(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)
        return ListView.get(self, request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.object = None
        self.form = self.get_form(self.form_class)

        if self.form.is_valid():
            self.object = self.form.save()

        return self.get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        """
        Load the context with what is needed for list display
        """
        ctx = super().get_context_data(**kwargs)
        ctx['page_heading'] = 'People Inquiry'
        ctx['table_heading'] = 'People'
        ctx['fields'] = Person.inquiry_fields()
        ctx['about_text'] = Person.page_params.about_text
        ctx['show_edit_link'] = Person.page_params.show_edit_link
        ctx['form'] = self.form

        return ctx


class PersonDetailView(DetailView):
    """
    Generic class-based detail view for a person.
    """
    model = Person
    fields = '__all__'
    template_name = 'people/person_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation to get a context
        ctx = super().get_context_data(**kwargs)

        # Add in the extra contect variables we want
        ctx['pageHeading'] = 'View Person Record'

        return ctx


class PersonCreate(CreateView):
    """
    class-based Person creation view
    """
    model = Person
    fields = '__all__'
    template_name = ''


class PersonUpdate(SuccessMessageMixin, UpdateView):
    """
    class-based Person record update view
    """
    model = Person
    fields = ['is_active', 'name_first', 'name_last', 'dept']
    template_name = 'people/person_update.html'
    success_url = reverse_lazy('people')
    success_message = '%s was updated.'

    def get_context_data(self, **kwargs):
        # Call the base implementation to get a context
        ctx = super().get_context_data(**kwargs)

        # Add in the extra contect variables we want
        ctx['page_heading'] = 'Edit Person Record'

        return ctx

    def get_success_message(self, cleaned_data):
        return self.success_message % str(self.object)


class PersonDelete(DeleteView):
    """
    class-based Person record delete view
    """
    model = Person
    success_url = reverse_lazy('people')
    template_name = ''  # TODO
