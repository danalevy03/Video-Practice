from Chef import Chef

myChef = Chef()
myChef.make_special_dish()
# The chef makes bbq ribs

from ChineseChef import ChineseChef

myChineseChef = ChineseChef()
myChineseChef.make_chicken()
myChineseChef.make_special_dish()
# The chef makes orange chicken

myChineseChef.make_fried_rice()
# The chef makes fried rice

# Inheritance is a way to form new classes using classes that have already been defined.
# The newly formed classes are called derived classes,
# the classes that we derive from are called base classes.
# Important benefits of inheritance are code reuse and reduction of complexity of a program.
# The derived classes (descendants) override or extend the functionality of base classes (ancestors).