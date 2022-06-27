import uuid

def image_upload_handler(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}{ext}"
    return f'images/article_{instance.article.id}/{filename}'