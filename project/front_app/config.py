from pathlib import Path 



DJANGO_STATIC_RELATIVE = 'static'

DJANGO_STATIC = f"/{DJANGO_STATIC_RELATIVE}"

VUE_BUILD = Path(__file__).resolve().parent / 'static'
