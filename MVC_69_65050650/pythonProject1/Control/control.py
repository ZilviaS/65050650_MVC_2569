from Model.model import Model

class Controller:
    def __init__(self):
        self.model = Model()

    def authentication(self,username,password):
        return self.model.authentication(username,password)

    def getAllPromised(self):
        return self.model.getAllPromised()

    def searchPromisedDetail(self, id):
        if not id[0] == 'P':
            return "Error, ID first letter is P"
        elif not len(id) == 4:
            return "Error, ID contain only 4 letter"
        result = self.model.searchPromisedDetail(id)
        print(result)
        return result

    def updatePromised(self, data):
        print(data[0])
        if not data[0][0] == 'P':
            return "Error, ID first letter is P"
        elif not len(data[0]) == 4:
            return "Error, ID contain only 4 letter"
        return self.model.updatePromised(data)

    def lookup(self):
        return self.model.lookup()


