"""
Alert Message model
templates\models\modelConfirmDinamic.html

HOW TO USE 
//In HTML 
{% if confrimAlertModel %}
    {% include 'models/modelConfirmDinamic.html'%}
{% endif %}
//In the route
alert= AlertModel(text="Continua Cosi!")
add confrimAlertModel=alert at render_template


"""

class AlertModel():
    CONST_TITLE = "Are you sure?"
    CONST_MSG = "This process cannot be undone."
    CONST_CONFIRM = "Delete"
    def __init__(self, title=CONST_TITLE
    , text=CONST_MSG, confirm=CONST_CONFIRM) -> None:
        self.title = title
        self.text = text    
        self.confirm = confirm


        