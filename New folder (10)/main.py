class Employee:

    # intializing (constructor)
    def __init__(self):
        print('Employee created')   


        # Deleting (destructor)
    def __del__(self):
        print('Destructor called, Employee deleted')

obj = Employee()
del obj    