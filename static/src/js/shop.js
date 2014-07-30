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
            this.products = ["Birdhouse", "Blind", "Flip", "Atm", "Element"];
        },
        start: function() {
            var wid=new instance.skate_shop.MyWidget(this);
            wid.appendTo(this.$el);
            $("button").click(function() {
                console.log("someone clicked on the button");
                
                var id_seq=$("main").html();
                
                console.log(id_seq);
                
//                 openerp.jsonRpc( '/request_rpc', 'call', 
//                 {'prix': '40','id_seq' : id_seq})
//                 .then(function (result) {
//                     console.log(result);
//                 })
                
            });
            
                
        },
        
        events: {
            "click .ici": "button_just_clicked",
            "click .my_class": "button_just_clicked",
        },
        
        button_just_clicked: function() {
            console.log('Fourth way!');
        },
        
    });
    
    instance.web.client_actions.add('example.action', 'instance.skate_shop.action');
    
    instance.skate_shop.MyWidget = instance.web.Widget.extend({
        init: function(parent) {
            this._super(parent);
        },
        
        start: function() {
            var self=this;
            console.log('Ready!');
            
            $("#my_button").click(function() {
                self.button_clicked();
            });
            
            
        },
        
        button_clicked: function() {
            openerp.jsonRpc( '/list_skates', 'call', 
                {})
                .then(function (result) {
                    console.log(result);
                })
        },
        

    });
    
    
    
};