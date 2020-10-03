from django.shortcuts import render, redirect

from django.views.generic import View, TemplateView, ListView,  DetailView, UpdateView
from .models import Blog,BlogCategory,Comment
from .forms import Contact,CommentForm

# Create your views here.
class Home(TemplateView):
    template_name = 'base.html'

# def home(request):
#     template = 'base.html'
#     return render(request, template)

class BlogListView(ListView):
    form = Contact()
    model = Blog
    template_name = 'Blog/blog_list.html'
    context_object_name = 'blog_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form
        return context

    def post(self, request, *args, **kwargs):
        form = Contact(request.POST)
        if form.is_valid():
            form.save(commit=True)
        else:
            print('ERROR FORM INVALID')
        return redirect("/")




# def bloglist(request):
#     bloglist = Blog.objects.all()
#     template = 'Blog/blog_list.html'
#
#     form = Contact()
#     if request.method == "POST":
#         form = Contact(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             return home(request)
#         else:
#             print('ERROR FORM INVALID')
#
#     context = {'blog_list':bloglist, 'form':form}
#     return render(request, template, context)

def blogdetail(request, blog_slug):
    print(blog_slug)
    blogdetail = Blog.objects.get(slug=blog_slug)
    blogcategory = Blog.objects.filter(category=blogdetail.category).order_by('blog_published')
    blogdetail_idx = list(blogcategory).index(blogdetail)
    comments = Comment.objects.filter(blog=blogdetail, reply=None).order_by('-id')

    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(blog=blogdetail, user=request.user, content=content, reply=comment_qs)
            comment.save()
    else:
        comment_form = CommentForm()

    template = 'Blog/blog_detail.html'
    context = {'blog_detail':blogdetail, 'sidebar':blogcategory, 'blog_idx':blogdetail_idx, 'comments':comments, 'comment_form':comment_form}
    return render(request, template, context)
