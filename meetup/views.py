from django.contrib.auth import login, logout, get_user_model
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from meetup.forms import RegisterForm, LoginForm, GroupForm
from meetup.models import Group, GroupMemberDetails


def homeview(request):
    if request.user.is_authenticated:
        if request.user.host:
            groups = Group.objects.filter(creator=request.user)
            return render(request, 'meetup/host_homepage.html',{'groups':groups})
        elif not request.user.host:
            if request.method == 'POST':
                group = Group.objects.get(group_id=request.POST['add'])
                group_member_obj = GroupMemberDetails.objects.get_or_create(user = request.user, group = group)
            interests = []

            for interest in request.user.interests:
                interests.append(interest)

            groups =[]
            members = GroupMemberDetails.objects.filter(user = request.user)
            grps = [member.group for member in members]

            ids_to_exclude = [g.group_id for g in grps]
            for group in Group.objects.exclude(group_id__in=ids_to_exclude):
                if group.category.interest in interests:
                    groups.append(group)
            return render(request, 'meetup/user_homepage.html',{'groups':groups})
    else:
        return redirect('/user_login')


def register(request):

    if request.method == 'POST' and 'submit' in request.POST:
        register_form = RegisterForm(request.POST or None)
        if register_form.is_valid():
            register_form.save()
            return render(request, 'meetup/host_homepage.html')
        else:
            return HttpResponse('{}'.format(register_form.errors))

    else:
        register_form = RegisterForm()
        return render(request, 'meetup/register.html',{'register_form':register_form})

def user_logout(request):
    logout(request)
    return render(request, 'meetup/host_homepage.html')

def user_login(request):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            user_obj = form.cleaned_data.get('user_obj')
            login(request,user_obj)
            return redirect('meetup:homeview')
        return render(request, 'meetup/login.html', {'form':form})

def create_group_view(request):
    if request.method == "POST":
        form = GroupForm(request.POST, request.FILES)
        if form.is_valid():
            saved_form = form.save(commit=False)
            saved_form.creator = request.user
            saved_form.save()
            return render(request, 'meetup/host_homepage.html')
        else:
            return HttpResponse("{}".format(form.errors))
    else:
        form = GroupForm()
        return render(request, 'meetup/groupform.html',{'form':form})

def group_details(request,group_id):
    group = Group.objects.get(group_id=group_id)
    return render(request, 'meetup/group_details.html',{'group':group})