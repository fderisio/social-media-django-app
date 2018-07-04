from django.http import Http404, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from project.motion_app.models import PostItem, User
from project.motion_app.models import PostItemForm


class OverviewView(TemplateView):
    template_name = 'overview.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = PostItem.objects.all().order_by('-created')
        return context


class PostDetailsView(TemplateView):
    template_name = 'post_details.html'

    def get_context_data(self, post_id, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['post'] = PostItem.objects.get(id=post_id)
        except PostItem.DoesNotExist:
            raise Http404
        return context

    # def get_context_data(self, post_id, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     try:
    #         context['user'] = User.objects.get(id=user_id)
    #     except User.DoesNotExist:
    #         raise Http404
    #     context['posts'] = PostItem.objects.filter(user=user_id).order_by('-created')
    #     return context


class NewPostView(FormView):
    template_name = 'new_post.html'
    success_url = reverse_lazy('overview')
    form_class = PostItemForm

    def form_valid(self, form):
        PostItem.objects.create(
            user=self.request.user,
            title=form.cleaned_data.get('title'),
            content=form.cleaned_data.get('content'),
        )
        return super().form_valid(form)


class NewPostTemplateView(TemplateView):
    template_name = 'new_post.html'
    success_url = reverse_lazy('overview')
    form_class = PostItemForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)
        form = self.form_class(request.POST)
        if form.is_valid():
            PostItem.objects.create(
                user=self.request.user,
                title=form.cleaned_data.get('title'),
                content=form.cleaned_data.get('content'),
            )
            return HttpResponseRedirect(self.success_url)
        context['form'] = form
        return self.render_to_response(context)

    # def get_context_data(self, user_id, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     try:
    #         context['user'] = User.objects.get(id=user_id)
    #     except User.DoesNotExist:
    #         raise Http404
    #     context['form'] = self.form_class()
    #     return context
