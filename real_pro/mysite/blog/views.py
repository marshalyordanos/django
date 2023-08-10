from django.shortcuts import render,get_list_or_404,get_object_or_404
from .models import Post
from django.contrib.auth.models import User
from django.http import Http404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


from django.views.generic import ListView
from .forms import EmailPostForm
from django.core.mail import send_mail

# Create your views here.
#  ******************* query


class PostListView(ListView):
    
    queryset = Post.objects.all()
    context_object_name = 'posts'
    paginate_by =2
    template_name = 'blog/post/list.html'

def post_list(request):
    post_list = Post.objects.all()


    
    paginator = Paginator(post_list,3)
    
    print(paginator.num_pages,paginator.object_list)
    page_no = request.GET.get('page',1)
    
    try:
        posts = paginator.page(page_no)
    except PageNotAnInteger:
        # If page_number is not an integer deliver the first page
        posts = paginator.page(1)    
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)    
    print(posts.paginator.num_pages)
    return render(request,'blog/post/list.html',{'posts':posts})


def post_detail(request,year,month,day,post):
    # try:
    #     post = Post.published.get(id=id)
    # except:
    #     return Http404("No Post fount.")   
    print(year,month,day,post)
    post = get_list_or_404(Post,slug=post,publish__year =year, publish__month=month, publish__day=day) 
    # user = get_list_or_404(User,id=post[0].author)
    print(post)
    # print(user)
    
    
    return render(request,'blog/post/detail.html',{'post':post[0]})


# email 
def post_share(request, post_id):
    # Retrieve post by id
    post = get_object_or_404(Post, id=post_id, status=Post.Status.PUBLISHED)
    sent  =False
    if request.method == 'POST':
    # Form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
        # Form fields passed validation
            cd = form.cleaned_data
            print("====================================================================================")
            print(cd)
            post_url = request.build_absolute_uri(
            post.get_absolute_url())
            subject = f"{cd['name']} recommends you read " \
            f"{post.title}"
            message = f"Read {post.title} at {post_url}\n\n" \
            f"{cd['name']}\'s comments: {cd['comments']}"

            send_mail(subject, message, 'marshalyordanos32@gmail.com',[cd['to']])

            sent = True
    # ... send email
    else:
        form = EmailPostForm()
    return render(request, 'blog/post/share.html', {'post': post,
    'form': form})

























'''
post = Post.objects.all()
    .filter(publish__year =2001,author__username='marshal')
    .exclude(title__startswith='why')
post = Post.objects.get(id=1)
post.delete()

post = Post(title="aa", slug="dd" ...)
post.save()

Post.objects.create(title="dk", slug='d')


'''