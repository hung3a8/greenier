import os
import uuid
from urllib.parse import urljoin

from django.conf import settings
from django.core.files.storage import default_storage
from django.http.response import JsonResponse
from django.views.decorators.http import require_POST


def image_uploader(image):
    ext = os.path.splitext(image.name)[1]
    if ext not in settings.SAFE_IMAGE_EXTENSIONS:
        ext = '.png'
    name = str(uuid.uuid4()) + ext
    default_storage.save(os.path.join(settings.IMAGE_UPLOAD_DIR, name), image)
    url_base = getattr(settings, 'MARTOR_UPLOAD_URL_PREFIX',
                       urljoin(settings.MEDIA_URL, settings.IMAGE_UPLOAD_DIR))
    if not url_base.endswith('/'):
        url_base += '/'
    return {'status': 200, 'name': '', 'link': urljoin(url_base, name)}


@require_POST
def upload_image(request):
    file = request.FILES.get('file', None)
    if file is not None:
        return JsonResponse(image_uploader(file))
    else:
        return JsonResponse({'status': 400, 'name': '', 'link': ''})
