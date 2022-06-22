def image_upload_handler(instance, filename):
    return f'images/article_{instance.article.id}/{filename}'