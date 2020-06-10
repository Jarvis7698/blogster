from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
		ListView, DetailView, 
		CreateView, UpdateView,
		DeleteView
	)
from . models import Post

def index(request):

	context = {
		'title' : 'Home',
		'posts' : Post.objects.all()
	}

	return render(request, 'blog/index.html', context)



class PostListView(ListView):
	model = Post
	template_name = 'blog/index.html' #<app>/<model>_<view>
	context_object_name = 'posts'
	ordering = ['-post_date']



class PostDetailView(DetailView):
	model = Post



class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['post_title', 'post_content']

	def form_valid(self, form):
		form.instance.post_author = self.request.user
		return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['post_title', 'post_content']

	def form_valid(self, form):
		form.instance.post_author = self.request.user
		return super().form_valid(form)

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.post_author:
			return True
		else:
			return False



class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.post_author:
			return True
		else:
			return False


def about(request):

	context = {
		'title' : 'About',
	}

	return render(request, 'blog/about.html', context)
