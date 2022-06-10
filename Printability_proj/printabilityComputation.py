import numpy as np

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~	PG (GLOBAL PRINTABILITY)	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

def globalPrintability(data,technology,application):



	################  QSCM COMPUTATION ##################
	QScm = 0.0
	areaCAD = 0.0
	areaSTL = 0.0


	if data["Area_STL"] == []:
		QScm = 1
	else:
		areaCAD = data["Area_CAD"][0]
		areaSTL = data["Area_STL"][0]
		QScm = areaSTL / areaCAD




	################  K ASSIGNMENT ##################

	#k = [Accuracy, Surface Texture, Various Abnormalities, Support]
	k = [0.0, 0.0, 0.0, 0.0]
	
	# ~~~~~~~ APPLICATION : BIOMEDICAL ~~~~~~~
	if (application == 0):	
		k = [0.9, 0.9, 0.9, 0.9]				
	
	# ~~~~~~~ APPLICATION : MECHANICAL  ~~~~~~~
	elif (application == 1):
		k = [0.9, 0.5, 0.9, 0.5]
	
	# ~~~~~~~ APPLICATION : ARTISTIC ~~~~~~~
	elif (application == 2):
		k = [0.1, 0.9, 0.1, 0.9]	


	################  DSt_PERFECT ASSIGNMENT ##################

	# dsPerfect = [Accuracy, Surface Texture, Various Abnormalities, Support]
	dsPerfect = [0.0, 0.0, 0.0, 0.0]
	
	# ~~~~~~~ TECHNOLOGY : FDM ~~~~~~~
	if (technology == 0):
		dsPerfect = [0.03, 0.05, 0.05, 0.03]


	# ~~~~~~~ TECHNOLOGY : MJ ~~~~~~~
	elif (technology == 1):
		dsPerfect = [0.01, 0.01, 0.01, 0.03]
	
	# ~~~~~~~ TECHNOLOGY : BJ ~~~~~~~
	elif (technology == 2):
		dsPerfect = [0.03, 0.03, 0.03, 0.01]

	 ################  DSt COMPUTATION / PG COMPUTATION  ##################

	DSt = [0.0, 0.0, 0.0, 0.0]
	PG = 1
	for x in range (len(DSt)):
		DSt[x] =  1 - (1 - dsPerfect[x]) * QScm
		PG = PG * (1 - DSt[x] * k[x])
	

	return PG

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	PF equation		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

def partCharacteristicEquation(w, c, s, d, e):
	pf = (1 - (1 / (1 + np.exp((w-(d-e))*c)))) * s
	return pf

def partCharacteristicEquationEmEng(w, c, s,w1, c1, s1, d1,d2,e):
	pf = (1 - ((1 / (1 + np.exp((w-(d1-e))*c)))*(1 / (1 + np.exp((w1-(d2-e))*c1))))) * s1
	return pf

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~	PF (PART CHARACTERISTIC PRINTABILITY)	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ *

