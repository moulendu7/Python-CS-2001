while True:
    pwd = input("Enter password: ")
    errors = []
    if len(pwd) < 8:
        errors.append("Minimum 8 characters required.")
    if not any(c.isupper() for c in pwd):
        errors.append("At least one uppercase letter required.")
    if not any(c.islower() for c in pwd):
        errors.append("At least one lowercase letter required.")
    if not any(c.isdigit() for c in pwd):
        errors.append("At least one number required.")
    if not any(not c.isalnum() for c in pwd):
        errors.append("At least one special character required.")
    if len(errors) == 0:
        print("Password accepted.")
        break
    else:
        print("Invalid password:")
        for e in errors:
            print("-", e)