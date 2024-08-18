"""
Requirements app - views module
"""
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from .forms import DocumentDetailForm, RequirementDetailForm
from .models import Document, Requirement, Standard


class DocumentListView(ListView):
    """
    List view of all the Documents.
    """
    model = Document
    template_name = 'common/generic_list_inquiry_page.html'

    def get_context_data(self, **kwargs):
        """
        Load the context with what is needed for list display.
        """
        ctx = super().get_context_data(**kwargs)
        ctx['page_heading'] = '{} Inquiry'.format(
            Document._meta.verbose_name_plural)
        ctx['table_heading'] = '{}'.format(Document._meta.verbose_name_plural)
        ctx['objects'] = Document.objects.all()
        ctx['fields'] = Document.inquiry_fields()
        ctx['about_text'] = Document.page_params.about_text
        ctx['show_edit_link'] = Document.page_params.show_edit_link

        return ctx


class DocumentUpdateView(SuccessMessageMixin, UpdateView):
    """
    Detail view for a single Document.
    Allows editing for Requirement Notes, but anything further requires use of
    Admin interface.
    """
    model = Document
    form_class = DocumentDetailForm
    template_name = 'common/generic_detail_page.html'
    success_url = reverse_lazy('documents_inquiry')
    success_message = '%s was updated.'

    def get_context_data(self, **kwargs):
        """
        Override the default implementation so we can load additional data to
        the context.
        """
        # Call the base implementation to get a context
        ctx = super().get_context_data(**kwargs)

        # Extend the context with stuff IADB2 generic_detail_page.html template
        # needs.
        ctx['page_heading'] = '{} Details'.format(Document._meta.verbose_name)
        ctx['alert_text'] = '''Document Notes can be updated here. Any other
                               maintenance to the Process record must be via
                               the admin interface.'''

        return ctx

    def get_success_message(self, cleaned_data):
        """
        Create a more informative success message.
        """
        return self.success_message % str(self.object)


class RequirementListView(ListView):
    """
    List view of all the Requirements.
    """
    model = Requirement
    template_name = 'common/generic_list_inquiry_page.html'

    def get_context_data(self, **kwargs):
        """
        Load the context with what is needed for list display.
        """
        ctx = super().get_context_data(**kwargs)
        ctx['page_heading'] = '{} Inquiry'.format(
            Requirement._meta.verbose_name_plural)
        ctx['table_heading'] = '{}'.format(
            Requirement._meta.verbose_name_plural)
        ctx['about_text'] = Requirement.page_params.about_text
        ctx['objects'] = Requirement.objects.all()
        ctx['fields'] = Requirement.inquiry_fields()
        ctx['show_edit_link'] = Requirement.page_params.show_edit_link

        return ctx


class RequirementUpdateView(SuccessMessageMixin, UpdateView):
    """
    Detail view for a single Requirement.
    Allows editing for Requirement Notes, but anything further requires use of
    Admin interface.
    """
    model = Requirement
    form_class = RequirementDetailForm
    template_name = 'common/generic_detail_page.html'
    success_url = reverse_lazy('requirements_inquiry')
    success_message = '%s was updated.'

    def get_context_data(self, **kwargs):
        """
        Override the default implementation so we can load additional data to
        the context.
        """
        # Call the base implementation to get a context
        ctx = super().get_context_data(**kwargs)

        # Extend the context with stuff IADB2 generic_detail_page.html template
        # needs.
        ctx['page_heading'] = '{} Details'.format(
            Requirement._meta.verbose_name)
        ctx['alert_text'] = '''Requirement Notes can be updated here. Any other
                               maintenance to the Process record must be via
                               the admin interface.'''

        return ctx

    def get_success_message(self, cleaned_data):
        """
        Create a more informative success message.
        """
        return self.success_message % str(self.object)


class StandardListView(ListView):
    """
    List view of all the Standards.
    """
    model = Standard
    template_name = 'common/generic_list_inquiry_page.html'

    def get_context_data(self, **kwargs):
        """
        Load the context with what is needed for list display.
        """
        ctx = super().get_context_data(**kwargs)
        ctx['page_heading'] = '{} Inquiry'.format(
            Standard._meta.verbose_name_plural)
        ctx['table_heading'] = '{}'.format(Standard._meta.verbose_name_plural)
        ctx['about_text'] = Standard.page_params.about_text
        ctx['objects'] = Standard.objects.all()
        ctx['fields'] = Standard.inquiry_fields()
        ctx['show_edit_link'] = Standard.page_params.show_edit_link

        return ctx


def view_digraphs(request):
    """
    View that has a drop-down selector to show requirement coverage
    delegation by way of digraphs for each top-level node.
    """
    # find top-level requirement nodes
    top_level_reqs = Requirement.objects.filter(parent=None)

    # build all the digraphs
    # At some point this may get too expensive to do them all at once
    # while waiting on the page to load, but not more than a small
    # dalay right now. This page is rarely used.
    requirements = Requirement.objects.filter(is_active=True)
    file_list = create_all_digraphs(requirements)

    ctx = {'pageHeading': 'View Requirement Coverage Delegations',
           'topLevelReqs': top_level_reqs,
           'file_list': file_list}

    return render(request, 'requirements/delegation_graphs.html', ctx)


def create_all_digraphs(requirements):
    """
    Creates a Digraph for every active top-level node.
    A top-level node does not have a parent node.
    """
    root_list = []
    file_list = []
    for requirement in requirements:
        if requirement.parent is None and requirement.is_active:
            root_list.append(requirement)
    for requirement in root_list:
        create_digraph(requirement)
        url = 'digraphs/' + str(requirement) + '_digraph.svg'
        file_list.append((str(requirement), url))
    return file_list


def create_digraph(root):
    """
    Creates a graphviz Digraph for a top-level node and all the
    descendants of that node.
    """
    import os
    import graphviz as gv
    from django.conf import settings

    file_name = os.path.join(
        settings.MEDIA_ROOT, 'digraphs/{}_digraph'.format(root))
    g = gv.Digraph(format='svg')
    g.attr(layout='twopi', overlap='false')

    descendants = get_descendants(root)
    print(descendants)

    if descendants:
        for node in descendants:
            name = node.identifier

            if node.coverage_by == 'S':
                # yellow nodes are those requiring coverage
                color = 'yellow'
                style = 'filled'
            else:
                # un-colored nodes delegate their coverage to
                # some other node.
                color = 'black'
                style = ''

            g.node(str(name), fillcolor=color, style=style)

            # Draw the edge (arrow) pointing from the node that
            # has delgated it's coverage in the direction it has
            # shifted responsibility (i.e., to child or parent)
            if node.parent:
                if node.parent.coverage_by == 'C':
                    g.edge(node.parent.identifier, node.identifier)
                elif (node.parent.coverage_by == 'S' and
                      node.coverage_by == 'S'):
                    g.edge(node.identifier, node.parent.identifier, dir='none')
                else:
                    g.edge(node.identifier, node.parent.identifier)

    g.render(file_name)

    return file_name


def get_descendants(root):
    """
    Returns a list of requirements which are descendants of the provided root.
    """
    descendant_list = []

    def get_children(node):
        for child in node.children.all():
            get_children(child)
            descendant_list.append(child)

    get_children(root)

    return descendant_list
