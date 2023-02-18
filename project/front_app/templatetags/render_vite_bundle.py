import json

from django import template
from django.utils.safestring import mark_safe

from .. import config


register = template.Library()

@register.simple_tag
def render_vite_bundle():
    """
    Template tag to render a vite bundle.
    Supposed to only be used in production.
    For development, see other files.
    """
  
    try:
        fd = open(f"{config.VUE_BUILD}/manifest.json", "rt")
        manifest = json.load(fd)
    except:
        raise Exception(
            f"Vite manifest file not found or invalid. Maybe your {config.VUE_BUILD}/manifest.json file is empty?"
        )

    import_files_list = [f'<script type="module" src="{config.DJANGO_STATIC}/{manifest["index.html"]["file"]}"></script>']

    # Append more import files (modules) if needed - view theme/static_src/dist/
    # import_files.append()

    import_files = "".join(import_files_list)

    return mark_safe(
        f"""
    <!-- # TODO: review
    <script type="module" src="{config.DJANGO_STATIC}/{manifest['index.html']['file']}"></script>
    -->
    
    <link rel="stylesheet" type="text/css" href="{config.DJANGO_STATIC}/{manifest['index.html']['css'][0]}" />
    
    {import_files}
    """
    )
