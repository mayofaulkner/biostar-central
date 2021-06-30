import datetime
import itertools
import logging
import os
import random
from datetime import timedelta
from itertools import count, islice

import bleach
from django import template, forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.paginator import Paginator
from django.db.models import Count
from django.shortcuts import reverse
from django.utils.safestring import mark_safe
from django.utils.timezone import utc
from taggit.models import Tag
from re import IGNORECASE, compile, escape
import html2markdown

from biostar.accounts.models import Profile, Message
from biostar.forum import const, auth
from biostar.utils import helpers
from biostar.forum import markdown
from biostar.forum.models import Post, Vote, Award, Subscription, Badge

User = get_user_model()

logger = logging.getLogger("engine")

register = template.Library()


@register.simple_tag
def get_wording(filtered, prefix="Sort by:", default=""):
    """
    Get the naming and icons for limits and ordering.
    """

    display = dict(all="all time", week="this week", month="this month",
                   year="this year", rank="Latest", views="Views", today="today",
                   replies="replies", votes="Votes", visit="recent visit",
                   reputation="reputation", joined="date joined", activity="activity level",
                   rsent="oldest to newest ", sent="newest to oldest",
                   rep="sender reputation", tagged="tagged", latest="Latest")
    if display.get(filtered):
        displayed = display[filtered]
    else:
        displayed = display[default]

    wording = f"{prefix} {displayed}"

    return wording