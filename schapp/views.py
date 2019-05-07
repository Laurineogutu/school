from django.shortcuts import render, get_object_or_404
from . models import Staff, Event, Department, Club, Mission, Vision, Anthem, Motto, Sport, Post, Message, Comment
from django.views.generic import CreateView


# Create your views here.
def index(request):
    staffs = Staff.objects.all()
    events = Event.objects.all()
    clubs = Club.objects.all()
    missions = Mission.objects.all()
    visions = Vision.objects.all()
    anthems = Anthem.objects.all()
    mottos = Motto.objects.all()
    posts = Post.objects.all()

    context = {'staffs': staffs, 'events': events, 'clubs': clubs, 'missions': missions, 'visions': visions, 'anthems': anthems, 'mottos': mottos, 'posts': posts}
    return render(request, 'schapp/index.html', context)


def departments(request):
    dpars = Department.objects.all()
    return render(request, 'schapp/departments.html', {'dpars': dpars})


def clubs(request):
    cbs = Club.objects.all()
    return render(request, 'schapp/clubs.html', {'cbs': cbs})


def sports(request):
    sprts = Sport.objects.all()
    return render(request, 'schapp/sports.html', {'sprts': sprts})



class MessageCreateView(CreateView):
    model = Message
    fields = ('name', 'email', 'subject', 'message')
    template_name = 'schapp/contact.html'



class CommentCreateView(CreateView):
    model = Comment
    fields = ['Comment']

    def form_valid(self, form, **kwargs):
        post = get_object_or_404(Post, pk=self.kwargs.get('pk'))
        form.instance.post = post
        return super().form_valid(form)













