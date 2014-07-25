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
                
                var id_seq=$("main").html();
                
                console.log(id_seq);
                
                openerp.jsonRpc( '/request_rpc', 'call', 
                {'prix': '40','id_seq' : id_seq})
                .then(function (result) {
                    console.log(result);
                })
                
            });
            
                
            },
    });

    instance.web.client_actions.add('example.action', 'instance.skate_shop.action');

    
};