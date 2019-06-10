data = {
    "products": [
        {
            'name' : 'Cisco Meraki MR42 Cloud Managed ',
			'type' : 'Wireless access point',
			'description' : 'Data Link Protocol:IEEE 802.11ac Wave 2',
			'price' :  '800.99',
            'imageUrl' : '/shared/images/hardware/1.jpg'
        },
		
		{
            'name' : 'Ubiquiti Unifi AP-AC Pro',
			'type' : 'Wireless access point',
			'description' : 'Data Link Protocol:IEEE 802.11g',
			'price' :  '657.99',
            'imageUrl' : '/shared/images/hardware/2.jpg'
        },
		
		{
            'name' : 'Cradlepoint COR IBR600 ',
			'type' : 'Wireless router',
			'description' : 'Data Link Protocol:IEEE 802.11g',
			'price' : '649.99',
            'imageUrl' : '/shared/images/hardware/3.jpg'
        },
		
		{
            'name' : 'Microsoft Surface USB 3.0',
			'type' : 'Ethernet Adapter',
			'description' : 'Data Link Protocol:Gigabit Ethernet',
			'price' : '34.99',
            'imageUrl' : '/shared/images/hardware/4.jpg'
        },
    ],
	
    "images": [
      {"url": '/shared/images/corgi.jpg'},
      {"url": '/shared/images/cavalier.jpg'},
      {"url": '/shared/images/aussi.jpg'},
      {"url": '/shared/images/corgi.jpg'},
      {"url": '/shared/images/cavalier.jpg'},
      {"url": '/shared/images/aussi.jpg'},
    ],
	
    "sizes":[
      {"name": "small", "toString":"Small"},
      {"name": "medium", "toString":"Medium"},
      {"name": "big", "toString":"Big"},
    ],
	
    "cities":[
      {"id":"telAviv", "toString": "Tel Aviv xoxo"},
      {"id":"2", "toString":"Haifa"}
    ],
	
    "days": [0, 1, 2],
    "hours": [[1, 2, 3, 4], [2, 3, 4], [3, 4]]
}


def get_data(params):
    index = int(params.pop('_index', 0))
    length = int(params.pop('_length', 0))
    collection = params.pop('_collection')

    filtered_data = list(filter(lambda element: set(params.items()).issubset(set(element.items())),
                           data[collection]))

    return filtered_data[index:index + length] if length > 0 else filtered_data[index:]
