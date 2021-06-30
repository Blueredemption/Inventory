#!/usr/bin/python3

class userDao():
    cat = 25 # global bavariable for test

    def __init__(self): # constructor
        super().__init__()
        self.create()
        self.read()
        self.update()
        self.delete()
        self.populate()
         
    def create(self): # there will be create for collection and container
        print('Create' +str(self.cat))

    def read(self):
        print('Read')

    def update(self):
        print('Update')

    def delete(self):
        print('Delete')

    def populate(self):
        print('Populate')


def main():
    run = userDao()
    print(str(run.cat))
    

if __name__ == '__main__':
    main()