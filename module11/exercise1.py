class Publication:
    def __init__(self,name):
        self.name =name
    def print_information(self):
        print(f"Publication: {self.name}")


class Book (Publication):
    def __init__(self, name, author, page_count):
        self.author=author
        self.page_count=page_count
        #call BASE INIT vs name property
        super().__init__(name)
    def print_information(self):
        #call method print_information from BASE class
        super().print_information()
        print(f"Author: {self.author}\nPage count: {self.page_count}")


class Magazine(Publication):
    def __init__(self, name, chief_editor):
        self.chief_editor=chief_editor
        #CALL BASE INIT vs name property
        super().__init__(name)
    def print_information(self):
        #call method print_information from BASE class
        super().print_information()
        print(f"chief_editor: {self.chief_editor}")
