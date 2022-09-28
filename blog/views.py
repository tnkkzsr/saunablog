from django.views.generic import TemplateView

# Create your views here.
class IndexView(TemplateView):
    template_name = "index.html"

class PostingView(TemplateView):
    template_name = "posting.html"

class PostslistView(TemplateView):
    template_name = "postslist.html"