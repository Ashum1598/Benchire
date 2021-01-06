Dict = [{'make':'Nokia', 'model':216, 'color':'Black'}, {'make':'Mi Max', 'model':'2', 'color':'Gold'}, {'make':'Samsung', 'model': 7, 'color':'Blue'}]
print("Original list of Dictonaries: ",Dict)
sorted_Dict = list(sorted(Dict,key=lambda x: x['color']))
print("sorted list of dictonaries: ",sorted_Dict)
