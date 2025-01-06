def process_status(d):
    #Prints the status message based on the 'status' value in the dictionary.
    status_messages = {
        'active':"Active",
        'inActive':'Inactive'
    }
    print(status_messages.get(d.get('status'),'unknown'))  #get the status msg or unknown if status is missing 