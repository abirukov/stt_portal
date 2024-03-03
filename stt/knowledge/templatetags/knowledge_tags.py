from django import template

from stt.knowledge.models import KnowledgePage

register = template.Library()

# Retrieves a single gallery item and returns a gallery of images


@register.inclusion_tag("tags/knowledge_section.html", takes_context=True)
def knowledge_section(context):
    knowledge = KnowledgePage.objects.all()
    return {
        "knowledge": knowledge,
        "request": context["request"],
    }
