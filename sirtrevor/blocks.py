


class BaseBlock(object):
    def pre_render(self, blockdata):
        """
            Over-ride this method to insert data into your block.
        """
        return blockdata


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


class MagentoBlock(BaseBlock):
    name = 'Magento'

    class Media:
        js = ['sirtrevor/blocks/magento.js']
