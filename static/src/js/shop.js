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
            var wid=new instance.skate_shop.MyWidget(this);
            wid.appendTo(this.$el);
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
    
    instance.skate_shop.MyWidget = instance.web.Widget.extend({
        
        init: function(parent) {
            this._super(parent);
        },
        
        start: function() {
            console.log('Ready!');
        
            $("#my_button").click(function() {
                console.log("You just clicked!");
            });
        },
    });
    
    $(document).ready(function() {
        var content = new instance.skate_shop.MyWidget();
        content.setElement($('.myclass'));
        content.start();
    });

    
};