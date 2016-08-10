(function ($) {

    SirTrevor.Blocks.Magento = SirTrevor.Block.extend({

        type: 'magento',
        icon_name: 'link',

        title: function () {
            return 'Magento';
        },

        editorHTML: function () {
            this.magento_block_id = _.uniqueId('js-magento-');
            var magento_id = this.magento_id;
            if(this.magento_id == undefined) {
                magento_id = '';
            }
            return '<div class="st-text-block--magento" >' +
                '<label>Magento ID</label><input type="text" id="' + this.magento_block_id + '" value="' + magento_id + '">' +
                '</div>';
        },

        loadData: function (data) {
            console.log(data);
            this.magento_id = data.magento_id;
            $('#' + this.magento_block_id).val(this.magento_id);
        },

        onBlockRender: function () {
            $('#' + this.magento_block_id).val(this.magento_id);
        },

        _serializeData: function () {
            console.log(this.magento_block_id);
            var dataObj = {};
            dataObj.magento_id = $('#' + this.magento_block_id).val();
            return dataObj;
        }

    });
})(django.jQuery);