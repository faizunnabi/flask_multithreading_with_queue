from datetime import date

def validate_data(data):
    error_list=[]
    if data['bdate'] < date.today():   
        errors = {}
        errors['error']=701
        errors['desc']='Error in date'
        error_list.append(errors)
    if int(data['duration'])<1 or int(data['rooms'])<1 or int(data['quantity'])<1:
        errors = {}
        errors['error'] = 702
        errors['desc'] = 'Error in quantity'
        error_list.append(errors)
    return error_list


def format_request(data):
    js_data={"hotelAvailabilityRQ": {"checkInDate": str(date.isoformat(data['bdate'])),
    "duration": str(data['duration']),
    "hotelCodes": data['hotels'],
    "preferences": {"Country": "AE",
                    "Currency": "USD",
                    "Language": "en"},
    "rooms": [{"Adults": data['quantity'],
                "Children": []}],
    "source": {"Client": "10001",
                "EMailAddress": "test@test.com",
                "Password": "123456789"}}}
    
    return js_data

    
