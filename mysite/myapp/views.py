from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm, LoginForm, ProjectForm
from .models import Project



# Create your views here.
@login_required(login_url='login')
def home(request):
    projects = Project.objects.filter(created_by=request.user).all().order_by('-created_at')
    context = {'projects': projects}
    
    return render(request, 'home.html', context)

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})
    


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def createProjectView(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.created_by = request.user
            project.save()
            return redirect('home')
    else:
        form = ProjectForm()
    return render(request, 'create_project.html', {'form': form})


def listItem(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'list_item.html', {'project': project})

@login_required
def project_edit(request, project_id):
    item = get_object_or_404(Project, pk=project_id, created_by=request.user)
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.created_by = request.user
            item.save()
            return redirect('home')
    else:
        form = ProjectForm(instance=item)   
    
    return render(request, 'project_edit.html', {'form': form,})

@login_required
def project_delete(request, project_id):
    item = get_object_or_404(Project, pk=project_id, created_by=request.user)
    if request.method == 'POST':
        item.delete()
        return redirect('home')
    return render(request, 'project_delete.html', {'item': item})
