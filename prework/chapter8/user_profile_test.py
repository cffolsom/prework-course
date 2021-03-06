def build_profile(first, last, **user_info):
    """build a dictionary containing everything we know about a user."""
    profile = {}
    profile['first name'] = first
    profile['last name'] = last
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('connor', 'folsom',
                            location='shoreline',
                            field='programming',
                            disability='deafness')
print(user_profile)