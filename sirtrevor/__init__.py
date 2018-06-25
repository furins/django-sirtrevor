import json
import six

from sirtrevor.blocks import \
    BaseBlock, ImageplusBlock, HeadingExtendedBlock, \
    IframeBlock, MagentoBlock, ImageBlock


class SirTrevorContent(six.text_type):
    @property
    def html(self):
        html = []
        if len(self):
            content = json.loads(self)
            for block in content['data']:
                try:
                    blocktype = custom_blocks_registry[block['type']]
                except KeyError:
                    blocktype = BaseBlock

                classed = blocktype(block)
                html.append(classed.render())
        return u''.join(html)


custom_blocks_registry = {}


def register_block(block, name=None):
    if name is None:
        name = block.name
    custom_blocks_registry[name] = block


register_block(ImageplusBlock)
register_block(ImageBlock)
register_block(HeadingExtendedBlock)
register_block(IframeBlock)
register_block(MagentoBlock)
