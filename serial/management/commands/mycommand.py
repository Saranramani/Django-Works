from django.core.management.base import BaseCommand
from serial.models import Album
from serial.models import Track

class Command(BaseCommand):
    help = 'Getting datas from album'
    
    def add_arguments(self,parser):
        parser.add_argument('id',type=str,help='Retreive album based on id')
        parser.add_argument('title',type=str,help='Retreive album based on name')

    def handle(self,*args,**kwargs):
        album_id = kwargs['id']
        track_title = kwargs['title']
        try:
            tracks = Track.objects.get(title=track_title)
            album = Album.objects.get(id=album_id)
            return self.stdout.write(f" Artist : {album.artist}, Track : {tracks.track}")   
        except Album.DoesNotExist:
            return ("For this ID Nothing in albums")
        except Track.DoesNotExist:
            return ("For this ID Nothing in tracks")
