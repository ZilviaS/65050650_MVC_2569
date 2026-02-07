import csv

class Model:
    def __init__(self):
        self.data = []
        self.adminData = ["admin","admin"]
        self.userData = ["user","user"]

    def authentication(self,username,password):
        if self.adminData[0] == username and self.adminData[1] == password:
            return 0
        elif self.userData[0] == username and self.userData[1] == password:
            return 1

    def getAllPromised(self):
        output = self.csv_read('Model/Promises.csv')
        output.sort(key=lambda x: x[3])
        return output

    def searchPromisedDetail(self, id):
        outputDetail = self.csv_read('Model/Promises.csv')
        result = []
        for i in outputDetail:
            if i[0] == id:
                result = i
        if len(result) == 0:
            return [0,"ID not found"]

        update = self.findUpdates(id)
        return [1,result + update]

    def lookup(self):
        politicianID = []
        data = self.csv_read('Model/Politicians.csv')
        for i in data:
            politicianID.append(i[0])
        promise = self.csv_read('Model/Promises.csv')
        mem = []
        output = []
        ext = ""
        for i in range(len(data)):
            for j in promise:
                if politicianID[i] == j[1]:
                    j.pop(1)
                    mem.append(j)
                    print(j)
                ext += ",".join(map(str, mem))
                mem.clear()
            output.append(politicianID[i] + ext)
            ext = ""
        return output










    def updatePromised(self,data):
        promiseData = self.csv_read('Model/Promises.csv')
        result = []
        for i in promiseData:
            if data[0] == i[0]:
                if i[4] == "Abandoned":
                    return "Error, this promissed is Abandon"
                result = i
        if len(result) == 0:
            return "Error, ID not found"
        self.updateCSV(data, 'Model/Promises.csv')
        return "Success"

    def findPolitician(self,id):
        politicians = self.csv_read('Model/Politicians.csv')
        result = []
        for i in politicians:
            if i[0] == id:
                result = i
        return result

    def findUpdates(self,id):
        updates = self.csv_read('Model/PromiseUpdates.csv')
        result = []
        for i in updates:
            if i[0] == id:
                i.pop(0)
                result.append(i)
        return result

    def csv_read(self,file_path):
        output = []
        counter = 0
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_file = csv.reader(file)
            for row in csv_file:
                if not counter == 0:
                    output.append(row)
                counter += 1
            return output
    def updateCSV(self,data,file_path):
        new_data = []
        with open(file_path, mode='r', newline='', encoding='utf-8') as file:
            csv_file = csv.reader(file)
            for row in csv_file:
                new_data.append(row)
        new_data.append(data)
        with open(file_path, 'w', newline='',encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerows(new_data)
