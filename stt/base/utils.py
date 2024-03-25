import os
import shutil
import subprocess
import uuid

from django.apps import apps
from django.core.files.base import File
from django.forms.utils import flatatt
from django.utils.html import format_html, format_html_join
from django.utils.translation import gettext_lazy as _
from wagtail.documents.models import Document
from wagtail.models import Page
from wagtailmedia.models import AbstractMedia

from stt.settings.base import BASE_DIR


def format_video_html(item: AbstractMedia) -> str:
    return format_html(
        "<video width='80%' controls>\n{sources}\n<p>{fallback}</p>\n</video>",
        sources=format_html_join(
            "\n",
            "<source{0}>",
            [[flatatt(s)] for s in item.sources],
        ),
        fallback=_("Your browser does not support the video element."),
    )


def get_real_page_model(page: Page) -> Page | None:
    content_type = page.content_type
    return apps.get_model(
        app_label=content_type.app_label,
        model_name=content_type.model,
    )


def convert_to_pdf(source: str) -> str | None:
    if not shutil.which("libreoffice"):
        return None
    folder = f"{BASE_DIR}/media/documents/pdf_samples/{uuid.uuid4()}"
    if not os.path.exists(folder):
        os.makedirs(folder)
    filename = os.path.split(os.path.abspath(source))[1].split(".")[0]
    args = [
        "libreoffice",
        "--headless",
        "--convert-to",
        "pdf",
        "--outdir",
        folder,
        source,
    ]
    subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    return f"{folder}/{filename}.pdf"


def create_document(filepath: str, title: str) -> Document:
    doc_file = File(open(filepath, "rb"), name=os.path.basename(filepath))
    doc = Document(
        title=title,
        file=doc_file,
    )
    doc.save()
    return doc
