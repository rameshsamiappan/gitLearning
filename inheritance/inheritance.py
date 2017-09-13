class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent class constructor called")
        self.last_name = last_name
        self.eye_color = eye_color


ramesh = Parent("Samiappan","Red")
print(ramesh.eye_color)
