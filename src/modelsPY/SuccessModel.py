"""
Success Message model
templates\models\modelSuccessDinamic.html


HOW TO USE 
//In HTML 
{% if successModel %}
    {% include 'models/modelSuccessDinamic.html'%}
{% endif %}
//In the route
success= SuccessModel(text="Continua Cosi!")
add successModel=success at render_template


"""

class SuccessModel():
    CONST_TITLE = "Awesome!"
    CONST_MSG = "Your booking has been confirmed. Check your email for detials."
    CONST_CONFIRM = "OK"
    def __init__(self, title=CONST_TITLE
    , text=CONST_MSG, confirm=CONST_CONFIRM) -> None:
        self.title = title
        self.text = text    
        self.confirm = confirm


        