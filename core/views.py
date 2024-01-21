from django.http import Http404

from django.shortcuts import render, redirect
from django.views import View
from django.apps import apps

from .forms import NameForm
from .models import *
from .services import generate_html_file


class Index(View):
    def get(self, request):
        return render(request, 'core/index.html', {})


class StartProject(View):
    def post(self, request):
        user = request.user
        result = Result.objects.create(user=user)
        return redirect('process', result.id)


class Process(View):
    def get(self, request, result_id):
        try:
            result = Result.objects.get(id=result_id)
            if result.user != request.user:
                raise Http404
        except:
            raise Http404

        if not result.name:
            component_name = 'Name'
            component_objects_list = []
            component_description = 'Enter the name'
            process_form = NameForm()
            return render(request, 'core/process.html', {'component_name': component_name,
                                                         'component_objects_list': component_objects_list,
                                                         'component_description': component_description,
                                                         'process_form': process_form})

        components = ['header', 'footer']
        for component_name in components:
            component = getattr(result, component_name)
            if not component:
                component_model = apps.get_model('core', component_name)
                component_objects_list = component_model.objects.all()
                component_description = component_model.get_description()

                return render(request, 'core/process.html', {'component_name': component_name,
                                                             'component_objects_list': component_objects_list,
                                                             'component_description': component_description})

        if result.result_html:
            #make result views
            return redirect('index')
        else:
            header_html_file = result.header.html
            footer_html_file = result.footer.html
            generated_result_html_file = generate_html_file(result.id ,header=header_html_file, footer=footer_html_file)
            result.result_html = generated_result_html_file
            result.save()
            print(generated_result_html_file)
            # make result views
            return redirect('index')

    def post(self, request, result_id):
        try:
            result = Result.objects.get(id=result_id)
            if result.user != request.user:
                raise Http404
        except:
            raise Http404

        component_name = request.POST['component_name']
        if component_name == 'name':
            result.name = request.POST['name']
            result.save()
        else:
            component_model = apps.get_model('core', component_name)
            component_object = component_model.objects.get(id=request.POST['value'])
            setattr(result, component_name, component_object)
            result.save()

        return redirect('process', result_id)