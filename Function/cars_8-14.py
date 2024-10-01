def cars_info(manfact, model, **info):
    """Show some cars information"""
    profile = {}
    profile['manufacturer'] = manfact
    profile['model'] = model
    for k,v in info.items():
        profile[k] = v
    return profile  

car = cars_info('subaru', 'outback', 
                color='black', tow_packages=True) 
print(car)

from pizza_arbitary import make_pizza

make_pizza(16, 'cheese')