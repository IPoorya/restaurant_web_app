from kavenegar import *


def send_otp_code(phone_number, code):
    try:
        api = KavenegarAPI(
            '6C4970344851423350316E6161664C67564B687A383834484D756269444B6258386C41327A314E644F38383D')
        params = {
            'sender': '',  # optional
            'receptor': phone_number,  # multiple mobile number, split by comma
            'message': f'your code: {code}',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)
