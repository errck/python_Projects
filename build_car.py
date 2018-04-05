def build_car(make, model, **car_info):
	car = {}
	car['make']= make
	car['model'] = model
	for key, value in car_info.items():
		car[key] = value
	return car
    
new_car = build_car('Acura', 'RSX',
                             engine='K20Z1',
                             Country='Japan',
                             manufactured='USA')

for key,value in new_car.items():
	print(key + " " + value)
	
