from datetime import datetime, date as date_, timedelta
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.urls import reverse
#from django.http import HttpResponse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum, Max
#from django.views.generic import ListView
from .models import Project, SalesOrderHeader, WorkTimeJournal
from .forms import WorkTimeJournalForm, WorkTimeJournalForm_V2
#from shared import utils



@login_required(login_url='/accounts/login/')
def work_time_journal_proj_list_view(request):
    projects = Project.objects.filter(employees__in = [request.user.employee], active = True).order_by('customer__name', 'name').select_related('customer')
    return render(request, 'salary/v1/registration_list.html', {'projects': projects})

#for validation check this source: https://stackoverflow.com/questions/7948750/custom-form-validation
class WorkTimeJournalView(LoginRequiredMixin, View):
    # Time registration for a selected object (project)
    login_url='/accounts/login/'
    
    form_class = WorkTimeJournalForm

    def get_context(self, request, project_id, date, jrline_id, action, form):
        project = Project.objects.get(id=project_id)
        employee = request.user.employee
        jr_lines = WorkTimeJournal.objects.filter(work_date = date,
                                                  employee = employee).order_by('work_time_from').prefetch_related('content_object')

        jr_totals = WorkTimeJournal.objects.filter(work_date = date,
                                                   employee = employee).aggregate(Sum('work_time'),
                                                                                  Sum('distance'), 
                                                                                  Sum('toll_ring'), 
                                                                                  Sum('ferry'), 
                                                                                  Sum('diet'))
        return {'date': date,
                'project': project,
                'employee': employee,
                'jr_lines': jr_lines,
                'jr_totals': jr_totals,
                'modify_id': int(jrline_id) if action == 'edit' else 0, #!! messy, rebuild template to fully use 'action' variable.
                'action': action,
                'open': self.get_open(date),
                'form': form
                }

    def get(self, request, project_id, date, jrline_id = 0, action='edit'):
        if jrline_id == 0:
            action = 'view'
        else:
            try:
                jrline = WorkTimeJournal.objects.get(id=jrline_id)
            except:
                action = 'view'
                jrline = None

        if action == 'view':
            form = self.form_class()
        elif action == 'delete':
            form = self.form_class()
            jrline.delete();
        elif action == 'edit':
            form = self.form_class(instance=jrline)

        return render(request, 
                      'salary/v1/registration_journal.html',
                      self.get_context(request, project_id, date, jrline_id, action, form)
                      )

    def post(self, request, project_id, date, jrline_id = 0, *args, **kwargs):
        work_date = datetime.strptime(date, '%Y-%m-%d').date()
        
        if jrline_id == 0:
            journal = None
        else:
            try:
                journal = WorkTimeJournal.objects.get(id=jrline_id)
            except:
                journal = None
            
        request.POST = request.POST.copy()
        
        #Adding date to request data to pass form validation
        request.POST['work_date_day'] = work_date.day
        request.POST['work_date_month'] = work_date.month
        request.POST['work_date_year'] = work_date.year
        request.POST['employee'] = request.user.employee
        
        form =  self.form_class(request.POST, instance = journal)
        
        project = Project.objects.get(id=project_id)
        employee = request.user.employee
        if form.is_valid():
            journal = form.save(commit=False)
            journal.employee = employee 
            journal.content_type = ContentType.objects.get_for_model(Project)
            journal.content_object = project
            journal.work_date = work_date
            journal.save()
            # Redirect to GET. 
            return redirect(reverse('tjournal', args = [project_id, date]))
        else:
            # Stay in POST only if form was not valid.
            return render(request, 
                          'salary/v1/registration_journal.html',
                          self.get_context(request, project_id, date, jrline_id, 'edit', form))

    def get_open(self, work_date):
        today = date_.today()
        last_sunday = today + timedelta(days = -today.weekday() - 1)
        return datetime.strptime(work_date, '%Y-%m-%d').date() > last_sunday


#for validation check this source: https://stackoverflow.com/questions/7948750/custom-form-validation
class WorkTimeJournalView_V2(LoginRequiredMixin, View):
    # Time registration for a selected object (project)
    login_url='/accounts/login/'

    form_class = WorkTimeJournalForm_V2

    def get_context(self, request, date, jrline_id, action, form):
        date = date_.today().strftime('%Y-%m-%d') if date is None else date
        employee = request.user.employee
        jr_lines = WorkTimeJournal.objects.filter(work_date = date,
                                                  employee = employee).order_by('work_time_from').prefetch_related('content_object')

        jr_totals = WorkTimeJournal.objects.filter(work_date = date,
                                                   employee = employee).aggregate(Sum('work_time'),
                                                                                  Sum('distance'),
                                                                                  Sum('toll_ring'),
                                                                                  Sum('ferry'),
                                                                                  Sum('diet'),
                                                                                  Max('work_time_to'))
        if jr_lines.count() > 0:
            hour = jr_totals['work_time_to__max'].hour
            minute = jr_totals['work_time_to__max'].minute
        else:
            hour = 8
            minute = 0

        return {'date': date,
                'employee': employee,
                'jr_lines': jr_lines,
                'jr_totals': jr_totals,
                'modify_id': int(jrline_id) if action == 'edit' else 0, #!! messy, rebuild template to fully use 'action' variable.
                'action': action,
                'open': self.get_open(date),
                'form': form,
                'prj_dropdown': Project.objects.filter(employees__in = [request.user.employee], active = True).order_by('name'),
                'time_dropdown': {'hr': str(hour).zfill(2), 'min': str(minute).zfill(2)},
                }

    def get(self, request, date = None, jrline_id = 0, action='edit'):

        if jrline_id == 0:
            action = 'view'
        else:
            try:
                jrline = WorkTimeJournal.objects.get(id=jrline_id)
            except:
                action = 'view'
                jrline = None

        if action == 'view':
            form = self.form_class()
        elif action == 'delete':
            form = self.form_class()
            jrline.delete();
        elif action == 'edit':
            form = self.form_class(instance=jrline)

        return render(request,
                      'salary/v2/registration_journal.html',
                      self.get_context(request, date, jrline_id, action, form)
                      )

    def post(self, request, date = None, jrline_id = 0, *args, **kwargs):
        work_date = datetime.strptime(date, '%Y-%m-%d').date() if date else date_.today()
        work_date_str = work_date.strftime('%Y-%m-%d')
        if jrline_id == 0:
            journal = None
        else:
            try:
                journal = WorkTimeJournal.objects.get(id=jrline_id)
            except:
                journal = None

        request.POST = request.POST.copy()

        #Adding date to request data to pass form validation
        request.POST['work_date_day'] = work_date.day
        request.POST['work_date_month'] = work_date.month
        request.POST['work_date_year'] = work_date.year
        request.POST['employee'] = request.user.employee

        form =  self.form_class(request.POST, instance = journal)

        employee = request.user.employee
        if form.is_valid():
            journal = form.save(commit=False)
            journal.employee = employee
            journal.content_type = ContentType.objects.get_for_model(Project)
            journal.work_date = work_date
            journal.save()
            # Redirect to GET.
            return redirect(reverse('tjr-v2', args = [work_date_str]))
        else:
            # Stay in POST only if form was not valid.
            return render(request, 
                          'salary/v2/registration_journal.html',
                          self.get_context(request, work_date_str, jrline_id, 'edit', form))

    def get_open(self, work_date):
        return True #Remove this when prjdash gets possibility to enter missing hours
        today = date_.today()
        last_sunday = today + timedelta(days = -today.weekday() - 1)
        return datetime.strptime(work_date, '%Y-%m-%d').date() > last_sunday
