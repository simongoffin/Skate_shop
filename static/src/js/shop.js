openerp.skate_shop = function(instance) {
    var _t = instance.web._t,
        _lt = instance.web._lt;
    var QWeb = instance.web.qweb;

    instance.skate_shop = {};

    instance.skate_shop.action = instance.web.Widget.extend({
        template: "MyTemplate",
        init: function(parent) {
            this._super(parent);
            this.name = "Simon";
        },
        start: function() {
            $("button").click(function() {
                console.log("someone clicked on the button");
                
                
                
                var def1 = $.ajax("/service_plus", {
                    type: "POST",
                    dataType: "json",
                    data: JSON.stringify({
                        "a": 3,
                        "b": 5,
                    }),
                    contentType: "application/json",
                });

                var def2 = $.ajax("/service_plus", {
                    type: "POST",
                    dataType: "json",
                    data: JSON.stringify({
                        "a": 6,
                        "b": 7,
                    }),
                    contentType: "application/json",
                });

                $.when(def1, def2).then(function(result1, result2) {
                    console.log("3+5=", result1[0].addition);
                    console.log("6+7=", result2[0].addition);
                });
                
                });
            },
    });

    instance.web.client_actions.add('example.action', 'instance.skate_shop.action');

    
};