from django.db import models
from conf import settings

from sirtrevor import register_block
from sirtrevor.blocks import ImageplusBlock, HeadingExtendedBlock


register_block(ImageplusBlock)
register_block(HeadingExtendedBlock)

