from models import Developers, Stacks, DeveloperStack

# Create, Read, Update and Delete (CRUD) Statements

def create_devs(dev_obj):
    dev_obj.save()

def read_all_devs():
    devs = Developers.query.all()
    for d in devs:
        print(f'Name: {d.name}, Age: {d.age} and Id: {d.id}')

def update_dev():
    dev = Developers.query.filter_by(name='Otacilio').first()
    dev.age = 30
    dev.save()
    
def delete_dev():
    dev = Developers.query.filter_by(name='Pedro').first()
    dev.delete()
    
if __name__ == '__main__':
    devs = [
        Developers(name="Otacilio", age=29, email="ota1@gmail.com"),
        Developers(name="Pedro", age=29, email="ota2@gmail.com"),
        Developers(name="Filho", age=29, email="ota3@gmail.com")
    ]
    
    for d in devs:
        create_devs(d)
    
    read_all_devs()
    update_dev()
    print('')
    read_all_devs()
    delete_dev()
    print('')
    read_all_devs()
