import pdfkit
from django.conf import settings


class PdfKit(object):

    @staticmethod
    def pdfkit_base_options():
        return {
            'page-size': 'Letter',
            'margin-top': '0.25in',
            'margin-right': '0.25in',
            'margin-bottom': '0.25in',
            'margin-left': '0.25in',
            'encoding': "UTF-8",
            'no-outline': None,
        }

    @classmethod
    def create_pdf(cls, url=None, filename=None, target=None, options=None):
        if options is None:
            options = cls.pdfkit_base_options()

        if target is None:
            target = settings.MEDIA_ROOT

        if filename is None:
            filename = 'pdf-file'

        path = '{}/{}.pdf'.format(target, filename)
        full_url = '{}{}'.format(settings.BASE_URL, url)
        print full_url
        pdfkit.from_url(full_url, path, options=options)
