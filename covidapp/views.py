from django.shortcuts import render
import json

# # # print(response.text)
# import requests
# url = "https://covid-193.p.rapidapi.com/countries"
# headers = {
#     'x-rapidapi-host': "covid-193.p.rapidapi.com",
#     'x-rapidapi-key': "61640332c8mshc97389ee45bb7edp1e63f2jsnb2c6421100b5"
#     }
# response = requests.request("GET", url, headers=headers).json()

# print(response.text)

import requests

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "61640332c8mshc97389ee45bb7edp1e63f2jsnb2c6421100b5"
    }

response = requests.request("GET", url, headers=headers).json()



# Create your views here.
def helloworldview(request):
    # string="everyone"
    # mylistitems=['item1','item2','item3']
    # context={'mylistitems':mylistitems}
    # context={'response':response['response'][0]}
    # print(response['response'][0])
    noofresults=int(response['results'])
    mylist=[]
    for x in range(0,noofresults):
        mylist.append(response['response'][x]['country'])

    if request.method=="POST":
        selectedcountry=request.POST['selectedcountry']
        noofresults=int(response['results'])
        for x in range(0,noofresults):
            if selectedcountry==response['response'][x]['country']:
                new=response['response'][x]['cases']['new']
                active=response['response'][x]['cases']['active']
                critical=response['response'][x]['cases']['critical']
                recovered=response['response'][x]['cases']['recovered']
                total=response['response'][x]['cases']['total']
                deaths=int(total)-int(active)-int(recovered)
        context={'selectedcountry':selectedcountry,'mylist':mylist,'new':new,'active':active,'critical':critical,'recovered':recovered,'deaths':deaths,'total':total}
        return render(request, 'helloworld.html',context)

    
    # mylist=[]
    # for x in range(0,noofresults):
    #     mylist.append(response['response'][x]['country'])
    context={'mylist':mylist}
    return render(request, 'helloworld.html',context)