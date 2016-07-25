


class BaseBlock(object):
    pass


class ImageplusBlock(BaseBlock):
    name = 'Imageplus'

    class Media:
        js = ['sirtrevor/blocks/image_plus.js']


class HeadingExtendedBlock(BaseBlock):
    name = 'HeadingExtended'

    class Media:
        js = ['sirtrevor/blocks/heading_extended.js']


class IframeBlock(BaseBlock):
    name = 'Iframe'

    class Media:
        js = ['sirtrevor/blocks/iframe.js']
