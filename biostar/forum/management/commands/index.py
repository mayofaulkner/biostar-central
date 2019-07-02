
import logging
import os
from django.conf import settings
from django.core.management.base import BaseCommand
from biostar.forum.models import Post
from biostar.forum.search import create_index

logger = logging.getLogger('engine')


class Command(BaseCommand):
    help = 'Create search index for the forum app.'

    def add_arguments(self, parser):
        parser.add_argument('--dir', type=str, help="Directory to create index in.")

    def handle(self, *args, **options):

        index_dir = options["dir"] or settings.INDEX_DIR

        posts = Post.objects.all()

        #os.mkdir(index_dir)

        index_dir = os.path.abspath(index_dir)

        os.makedirs(index_dir, exist_ok=True)

        if not os.path.exists(index_dir):
            raise Exception("Index directory does not exist.")

        create_index(index_dir=index_dir, posts=posts)