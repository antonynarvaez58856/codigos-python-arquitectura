vs = 20  # voltios
rs = 75  # ohmios
ro = 100 # ohmios
k = 0.5  # adimencional
done = 1 # valor centinela

while done:
	vm = float(input (" ingrese el voltaje mostrado en el multimetro: "))
	
	if vm >= 12.0 and vm <= 18.0:   # si vm esta entre 12 y 18 entonces :
		t = (rs/k) * ( vm/(vs-vm)) - (ro/k)   # formula de la temperatura de la camara
		print( " la temperatura de la camarade gas es: ",t)
		done = 0 # desactivar centinela
	else:
		print("voltaje incorrecto. porfavor ingrese el voltaje nuevamente")
