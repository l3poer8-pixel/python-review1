class Contact:
    def __init__(self,name,phone_number,email):
        self.name = name
        self.email = email
        self.phone_number = phone_number

    def to_dict(self):
        return{
            "name":self.name,
            "email":self.email,
            "phone_number":self.phone_number
        }