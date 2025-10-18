from django.shortcuts import render,redirect
from django.http import HttpResponse
from event.forms import CategoryModelForm,EventModelForm,ParticipantModelForm #only used in create task
from event.models import Category,Event,Participant #used in view ,update ,delete task
from django.contrib import messages
from django.utils import timezone
from django.db.models import Count

# Create your views here.
def organizer_dashboard(request):
    today = timezone.now().date()

    total_participants = Participant.objects.count()
    total_events = Event.objects.count()
    upcoming_events = Event.objects.filter(date__gt=today).count()
    past_events = Event.objects.filter(date__lt=today).count()


    todays_events = Event.objects.filter(date=today).select_related('category')

    filter_type = request.GET.get('filter', 'today')

    if filter_type == 'upcoming':
        filtered_events = Event.objects.filter(date__gt=today).select_related('category')
    elif filter_type == 'past':
        filtered_events = Event.objects.filter(date__lt=today).select_related('category')
    elif filter_type == 'all':
        filtered_events = Event.objects.all().select_related('category')
    else:
        filtered_events = todays_events

    categories = Category.objects.all()
    participants = Participant.objects.prefetch_related('events')

    context = {
        "total_participants": total_participants,
        "total_events": total_events,
        "upcoming_events": upcoming_events,
        "past_events": past_events,
        "filtered_events": filtered_events,
        "filter_type": filter_type,
        "categories": categories,
        "participants": participants,
    }

    return render(request, "dashboard/organizer_dashboard.html", context)


def create_category(request):
    """ 2 ta jinis form create korar jonno lagbei
    1.froms er kon model use hobe seta and
    2.context"""
    category_model_form=CategoryModelForm()
    
    if request.method=="POST":
       category_model_form=CategoryModelForm(request.POST)
       
       if category_model_form.is_valid():
            category_model_form.save()
            messages.success(request,'Category Created Successfully')
            # return redirect('view_category')
    context={"category_form":category_model_form}
    return render(request,'categories/categorie_form.html',context)

def view_category(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "categories/category_list.html", context)


def update_category(request,id):
    category=Category.objects.get(id=id)
    category_model_form=CategoryModelForm(instance=category)
    
    if request.method=="POST":
        category_model_form=CategoryModelForm(request.POST,instance=category)
        if category_model_form.is_valid():
            category_model_form.save()
            messages.success(request,'Category Updated Successfully')
            # return redirect('view_category')
    context={"category_form":category_model_form}
    return render(request,'categories/categorie_form.html',context)

def delete_category(request,id):
    if request.method=='POST':
        category = Category.objects.get(id=id)
        category.delete()
        messages.success(request,"Category deleted successfully")
    # return redirect('view_category')



def create_event(request): 
    event_model_form=EventModelForm()
    
    if request.method=="POST":
       event_model_form=EventModelForm(request.POST)
       
       if event_model_form.is_valid():
            event_model_form.save()
            messages.success(request,'Event Created Successfully')
            # return redirect('view_event')
    context={"event_form":event_model_form}
    return render(request,"events/event_form.html",context)

def view_event(request):
    events = Event.objects.all()
    context = {"events": events}
    return render(request, "events/event_list.html", context)


def update_event(request,id):
    event=Event.objects.get(id=id)
    event_model_form=EventModelForm(instance=event)
    
    if request.method=="POST":
        event_model_form=EventModelForm(request.POST,instance=event)
        if event_model_form.is_valid():
            event_model_form.save()
            messages.success(request,'Event Updated Successfully')
            # return redirect('view_event')
    context={"event_form":event_model_form}
    return render(request,"events/event_form.html",context)

def delete_event(request,id):
    if request.method=='POST':
        event = Event.objects.get(id=id)
        event.delete()
        messages.success(request,"Event deleted successfully")
    # return redirect('view_event')
    
    
    
def create_participant(request): 
    participant_model_form=ParticipantModelForm()
    
    if request.method=="POST":
       participant_model_form=ParticipantModelForm(request.POST)
       
       if participant_model_form.is_valid():
            participant_model_form.save()
            messages.success(request,'Participant Created Successfully')
            # return redirect('view_event')
    context={"Participant_form":participant_model_form}
    return render(request,"participants/participant_form.html",context)

def view_participant(request):
    participants = Participant.objects.all()
    context = {"participants": participants}
    return render(request, "participants/participant_list.html", context)


def update_participant(request,id):
    participant=Participant.objects.get(id=id)
    participant_model_form=ParticipantModelForm(instance=participant)
    
    if request.method=="POST":
        participant_model_form=ParticipantModelForm(request.POST,instance=participant)
        if participant_model_form.is_valid():
            participant_model_form.save()
            messages.success(request,'Participant Updated Successfully')
            # return redirect('view_event')
    context={"Participant_form":participant_model_form}
    return render(request,"participants/participant_form.html",context)

def delete_participant(request,id):
    if request.method=='POST':
        participant = Participant.objects.get(id=id)
        participant.delete()
        messages.success(request,"Participant deleted successfully")
    # return redirect('view_event')
