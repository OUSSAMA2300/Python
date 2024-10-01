def build_profile(first, last, **user_info):
    """Build a dicionary contaning everything about the user"""
    profile = {} 
    profile['first name'] = first
    profile['last name'] = last
    for k, v in user_info.items():
        profile[k] = v
    return profile

user_profile = build_profile('albert', 'einstein',
                            location='princeton',
                            field='physics')

print(user_profile)

# 8-13

user_profile = build_profile('alaa', 'waleed',
                             location='alex',
                             field='mechanic',
                             birthdate='8/9/1978')

print(user_profile)