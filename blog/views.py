from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.models import Post


class BlogCreate(CreateView):
    model = Post
    fields = ('title', 'description', 'image', 'is_published')
    success_url = reverse_lazy('blog:blog')
    template_name = 'blog/post_form.html'
    context = {
        'page_title': 'Create Post'
    }

    def form_valid(self, form):
        new_mat = form.save(commit=False)
        new_mat.slug = slugify(new_mat.title)
        new_mat.save()
        return super().form_valid(form)


class BlogUpdate(UpdateView):
    model = Post
    fields = ('title', 'description', 'image', 'is_published')
    context = {
        'page_title': 'Update Post'
    }

    def form_valid(self, form):
        new_mat = form.save(commit=False)
        new_mat.slug = slugify(new_mat.title)
        new_mat.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:view', args=[self.object.pk])


class BlogList(ListView):
    model = Post
    context = {
        'page_title': 'Блог'
    }

    def get_queryset(self):
        return super().get_queryset().filter(is_published=True)


class BlogDetail(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        post.views_count += 1
        post.save()
        context['title'] = post.title
        return context


class BlogDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('blog:blog')
    context = {
        'page_title': 'Delete Post'
    }
