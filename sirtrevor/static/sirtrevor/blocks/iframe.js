/*
 iFrame block

 */

(function ($) {

    SirTrevor.Blocks.Iframe = SirTrevor.Block.extend({

        regex_src: /(?:<iframe)(?:.+)(?:src="){1}([^"].+?)(?:")(?:.+)(?:<\/iframe>)/i,
        regex_width: /(?:<iframe)(?:.+)(?:width="){1}([^"].+?)(?:")(?:.+)(?:<\/iframe>)/i,
        regex_height: /(?:<iframe)(?:.+)(?:height="){1}([^"].+?)(?:")(?:.+)(?:<\/iframe>)/i,

        type: 'iframe',
        icon_name: 'iframe',

        title: function () {
            return 'iFrame';
        },

        toolbarEnabled: true,
        droppable: false,
        uploadable: false,
        formattable: true,

        pastable: true,

        paste_options: {
            html: '<input type="text" placeholder="Paste iFrame data here" class="st-block__paste-input st-paste-block">'
        },

        onContentPasted: function (event) {
            this.loading();

            var obj = {};
            var val = $(event.target).val();
            var match_src = this.regex_src.exec(val);

            if (match_src !== null && !_.isUndefined(match_src[1])) {
                obj.src = match_src[1];
                var match_width = val.match(this.regex_width);
                if (match_width !== null && !_.isUndefined(match_width[1])) {
                    console.log(obj.width);
                    obj.width = match_width[1];
                }

                var match_height = val.match(this.regex_height);
                if (match_height !== null && !_.isUndefined(match_height[1])) {
                    obj.height = match_height[1];
                }
                this.setAndLoadData(obj);
            }
        },

        loadData: function (data) {
            console.log("loaddata");

            data.width = (data.width == undefined || !data.width) ? '100%' : data.width;
            data.height = (data.height == undefined || !data.height) ? '100%' : data.height;

            this.$inner.prepend(
                $('<iframe>')
                    .attr('src', data.src)
                    .attr('class', 'st-block-embed')
                    .attr('width', data.width)
                    .attr('height', data.height)
            );

            this.ready();
        },

        onBlockRender: function () {
            console.log(this.getData());

        },

    });
})(django.jQuery);


