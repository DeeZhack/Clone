def loginauth(username, password):
     """
     * Confirms that the username exists and that the password is correct for that username
     * @param(str) username -- the username
     * @param(str) password -- the password
     * @return(bool) True -- if successful login
     * @return(bool) False -- if unsucessful logic (either username does not exist, or password is incorrect)
     """
    if username in users:
        if password == users[username]["password"]:
            print("Login successful")
            return True
    return False
