from django.db.models.expressions import Value
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect , redirect
from .models import Post, Comment, Category , Like ,Album ,Contact
from .forms import NewCommentForm , Question
from django.core.mail import message, send_mail, BadHeaderError
from django.http import HttpResponse
from django.views.generic import ListView
from django.core.paginator import Paginator ,EmptyPage,PageNotAnInteger


def d(request):
    return render(request,'d.html')

def home(request):

    all_posts = Post.newmanager.all()
    
    return render(request, 'h.html', {'posts': all_posts})


def post_single(request, post):
    if(request.method == 'POST'):
        form = Question(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body ={
                'Name': form.changed_data['Name'],
                'Email': form.changed_data['Email'],
                'category': form.changed_data['category'],
                'question': form.changed_data['question'],
            }
            message = '\n'.join(body.values())
            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("/")
    

    post = get_object_or_404(Post, slug=post, status='published')

    allcomments = post.comments.filter(status=True)
    page = request.GET.get('page', 1)

    paginator = Paginator(allcomments, 10)
    try:
        comments = paginator.page(page)
    except PageNotAnInteger:
        comments = paginator.page(1)
    except EmptyPage:
        comments = paginator.page(paginator.num_pages)

    user_comment = None

    if request.method == 'POST':
        comment_form = NewCommentForm(request.POST)
        if comment_form.is_valid():
            user_comment = comment_form.save(commit=False)
            user_comment.post = post
            user_comment.save()
            return HttpResponseRedirect('/' + post.slug)
    else:
        comment_form = NewCommentForm()
    form = Question()
    return render(request, 'd.html', {'post': post, 'comments':  user_comment, 'comments': comments, 'comment_form': comment_form,'form':form})


class CatListView(ListView):
    template_name = 'category.html'
    context_object_name = 'catlist'

    def get_queryset(self):
        content = {
            'cat': self.kwargs['category'],
            'posts': Post.objects.filter(category__name=self.kwargs['category']).filter(status='published')
        }
        return content


def category_list(request):
    category_list = Category.objects.exclude(name='default')
    context = {
        "category_list": category_list,
    }
    return context

def question(request):
    if(request.method == 'POST'):
        form = Question(request.POST)
        if form.is_valid():
            subject = "Website Inquiry"
            body ={
                'Name': form.changed_data['Name'],
                'category': form.changed_data['category'],
                'question': form.changed_data['question'],
            }
            message = '\n'.join(body.values())
            try:
                send_mail(subject, message, 'admin@example.com', ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect("/")

    form = Question()
    return render (request , 'h.html' , {'form':form})

# like unlike code 

def album(request):
    qs=Album.objects.all()
    user = request.user
    context = {
        'qs':qs,
        'user':user
    }
    return render(request,'main.html',context)

def like(request):
    user = request.user
    if request.method == 'POST':
        album_id = request.POST.get('album_id')
        album_obj = Album.objects.get(id=album_id)
        if user in album_obj.liked.all():
            album_obj.liked.remove(user)
        else :
            album_obj.liked.add(user)
        like , created = Like.objects.get_or_create(user=user,post_id = album_id)

        if not created:
            if like.value == 'like':
                like.value = 'unlike'
            else:
                like.value = 'like'
        like.save()
    return redirect('talk:album-list')

#contact us

def contact(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name', '')
        last_name=request.POST.get('last_name', '')
        email=request.POST.get('email', '')
        phone=request.POST.get('contact_no', '')
        message=request.POST.get('message', '')
        print(first_name,last_name,email,phone,message)
        contact = Contact(first_name=first_name,last_name=last_name, email=email, phone=phone, message=message)
        contact.save()
    return render(request,"contact.html")