from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView
from .forms import EmailPostForm, CommentForm

# Create your views here.

def post_list(request):
	posts = Post.published.all()
	paginator = Paginator(posts, 1)
	page = request.GET.get('page')
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		# if page is not an integer deliver the first page
		posts = paginator.page(1)
	except EmptyPage:
		# if page is out of range deliver last page of results
		posts = paginator.page(paginator.num_pages)

	return render(request, 'blog/post-list.html', {'posts': posts})	

def post_share(request, post_id):
	post = get_object_or_404(Post, id=post_id, status='published')
	if request.method == 'POST':
		form = EmailPostForm(request.POST)
		if form.is_valid():
			cd = form.cleaned_data
			# send email
	else:
		form = EmailPostForm()
	return render(request, 'blog/share.html', {'post': post, 'form': form})



class PostListView(ListView):
	queryset = Post.published.all()
	context_object_name = 'posts'
	paginate_by = 3
	template_name = 'blog/post-list.html'

def post_detail(request, post):
	post = get_object_or_404(Post, slug=post, status='published',)
	#  publish__year=year, publish__month=month, publish__day=day

	comments = post.comments.filter(active=True, parent=None)

	new_comment = None
	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			parent_obj = None
			try:
				parent_id = int(request.POST.get('parent_id'))
			except:
				parent_id = None
			if parent_id:
				parent_qs = Comment.objects.filter(id=parent_id)
				if parent_qs.exists() and parent_qs.count() == 1:
					parent_obj = parent_qs.first()

			new_comment = comment_form.save(commit=False) # this is because we did not relate post yet
			new_comment.post = post
			new_comment.parent = parent_obj
			new_comment.save()
			return redirect(post.get_absolute_url())

	else:
		comment_form = CommentForm()

	return render(request, 'blog/post-detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})


