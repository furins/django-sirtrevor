import json
from django.template.loader import render_to_string
import six

from sirtrevor.blocks import ImageplusBlock, HeadingExtendedBlock, IframeBlock
from sirtrevor.blocks import MagentoBlock


class SirTrevorContent(six.text_type):
    @property
    def html(self):
        html = []
        if len(self):
            content = json.loads(self)
            for block in content['data']:
                template_name = 'sirtrevor/blocks/%s.html' % block['type']
                data = custom_blocks_registry[block['type']].pre_render(block['data'])
                html.append(render_to_string(template_name, data))
        return u''.join(html)


custom_blocks_registry = {}


def register_block(block, name=None):
    if name is None:
        name = block.name
    custom_blocks_registry[name] = block


register_block(ImageplusBlock)
register_block(HeadingExtendedBlock)
register_block(IframeBlock)
register_block(MagentoBlock)
