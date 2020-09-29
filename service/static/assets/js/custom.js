!(function ($) {
    "use strict";

    $(".main-purpose-filter").change(function () {
        var purpose = this.value;
        console.log(purpose);

        $(".container .row.content").each(function () {
            if (purpose == 'all') {
                $(this).show();
                return 0;
            }
            
            var pursope_text = $(this).find(".main-purpose").text(); 

            console.log(pursope_text);

            if ( pursope_text.indexOf(purpose) == -1 ) {
                $(this).hide();
            } else {
                $(this).show();
            }
        });

    });

    $('[data-toggle="tooltip"]').tooltip();

})(jQuery);