def partCharacteristicPrintability(data, technology, application):


	##############  w(T,i) - critical values ASSIGNMENT / c(T,i) - coefficient ASSIGNMENT ##############
	
	# Holes, Pins, Supported, UnSupported, Embossed Width, Embossed Height, Engraved Width, Engraved Height, Thin Feature
	w = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
	
	# Holes, Pins, Supported, UnSupported, Embossed Width, Embossed Height, Engraved Width, Engraved Height, Thin Feature
	c = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

	# ~~~~~~~ TECHNOLOGY : FDM ~~~~~~~
	if (technology == 0):
		w = [2.0, 3.0, 0.8, 0.8, 0.6, 2.0, 0.6, 2.0, 2.0]
		
		c = [1.246, 0.827, 3.17, 3.17, 4.266, 1.246, 4.266, 1.246, 1.246]

	
	# ~~~~~~~ TECHNOLOGY : MJ ~~~~~~~
	elif (technology == 1):
		w = [0.5, 0.5, 1.0, 1.0, 0.5, 0.5, 0.5, 0.5, 0.5]
		
		c = [1.246, 0.827, 3.17, 3.17, 4.266, 1.246, 4.266, 1.246, 1.246]
	
	
	# ~~~~~~~ TECHNOLOGY : BJ ~~~~~~~
	elif (technology == 2):	
		w = [1.5, 2.0, 2.0, 3.0, 0.5, 0.5, 0.5, 0.5, 2.0]
		
		c = [1.67, 1.246, 1.246, 0.827, 5.156, 5.156, 5.156, 5.156, 1.246]

	
	

	# ##########  S(A,i) -  Significance ASSIGNMENT ############
	# Holes, Pins, Supported, UnSupported, Embossed, Engraved, Thin Feature
	S = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
	# ~~~~~~~ APPLICATION : BIOMEDICAL ~~~~~~~
	if (application == 0):
		S = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
	
	# ~~~~~~~ APPLICATION : MECHANICAL  ~~~~~~~
	elif (application == 1):
		S = [1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
	
	# ~~~~~~~ APPLICATION : ARTISTIC ~~~~~~~
	elif (application == 2): 
		S = [0.1, 0.3, 0.3, 0.3, 0.3, 0.3, 1.0]
	
	
	PF = 1.0
	PF_curr = 0.0

	if (not(data["Holes"] == [])):				# Holes PF computation
		
		for i in range (len(data["Holes"])):
			
			if len(data["Holes"][i]) == 2:
				d = data["Holes"][i][0]
				e = data["Holes"][i][1]
			elif len(data["Holes"][i]) == 1:
				d = data["Holes"][i][0]
				e = 0.0
			else:
				#print(d)
				print("Something went wrong...")


			PF_curr = 1 - partCharacteristicEquation(w[0], c[0], S[0], d, e)
			PF = PF * PF_curr

		

	

	if (not(data["Pins"] == [])):					# Pins PF computation

		for i in range (len(data["Pins"])):
			
			if len(data["Pins"][i]) == 2:
				d = data["Pins"][i][0]
				e = data["Pins"][i][1]
			elif len(data["Pins"][i]) == 1:
				d = data["Pins"][i][0]
				e = 0.0
			else:
				print("Something went wrong...")

			PF_curr = 1 - partCharacteristicEquation(w[1], c[1], S[1], d, e)
			PF = PF * PF_curr

		
	


	if (not(data["Supported_walls"] == [])):					# Supported walls PF computation
	
		for i in range (len(data["Supported_walls"])):
			

			if len(data["Supported_walls"][i]) == 2:
				d = data["Supported_walls"][i][0]
				e = data["Supported_walls"][i][1]
			elif len(data["Supported_walls"][i]) == 1:
				d = data["Supported_walls"][i][0]
				e = 0.0
			else:
				print("Something went wrong...")

			PF_curr = 1 - partCharacteristicEquation(w[2], c[2], S[2], d, e)
			PF = PF * PF_curr

		
	


	if (not(data["Unsupported_walls"] == [])):				# Unsupported walls PF computation
	
		for i in range (len(data["Unsupported_walls"])):

			if len(data["Unsupported_walls"][i]) == 2:
				d = data["Unsupported_walls"][i][0]
				e = data["Unsupported_walls"][i][1]
			elif len(data["Unsupported_walls"][i]) == 1:
				d = data["Unsupported_walls"][i][0]
				e = 0.0
			else:
				print("Something went wrong...")

			PF_curr = 1 - partCharacteristicEquation(w[3], c[3], S[3], d, e)
			PF = PF * PF_curr

		
	


	if (not(data["Embossed_details_Width"] == []) and not(data["Embossed_details_Height"] == [])):			# Embossed details PF computation
		
		for i in range(len(data["Embossed_details_Width"])):


			if len(data["Embossed_details_Width"][i]) == 2:
				d1 = data["Embossed_details_Width"][i][0]
				e = data["Embossed_details_Width"][i][1]
			elif len(data["Embossed_details_Width"][i]) == 1:
				d1 = data["Embossed_details_Width"][i][0]
				e = 0.0
			else:
				print("Something went wrong...")


			if len(data["Embossed_details_Height"][i]) == 2:
				d2 = data["Embossed_details_Height"][i][0]
				
			elif len(data["Embossed_details_Height"][i]) == 1:
				d2 = data["Embossed_details_Height"][i][0]
				
			else:
				print("Something went wrong...")
				print(d2)
				break
				
			PF_curr = 1 - partCharacteristicEquationEmEng(w[4], c[4], S[4], w[5], c[5], S[4], d1, d2, e)
			PF = PF * PF_curr

				
	if (not(data["Engraved_details_Width"] == []) and not(data["Engraved_details_Height"] == [])):					# Engraved details PF computation
		
		for i in range(len(data["Engraved_details_Width"])):
			if len(data["Engraved_details_Width"][i]) == 2:
				d1 = data["Engraved_details_Width"][i][0]
				e = data["Engraved_details_Width"][i][1]
			elif len(data["Engraved_details_Width"][i]) == 1:
				d1 = data["Engraved_details_Width"][i][0]
				e = 0.0
			else:
				print("Something went wrong...")

			if len(data["Engraved_details_Height"][i]) == 2:
				d2 = data["Engraved_details_Height"][i][0]
				
			elif len(data["Engraved_details_Height"][i]) == 1:
				d2 = data["Engraved_details_Height"][i][0]
				
			else:
				print("Something went wrong...")

			PF_curr = 1 - partCharacteristicEquationEmEng(w[6], c[6], S[5], w[7], c[7], S[5], d1, d2, e)
			PF = PF * PF_curr		



	if (not(data["Thin_Features"] == [])):					# Thin Features PF computation
		
		for i in range (len(data["Thin_Features"])):

			if len(data["Thin_Features"][i]) == 2:
				d = data["Thin_Features"][i][0]
				e = data["Thin_Features"][i][1]
			elif len(data["Thin_Features"][i]) == 1:
				d = data["Thin_Features"][i][0]
				e = 0.0
			else:
				print("Something went wrong...")

			PF_curr = 1 - partCharacteristicEquation(w[8], c[8], S[6], d, e)
			PF = PF * PF_curr
		
	


	return PF

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~	BASIC PRINTABILITY FUNCTION		~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ 

def computePrintability(data, technology, application):

	
	outputPG = globalPrintability(data, technology, application)
	print("Final PG :", outputPG)
	outputPF = partCharacteristicPrintability(data, technology, application)
	print("Final PF :",  outputPF)
	output = outputPG * outputPF * 100
	print("Final Score (%): ",output)
	
	if outputPG > 1:
		output = -1  #  Indicates Area ERROR
	
	return (output)

def computePFperChar(data, technology, application):
	outputPF = partCharacteristicPrintability(data, technology, application)
	output = outputPF * 100
	return (output)






######################## TEST #################################
'''

#study_case_6
data = {"Holes":	 				[[5.5, 0.093310], [6.5, 0.091686]], 
		"Pins": 					[[6.5, 0.095907], [7.5, 0.093293]], 
		"Supported_walls":			[[6.5, 0.096814], [7.5, 0.109800]],
		"Unsupported_walls":		[[9.5, 0.087855], [8.5, 0.085138]], 
		"Embossed_details_Width":	[[3.5, 0.096621], [4.5, 0.092030]], 
		"Embossed_details_Height":	[[3.5, 0.096621], [4.5, 0.092030]], 
		"Engraved_details_Width":	[[3.5, 0.093710], [4.5, 0.091417]], 
		"Engraved_details_Height":	[[3.5], [4.5]], 
		"Thin_Features": 			[[6.5, 0.084104], [7.5, 0.087484]], 
		"Area_STL":					[], 
		"Area_CAD":					[]
}

FDM = 0
Material_jetting = 1
Binder_jetting = 2

BIOMEDICAL = 0
MECHANICAL = 1
ARTISTIC = 2

computePrintability(data, FDM, BIOMEDICAL)
computePrintability(data, Material_jetting, BIOMEDICAL)
computePrintability(data, Binder_jetting, BIOMEDICAL)'''
