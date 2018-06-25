from django.template.loader import render_to_string


class BaseBlock(object):
    def __init__(self, block):
        """
            This is run for each block when rendering.
        """
        self.block = block
        self.template_name = 'sirtrevor/blocks/%s.html' % block['type']

    def render(self):
        """
            render this block to HTML
        """
        return render_to_string(self.template_name, self.block['data'])

    @staticmethod
    def on_register():
        """ called on registration """
        pass


class ImageplusBlock(BaseBlock):
    name = 'Imageplus'

    class Media:
        js = ['sirtrevor/blocks/image_plus.js']


class HeadingExtendedBlock(BaseBlock):
    name = 'HeadingExtended'

    class Media:
        js = ['sirtrevor/blocks/heading_extended.js']


class ImageBlock(BaseBlock):
    name = 'Image'

    class Media:
        js = ['sirtrevor/blocks/image.js']


class IframeBlock(BaseBlock):
    name = 'Iframe'

    class Media:
        js = ['sirtrevor/blocks/iframe.js']


class MagentoBlock(BaseBlock):
    name = 'Magento'

    class Media:
        js = ['sirtrevor/blocks/magento.js']
