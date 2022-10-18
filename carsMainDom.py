import xml.dom.minidom

carsList = []


class Car:
    def __init__(self,companyName,model,year,price,index):
        self.companyName = companyName
        self.model = model
        self.year = year
        self.price = price
        self.index = index
        self.attribute = ""

    def __str__(self):
        return f"Company: {self.companyName}\n"+f"Model: {self.model}\n"+f"Year: {self.year}\n"+f"Price: {self.price}\n"

    def changePrice(self,newPrice):
        self.price = newPrice



def parseToCSV(listOfRecords, parser):
    index = 0
    for record in listOfRecords:
        parser[index].getElementsByTagName('companyName')[0].childNodes[0].nodeValue = str(record.companyName)
        parser[index].getElementsByTagName('model')[0].childNodes[0].nodeValue = str(record.model)
        parser[index].getElementsByTagName('year')[0].childNodes[0].nodeValue = str(record.year)
        parser[index].getElementsByTagName('price')[0].childNodes[0].nodeValue = str(record.price)
        index += 1


def main():
    domtree = xml.dom.minidom.parse('cars.xml')
    group = domtree.documentElement
    cars = group.getElementsByTagName('car')

    index = 0
    for car in cars:
        print(f"-- CAR {car.getAttribute('id')} --")

        companyName = car.getElementsByTagName('companyName')[0].childNodes[0].nodeValue
        model = car.getElementsByTagName('model')[0].childNodes[0].nodeValue
        year = car.getElementsByTagName('year')[0].childNodes[0].nodeValue
        price = car.getElementsByTagName('price')[0].childNodes[0].nodeValue


        carsList.append(Car(companyName, model, year, price, index))
        print(carsList[index])

        index += 1

    carsList[2].changePrice("10000000")

    parseToCSV(carsList,cars)

    domtree.writexml(open('cars2.xml', 'w'))

if __name__ == '__main__':
    main()