"""
# Zadanie #11Zaimplementuj klasy odpowiedzialne za tworzenie dokumentów w składni MarkDown.
Stwórz klasę bazową `Element` zawierającą podstawową implementację metody `render()`
oraz kilka jej klas pochodnych. Stwórz klasę `Document` umożliwiającą wyrenderowanie dodanych elementów.
Przykład użycia:
>>> document = Document()
>>> document.add_element(HeaderElement('Header'))
>>> document.add_element(LinkElement('ABC', 'abc.com'))
>>> document.add_element(Element('Simple'))
>>> document.render()
Header
======
[ABC](http://abc.com)
Simple
"""
class Document:
    lista = []
    def __init__(self):
        pass


    def add_element(self, argument):
        self.lista.append(argument)

    def render(self):
        string = ''
        for i in self.lista:
            string += i.render()
        return string




class Element:
    text = ''
    def __init__(self, text):
        self.text = text

    def render(self):
        return self.text


class HeaderElement(Element):
    def render(self):
        text = super().render()
        return text + "\n" + "=" * len(text)+ "\n"


class LinkElement(Element):
    text1 = ''
    text2 = ''

    def __init__(self, text1, text2):
        self.text1 = text1
        self.text2 = text2

    def render(self):
        text = super().render()
        return f'[ {self.text1} ]' + f'(http://{self.text2}) '+ "\n"




dokument = Document()
dokument.add_element(HeaderElement('Header'))
dokument.add_element(LinkElement('ABC', 'abc.com'))
dokument.add_element(LinkElement('DDD', 'ddd.com'))
dokument.add_element(Element('simple'))
print(dokument.render())