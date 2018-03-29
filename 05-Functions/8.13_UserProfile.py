def build_profile(first, last, **user_info):
    """Build a dictionary containing everything you know about a user"""
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, info in user_info.items():
        profile[key] = info
    return profile

user_profile = build_profile('Fio', 'Ambadar', location = 'Jakarta', university = 'Binus', major = 'CS')
print(user_profile)
