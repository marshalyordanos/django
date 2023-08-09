from django.shortcuts import render,get_list_or_404
from .models import Post
from django.contrib.auth.models import User
from django.http import Http404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger


from django.views.generic import ListView


# Create your views here.
#  ******************* query


class PostListView(ListView):
    
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by =3
    template_name = 'blog/post/list.html'

def post_list(request):
    post_list = Post.objects.all()
    
    paginator = Paginator(post_list,3)
    
    print(paginator.num_pages,paginator)
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