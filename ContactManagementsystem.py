class Contact:
    def __init__(self, name, mobile, email):
        self.name=name
        self.mobile=mobile
        self.email=email
    def display(self):
        print("Name:{}\n Mobile:{}\n Email:{}\n".format(self.name, self.mobile, self.email))
class ContactManager:
    def __init__(self):
        self.contacts=[]
    def add_contact(self):
        name=input("Enter Name: ")
        mobile=int(input("Enter Mobile: "))
        email=input("Enter Email: ")
        contact=Contact(name,mobile,email)
        self.contacts.append(contact)
        print("Contact Added Successfully!\n")
    def display_contacts(self):
        if not self.contacts:
            print("No Contacts Found\n")
            return
        print("\nContact List:")
        i=1
        for contact in self.contacts:
            print(str(i)+".",end="")
            contact.display()
            i+=1
        print()
    def update_contact(self):
        self.display_contacts()
        if not self.contacts:
            return
        index=int(input("Enter contact number to update: "))-1
        if index>=0 and index<len(self.contacts):
            print("Enter new details:")
            new_mobile=input("New Mobile: ")
            new_email=input("New Email: ")
            self.contacts[index].mobile=new_mobile
            self.contacts[index].email=new_email
            print("Contact Updated Successfully!\n")
        else:
            print("Invalid Contact Number\n")
    def delete_contact(self):
        self.display_contacts()
        if not self.contacts:
            return
        index=int(input("Enter contact number to delete: "))-1
        if index>=0 and index<len(self.contacts):
            self.contacts.pop(index)
            print("Contact Deleted Successfully!\n")
        else:
            print("Invalid Contact Number\n")
def main():
    manager=ContactManager()
    while True:
        print("===== Contact Management System =====")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Display Contacts")
        print("4. Delete Contact")
        print("5. Exit")
        choice=input("Enter your choice:")
        if choice=='1':
            manager.add_contact()
        elif choice=='2':
            manager.update_contact()
        elif choice=='3':
            manager.display_contacts()
        elif choice=='4':
            manager.delete_contact()
        elif choice=='5':
            print("Exiting...")
            break
        else:
            print("Invalid Choice\n")
if __name__=="__main__":
    main()
