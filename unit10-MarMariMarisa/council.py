class Administrator:
    __slots__ = ["name","region","languages","departments"]
    def __init__(self,name,region,languages,departments):
        self.name = name
        self.region = region
        self.languages = languages
        self.departments = departments

class Council:
    __slots__ = ["members","chief"]
    def __init__(self,members,chief):
        self.chief = chief
        self.members = members

def print_admin_bio(council,administrator):
    if administrator in council.members:
        print("Found Adminstrator Biography:")
        print(administrator.name)
        print("Region:")
        print("\t",administrator.region)
        print("Departments:")
        for department in administrator.departments:
            print("\t",department)
        print("Languages:")
        for language in administrator.languages:
            print("\t",language)
        
    else:
        print("Adminstrator not found")

def print_chief_admin_bio(council):
    for member in council.members:
        if member.name == council.chief.name:
            print("Chief Administrator Biography")
            print(council.chief.name)
            print("Departments:")
            for department in council.chief.departments:
                print("\t",department)
            print("Languages:")
            for language in council.chief.languages:
                print("\t",language)
            break

def print_council_members(council):
    print("Council:")
    for member in council.members:
        if member == council.chief:
            print("\t","[Chief]",member.name)
        else:
            print("\t",member.name)
def print_council_with_biographies(council):
    print("Council with Biographies:")
    for member in council.members:
        if member == council.chief:
            print("[Chief]", end = " ")
            print_admin_bio(council,member)
        else:
            print_admin_bio(council,member)
        print("")
def main():
    admin_1 = Administrator("Boe Jiren","USA",["English","Spanish"],["Executive","Federal"])
    admin_2 = Administrator("Aacinda Jrdern","NZD",["English","Maori"],["Minister"])
    admin_3 = Administrator("Tusin Jrudeau","CA",["English","French"],["Executive"])
    admin_4 = Administrator("Klf Uristersson","SE",["Swedish"],["Minister"])
    council = Council([admin_1,admin_2,admin_3,admin_4],admin_2)

    print_admin_bio(council,admin_1)
    print_chief_admin_bio(council)
    print_council_members(council)
    print_council_with_biographies(council)

if __name__ == "__main__":
    main()