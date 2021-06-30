#!/usr/bin/python3

class cardDao():

    def __init__(self): # constructor
        super().__init__()
        self.create()
        self.read()
        self.update()
        self.delete()
        self.populate()
         
    def create(self): # there will be create for cards
        print('Create')

    def read(self):
        print('Read')

    def update(self):
        print('Update')

    def delete(self):
        print('Delete')

    def populate(self):
        print('Populate')


def main():
    run = cardDao()
    

if __name__ == '__main__':
    main()