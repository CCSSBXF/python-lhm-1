def build_profile(first,last,**user_info):
    profile={}
    profile['first_name']=first
    profile['last_name']=last
    for key,value in user_info.items():
        profile[key]=value
    return profile

uses_profile=build_profile('a','b',lication='princeton',field='phusics')
print(uses_profile)