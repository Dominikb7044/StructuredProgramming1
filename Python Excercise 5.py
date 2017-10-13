Python 3.5.4rc1 (v3.5.4rc1:385b368, Jul 24 2017, 14:37:10) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> values = input("Insert some numbers seperated by commas : ")
Insert some numbers seperated by commas : 3,5,7,23
>>> list = values.split(",")
>>> tuple = tuple(list)
>>> print('List : ',list)

List :  ['3', '5', '7', '23']
>>> print('Tuple : ',tuple)
Tuple :  ('3', '5', '7', '23')
>>> #This Program Turns comma seperated numbers into a list and tuple

