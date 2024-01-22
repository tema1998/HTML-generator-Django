from django.contrib import auth, messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import Http404

from django.shortcuts import render, redirect
from django.views import View
from django.apps import apps

from .forms import SignupForm, SigninForm
from .models import *
from .services import generate_html_file


class Index(LoginRequiredMixin, View):
    login_url = 'signin'

    def get(self, request):
        results = Result.objects.filter(user=request.user)
        return render(request, 'core/index.html', {'results':results})


class StartProject(LoginRequiredMixin, View):
    login_url = 'signin'

    def post(self, request):
        user = request.user
        result = Result.objects.create(user=user)
        return redirect('process', result.id)


class Process(LoginRequiredMixin, View):
    login_url = 'signin'

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
            return render(request, 'core/process.html', {'component_name': component_name,
                                                         'component_objects_list': component_objects_list,
                                                         'component_description': component_description,})

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
            return redirect('show-result', result.id)

        else:
            header_html_file = result.header.html
            footer_html_file = result.footer.html
            generated_result_html_file = generate_html_file(result.id, title=result.title, header=header_html_file, footer=footer_html_file)
            result.result_html = generated_result_html_file
            result.save()
            return redirect('show-result', result.id)

    def post(self, request, result_id):
        try:
            result = Result.objects.get(id=result_id)
            if result.user != request.user:
                raise Http404
        except:
            raise Http404

        component_name = request.POST['component_name']

        if component_name == 'name':
            try:
                result.name = request.POST['value']
                result.title = request.POST['title']
                result.save()
            except:
                return redirect('process', result_id)
            return redirect('process', result_id)

        else:
            try:
                component_model = apps.get_model('core', component_name)
                component_object = component_model.objects.get(id=request.POST['value'])
                setattr(result, component_name, component_object)
                result.save()
            except:
                return redirect('process', result_id)
        return redirect('process', result_id)


class ShowResult(LoginRequiredMixin ,View):
    login_url = 'signin'

    def get(self, request, result_id):
        try:
            result = Result.objects.get(id=result_id)
            if result.user != request.user:
                raise Http404
        except:
            raise Http404
        header_html = Header.objects.get(id=1).html
        return render(request, 'core/show_result.html', {'result_name': result.name,
                                                         'result_html': result.result_html,
                                                         'header_html': header_html})


class Signup(View):

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            signup_form = SignupForm(request.POST)
            if signup_form.is_valid():
                with transaction.atomic():
                    cd = signup_form.cleaned_data
                    username = cd['username']
                    email = cd['email']
                    password = cd['password']
                    new_user = User.objects.create_user(username=username, password=password, email=email)

                    auth.login(request, new_user)

                    return redirect('index')
            return render(request, 'core/signup.html', {'signup_form': signup_form})

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            signup_form = SignupForm()
            return render(request, 'core/signup.html', {'signup_form': signup_form})


class Signin(View):
    def post(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            signin_form = SigninForm(request.POST)
            if signin_form.is_valid():
                cd = signin_form.cleaned_data
                user = auth.authenticate(username=cd['username'], password=cd['password'])
                if user:
                    auth.login(request, user)
                    return redirect('index')
            messages.error(request, f'Invalid username or password')
            return render(request, 'core/signin.html', {'signin_form': signin_form})

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('index')
        else:
            signin_form = SigninForm()
            return render(request, 'core/signin.html', {'signin_form': signin_form})


class Logout(View):
    def post(self, request):
        auth.logout(request)
        return redirect('signin')


