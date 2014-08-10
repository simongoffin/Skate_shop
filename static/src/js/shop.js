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
                
                openerp.jsonRpc( '/request_rpc', 'call', 
                {'prix': '40'})
                .then(function (result) {
                    console.log(result);
                })
                
            });
            
                
        },
        
        events: {
            "click .ici": "button_just_clicked",
        },
        
        button_just_clicked: function() {
            console.log('Fourth way!');
        },
        
    });
    
    instance.web.client_actions.add('example.action', 'instance.skate_shop.action');
    
    
};