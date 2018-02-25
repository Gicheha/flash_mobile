#Abstract class to validate user input

from abc import ABC, abstractmethod
import re

class sanitizer(ABC):

    @abstractmethod
    def sanitise_number(self, number):
        try:
            sanitized = int(number)
        except ValueError:
            #TODO:JSON RESPONSE
            print("Invalid Employee Number!")

    @abstractmethod
    def sanitise_tax_pin(self, tax_pin):
        try:
            matched = re.match("/^[A-Z]+[0-9]+\[A-Z]/",tax_pin)
        except ValueError:
            # TODO:JSON RESPONSE
            print("Invalid Tax Pin Number!")

    @abstractmethod
    def sanitise_id_number(self, id_number):
        try:
            sanitized = int(id_number)
        except ValueError:
            #TODO:JSON RESPONSE
            print("invalid id_number!")

    @abstractmethod
    def sanitise_phone_number(self, phone_number):
        try:
            matched = re.match("/^[+0-9]{10,15}$/",phone_number)
        except:
            #TODO:JSON RESPONSE
            print("invalid phone number")

    @abstractmethod
    def sanitize_email(self, email):
        try:
            matched = re.match("/^[a-zA-Z0-9_\-\.]+@[a-zA-Z0-9\-]+\.[a-zA-Z0-9\-\.]+$/", email)
        except:
            #TODO:JSON RESPONSE
            print("Invalid email Entry")