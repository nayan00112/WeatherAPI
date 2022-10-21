from django.shortcuts import render
import requests 
# Create your views here.

def Home(request):
    if request.method == 'POST':
        address = request.POST['cname']
        params = {
            'access_key': 'YOUR_API_KEY',
            'query': address,
        }
        # https://weatherstack.com/
        try:
            api_result = requests.get(f'http://api.weatherstack.com/current', params)
            api_response = api_result.json()
            try:
                location = api_response['location']
                current = api_response['current']
                # print(api_response)
                objects = {
                    # 'requestAPI' : requestAPI,
                    'location': location,
                    'current': current
                }
            except:
                success = api_response['success']
                error = api_response['error']
                objects = {
                    'success': success,
                    'error' : error,
                }
        except:
            objects = {
                    'success': "Network Connection Probblem."
                }
    
        return render(request, 'Home/index.html', objects)
    else:
        return render(request, 'Home/index.html', {'is_data_false' : 'false'})

