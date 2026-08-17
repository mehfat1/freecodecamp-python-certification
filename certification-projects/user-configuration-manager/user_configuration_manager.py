test_settings = {
    'theme': 'dark',
    'language': 'english',
    'notifications': 'enabled'
}

def add_setting(dictionary, key_value):
    key, value = key_value
    key = key.lower()
    value = value.lower()
        
    if key in dictionary:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    
    else:
        dictionary[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(dictionary, key_value):
    key, value = key_value
    key = key.lower()
    value = value.lower()
    
    if key in dictionary:
        dictionary[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"

    else: 
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(dictionary, key):
    key = key.lower()
    if key in dictionary:
        del dictionary[key]
        return f"Setting '{key}' deleted successfully!"

    else:
        return 'Setting not found!'

def view_settings(dictionary):
    
    if dictionary:

        settings = 'Current User Settings:\n'
        for key, value in dictionary.items():
            settings += f'{key.capitalize()}: {value}\n'

        return settings
    
    else:
        return 'No settings available.'

print(view_settings(test_settings)) 
