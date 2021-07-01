#!/usr/bin/python3

class CardDao():

    def __init__(self): # constructor
        super().__init__()
        self.create()
        self.return()
        self.update()
        self.delete()
        self.populate()
         
    def create(self): # there will be create for cards
        print('Create')

    def return(self):
        print('Read')

    def update(self):
        print('Update')

    def delete(self):
        print('Delete')

    def populate(self):
        print('Populate')


def main():
    run = CardDao()
    

if __name__ == '__main__':
    main()