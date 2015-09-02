def boys_and_girls(): 
	with open("/home/ugd/mmllee/PP/PRSAVES/names.txt", 'r') as f:
		for line in f:
		    if 'Ms.' in line:
		        return line    
	
student= boys_and_girls()
print student.rstrip() 
