from django.db import models
from django.contrib.auth.models import User

# Users in our DataBase
class userInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    org_name = models.CharField(max_length=255)
    isAdmin = models.BooleanField(default=False)
    isActive = models.BooleanField(default=False)
    isPending = models.BooleanField(default=True)
    contact_name = models.CharField(max_length=255, default="Name not Specified")
    contact_phone = models.CharField(max_length=255, default="Phone Number not Specified")
    contact_email = models.CharField(max_length=255, default="Email Address not Specified")
    image_reference = models.CharField(max_length=40, default="NOT SPECIFIED")
    last_login = models.CharField(max_length=100, default="Has Not Logged In")

    def __str__(self):
        return self.org_name

    #Get a specific users info by their ID
    def get_by_id(self, id):
        query = userInfo.objects.filter(id=id)
        if query.count() == 1:
            return query[0]
        return None

    #Since we are not deleting users and have pending users we only want to gab ones that are Active
    def get_all_users(self):
        query = userInfo.objects.filter(isActive=True)
        if query.count() > 0:
            return query
        return None

    #Return all pending users, will be useful for showing on admin page all accounts awaiting approval
    def get_all_pending(self):
        query = userInfo.objects.filter(isPending=True)
        if query.count() > 0:
            return query
        return None

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
    objects = None
    user_id = models.ForeignKey(userInfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, default="NOT SPECIFIED")
    content = models.TextField(default="NOT SPECIFIED")
    address = models.CharField(max_length=255, default="NOT SPECIFIED")
    lat = models.CharField(max_length=255, default="43.154535")
    lng = models.CharField(max_length=255, default="-77.590575")
    website = models.CharField(max_length=255, default="NOT SPECIFIED")
    #Refactored fees to a float so they could be filtered by a range
    fees = models.FloatField(default=0)
    isPending = models.BooleanField(default=True)
    contact_name = models.CharField(max_length=255, default="NOT SPECIFIED")
    contact_email = models.CharField(max_length=255, default="NOT SPECIFIED")
    contact_phone = models.CharField(max_length=255, default="NOT SPECIFIED")
    editOf = models.IntegerField(default=0)
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

class resetPWURLs(models.Model):
    user_ID = models.TextField(default="DEFAULT PROVIDER")
    reset_string = models.CharField(max_length=15, default="A DEFAULTSTRING")