from django.db import models

# Users in our DataBase
class User(models.Model):
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=40)
    org_name = models.CharField(max_length=255)
    isAdmin = models.BooleanField(default=False)
    isActive = models.BooleanField(default=False)
    isPending = models.BooleanField(default=True)
    image_reference = models.CharField(max_length=40, default="")

    def __str__(self):
        return self.email

    #Get a specific users info by their ID
    def get_by_id(self, id):
        query = User.objects.filter(id=id)
        if query.count() == 1:
            return query[0]
        return None

    #Since we are not deleting users and have pending users we only want to gab ones that are Active
    def get_all_users(self):
        query = User.objects.filter(isActive=True)
        if query.count() > 0:
            return query
        return None

    #Return all pending users, will be useful for showing on admin page all accounts awaiting approval
    def get_all_pending(self):
        query = User.objects.filter(isPending=True)
        if query.count() > 0:
            return query
        return None

    #New user, defaults to not active and pending
    def createNewUser(self, tmpEmail, tmpPassword, tmpIsAdmin):
        u = User(email=tmpEmail, password=tmpPassword, isAdmin=tmpIsAdmin)
        u.save()

    #Approve a currently pending user by ID
    def approveNewUser(self, id):
        u = self.get_by_id(id)
        u.isPending = False
        u.isActive = True
        u.save()

    #Deny a currently pending user by ID, will only be inactive
    def denyNewUser(self, id):
        u = self.get_by_id(id)
        u.isPending = False
        u.isActive = False
        u.save()

    #Edit a user's email - likely to change with auth
    def editEmail(self, id, tmpEmail):
        u = self.get_by_id(id)
        u.email = tmpEmail
        u.save()

    #Edit a user's password - likely to change with auth
    def editPassword(self, id, tmpPassword):
        u = self.get_by_id(id)
        u.password = tmpPassword
        u.save()


class Category(models.Model):
    description = models.CharField(max_length=40)

    def __str__(self):
        return self.description


class Program(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20)
    content = models.CharField(max_length=250)
    address = models.CharField(max_length=40)
    website = models.CharField(max_length=40)
    isPending = models.BooleanField(default=True)
    editOf = models.IntegerField(default=None)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.title

    #Get a specific programs info by it's ID
    def get_by_id(self, id):
        query = Program.objects.filter(id=id)
        if query.count() == 1:
            return query[0]
        return None

    #Since we have pending programs we only want to gab ones that are not pending
    def get_all_programs(self):
        query = Program.objects.filter(isPending=False)
        if query.count() > 0:
            return query
        return None

    #Since we have programs that belong to a user, we may want to get all that user's programs
    def get_my_programs(self, id):
        query = Program.objects.filter(user_id=id)
        if query.count() > 0:
            return query
        return None

    #Return all pending programs, will be useful for showing on admin page all programs awaiting approval
    def get_all_pending(self):
        query = Program.objects.filter(isPending=True)
        if query.count() > 0:
            return query
        return None

    #New Program, defaults to pending
    def createNewProgram(self, tmpUser_id, tmpTitle, tmpContent, tmpAddress, tmpWebsite, tmpCategories):
        p = Program(user_id=tmpUser_id, title=tmpTitle, content=tmpContent, address=tmpAddress, website=tmpWebsite)
        for descr in tmpCategories:
            c = Category.objects.get(description=descr)
            p.categories.add(c)
        p.save()

    #Edit a program, creates a new program with an editOf value that corresponds to the original program
    def editProgram(self, currentId, tmpUser_id, tmpTitle, tmpContent, tmpAddress, tmpWebsite, tmpCategories):
        p = Program(user_id=tmpUser_id, title=tmpTitle, content=tmpContent, address=tmpAddress, website=tmpWebsite, editOf=currentId)
        for descr in tmpCategories:
            c = Category.objects.get(description=descr)
            p.categories.add(c)
        p.save()

    # Approve a currently pending new or edited program,
    # if edited and was aprroved the original program will be deleted
    def approveProgram(self, id):
        p = self.get_by_id(id)
        p.isPending = False
        if p.editOf != None:
            origProg = self.get_by_id(editOf)
            origProg.delete()
        p.save()

    #Deny a currently pending program by ID, will only be inactive
    def denyProgram(self, id):
        p = self.get_by_id(id)
        p.delete()

