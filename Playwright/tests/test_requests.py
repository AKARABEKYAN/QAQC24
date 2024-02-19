import requests 
from config import *
# from enums.global_enums import Error 

# def test_get_single_user():
#     req = requests.get (SINGLE_USER_URL, timeout=1.0)
#     if req.status_code == 201:
#         r = req.json()
#         assert (r['data'] ['first_name']) == 'Janet', "First name is incorrect"
#         assert (r['data'] ['last_name']) == 'Weaver'
#         assert (r['data'] ['id']) == 2, 'ID is incorrect' "Last name is incorrect"
#         assert req.status_code == 200, "Status code is incorrect"
#     else:
#         print (f'An error occured with status code')

# def test_get_list_users():
#     req = requests.get(LIST_USER_URL, timeout= 0.5)
#     r = req.json()
#     assert (r['data'][0] ['id'])== 7, "ID is incorrec"
#     assert req.status_code == 200, "Status code is incorrect"

# def test_get_not_found_user():
#     req = requests.get (NOT_FOUND_USER, timeout= 0.5)
#     assert req.status_code == 404, "Status code is incorrect"

# def test_create_user():
#     req = requests.post (CREATE_USER_URL, data= CREATE_USER_DATA)
#     print (req.json())
#     r = req.json()
#     assert (r['name']) == 'Slava', 'Name is incorrect'
#     assert req.status_code == 201

def list_resource():
    req =  requests.get('https://reqres.in/api/unknown')
    r = req.json()
    assert (r['data'] [2] ['id']) == 3, 'id is incorrect'
    assert (r['data'][2]['name']) == 'true red', 'name is incorrect'
    assert (r['data'] [2] ['year'])== 2002, 'year is incorrect'
    assert (r['data'] [2] ['color'])== '#BF1932', 'color is incorrect'
    assert (r['data'] [2] ['pantone_value']) == '19-1664', 'pantone value is incorrect'
    assert req.status_code == 200, 'status code is incorrect'
    return req

def single_resource_not_found():
    req = requests.get ('https://reqres.in/api/unknown/23')
    r = req.json()
    assert req.status_code == 404, "status code is incorrect"
    print (req.json())
    return req

def register_successful():
    params_register_successful = {
        'email': 'eve.holt@reqres.in',
        'password': 'pistol'}
    req = requests.post('https://reqres.in/api/register', data=params_register_successful)
    r = req.json()
    assert (r ['id'])== 4, 'id is incorrect'
    assert (r ['token'])=='QpwL5tke4Pnpja7X4','token is incorrect'
    assert req.status_code == 200, 'status code is incorrect'
    return req

def get_not_found_user():
    req = requests.get ('https://reqres.in/api/users/23')
    r = req.json()
    assert req.status_code == 404, "status code is incorrect"
    assert not r == None
    return req 


# get_list_users()
# get_list_users()
# get_not_found_user()
# create_user ()
# print(list_resource())
print(single_resource_not_found())
print (register_successful())
print (get_not_found_user())