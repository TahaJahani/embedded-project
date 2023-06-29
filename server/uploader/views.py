from django.http import JsonResponse
from django.views import View

from .forms import ImageForm


# Create your views here.
class UploadImageView(View):
    http_method_names = ['post']

    def post(self):
        form = ImageForm(self.request.POST, self.request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse(data={"message": "success"})
        else:
            return JsonResponse(data={"message": "failed"}, status=400)