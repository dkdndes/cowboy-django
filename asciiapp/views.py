import random
from django.http import HttpResponse
from django.shortcuts import render
from .cowboy import render_art, ASCII_ARTS

JOKES = [
    "Pod went missing—turned out to be a Job all along.",
    "Our cowboy lassoed nodes; now it’s a proper cluster.",
    "This Service had no selectors, but plenty of ambition.",
    "Yeehaw! Autoscaler grew faster than our Helm chart broke.",
    "ConfigMaps: because even cowboys need plain text wisdom."
]

def _next_index(request, key: str, modulo: int) -> int:
    idx = request.session.get(key, -1) + 1
    idx %= modulo
    request.session[key] = idx
    return idx

def home(request):
    # Reset rotation on full page view to start at the beginning each visit
    request.session['rot_idx'] = -1
    return render(request, "asciiapp/index.html")

def cowboy_api(request):
    # Deterministic rotation through both lists
    idx = _next_index(request, 'rot_idx', min(len(JOKES), len(ASCII_ARTS)))
    msg = JOKES[idx]
    art = ASCII_ARTS[idx]
    rendered = render_art(msg, art)
    return HttpResponse(f"<pre style='margin:0'>{rendered}</pre>", content_type="text/html")
