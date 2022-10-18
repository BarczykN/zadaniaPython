import xml.sax

class CarsHandler(xml.sax.handler.ContentHandler):

    def startElement(self, name, attrs):
        self.current = name
        if name == "car":
            print(f"-- CAR {attrs['id']} --")

    def characters(self, content):
        if self.current == "companyName":
            self.companyName = content
        elif self.current == "model":
            self.model = content
        elif self.current == "year":
            self.year = content
        elif self.current == "price":
            self.price = content

    def endElement(self, name):
        if self.current == "companyName":
            print(f"Company: {self.companyName}")
        elif self.current == "model":
            print(f"Model: {self.model}")
        elif self.current == "year":
            print(f"Year: {self.year}")
        elif self.current == "price":
            print(f"Price: {self.price}")
        self.current = ""




def main():
    handler = CarsHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse('cars.xml')


if __name__ == '__main__':
    main()