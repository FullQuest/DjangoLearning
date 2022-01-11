from django.shortcuts import render
from .models import Track, Artist


def tracks(request):
    tracks = Track.objects.all()  # pylint: disable=maybe-no-member
    artists = Artist.objects.all()  # pylint: disable=maybe-no-member
    context = {
        'tracks': tracks,
        'artists': artists,
        }
    return render(request, 'tracks/tracks.html', context)


def track(request, pk):

    track_obj = Track.objects.get(id=pk)  # pylint: disable=maybe-no-member

    return render(request, 'tracks/single-track.html',
                  {'track': track_obj})

