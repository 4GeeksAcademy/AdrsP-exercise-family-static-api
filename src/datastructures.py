
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        # example list of members
        self._members = [
            {
            "age": 33,
            "first_name": "John",
            "id": 1,
            "lastname": last_name,
            "lucky_numbers": [7, 13, 22]
            },
            {
            "age": 35,
            "first_name": "Jane",
            "id": 2,
            "lastname": last_name,
            "lucky_numbers": [10, 14, 3]
            },
            {
            "age": 5,
            "first_name": "Jimmy",
            "id": 3,
            "lastname": last_name,
            "lucky_numbers": [1]
            }
        ]

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)

    def add_member(self, member):
        # fill this method and update the return
        # me da la impresion de lo que puedo hacer aca es recibir el objeto con la info del miembro y pues apend a la lista no?
        # member['lastname'] = self.last_name HEY CUIDADO ACA
        self._members.append(member)
        

    def delete_member(self, id):
        # fill this method and update the return
        # supongo que va a ser algo parecido al add member pero bueno ya va
        for member in self._members:
            if member['id'] == id:
                self._members.remove(member) 
                return True

    def get_member(self, id):
        # fill this method and update the return
        for member in self._members:
            if member['id'] == id:
                return member

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        print(self._members)
        return self._members
