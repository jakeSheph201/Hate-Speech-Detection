from View.View import View

view = View

class Controller:

    def startApp():
        view.showWelcome()
        Controller.startDescription()

    def startDescription():
        response = view.showDescription()
        print(response)
