from django.db import models

class TblSettings(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)
    # Field name made lowercase.
    value = models.CharField(
        db_column='Value', max_length=50, blank=True, null=True)
    # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)
    # Field name made lowercase.
    created = models.DateTimeField(db_column='Created', blank=True, null=True)
    # Field name made lowercase.
    modified = models.DateTimeField(
        db_column='Modified', blank=True, null=True)

    class Meta:
        db_table = 'Tbl_Settings'


class TblCountry(models.Model):
    # Field name made lowercase.
    countryid = models.AutoField(db_column='CountryID', primary_key=True)
    # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)

    class Meta:
        db_table = 'tbl_Country'


class TblCurency(models.Model):
    # Field name made lowercase.
    curuncyid = models.AutoField(db_column='CuruncyID', primary_key=True)
    # Field name made lowercase.
    curuncyname = models.TextField(
        db_column='CuruncyName', blank=True, null=True)

    class Meta:
        db_table = 'tbl_Curency'


class TblDepartment(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    departmentname = models.TextField(
        db_column='DepartmentName', blank=True, null=True)
    # Field name made lowercase.
    status = models.BooleanField(db_column='Status', blank=True, null=True)

    class Meta:
        db_table = 'tbl_Department'


class TblEmployeetechnologies(models.Model):
    # Field name made lowercase.
    etid = models.AutoField(db_column='ETID', primary_key=True)
    # Field name made lowercase.
    empid = models.IntegerField(db_column='EmpID', blank=True, null=True)
    # Field name made lowercase.
    techid = models.IntegerField(db_column='TechID', blank=True, null=True)

    class Meta:
        db_table = 'tbl_EmployeeTechnologies'


class TblEmployees(models.Model):
    # Field name made lowercase.
    empid = models.AutoField(db_column='EmpID', primary_key=True)
    # Field name made lowercase.
    empname = models.TextField(db_column='EmpName', blank=True, null=True)
    # Field name made lowercase.
    roleid = models.IntegerField(db_column='RoleID', blank=True, null=True)
    # Field name made lowercase.
    loginid = models.TextField(db_column='LoginID', blank=True, null=True)
    # Field name made lowercase.
    password = models.TextField(db_column='Password', blank=True, null=True)
    # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)
    # Field name made lowercase.
    empcode = models.TextField(db_column='EmpCode', blank=True, null=True)

    class Meta:
        db_table = 'tbl_Employees'




class TblFlag(models.Model):
    # Field name made lowercase.
    flagid = models.AutoField(db_column='FlagID', primary_key=True)
    # Field name made lowercase.
    flagimagepath = models.TextField(
        db_column='FlagImagePath', blank=True, null=True)

    class Meta:
        db_table = 'tbl_Flag'


class TblHolidays(models.Model):
    # Field name made lowercase.
    id = models.BigAutoField(db_column='Id', primary_key=True)
    # Field name made lowercase.
    holidaydate = models.DateTimeField(
        db_column='HolidayDate', blank=True, null=True)
    # Field name made lowercase.
    occasionname = models.CharField(
        db_column='OccasionName', max_length=200, blank=True, null=True)
    # Field name made lowercase.
    isactive = models.BooleanField(db_column='isActive', blank=True, null=True)
    # Field name made lowercase.
    datecreated = models.DateTimeField(
        db_column='DateCreated', blank=True, null=True)
    # Field name made lowercase.
    datemodified = models.DateTimeField(
        db_column='DateModified', blank=True, null=True)

    class Meta:
        db_table = 'tbl_Holidays'


class TblLockedresource(models.Model):
    # Field name made lowercase.
    lid = models.BigAutoField(db_column='LID', primary_key=True)
    # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)
    # Field name made lowercase.
    lockeddate = models.DateTimeField(
        db_column='LockedDate', blank=True, null=True)
    # Field name made lowercase.
    lockedby = models.IntegerField(db_column='LockedBy', blank=True, null=True)
    # Field name made lowercase.
    unlockeddate = models.DateTimeField(
        db_column='UnlockedDate', blank=True, null=True)
    # Field name made lowercase.
    unlockedby = models.IntegerField(
        db_column='UnlockedBy', blank=True, null=True)

    class Meta:
        db_table = 'tbl_LockedResource'


class TblTechnologies(models.Model):
    # Field name made lowercase.
    techid = models.AutoField(db_column='TechID', primary_key=True)
    # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)
    # Field name made lowercase.
    description = models.TextField(
        db_column='Description', blank=True, null=True)
    # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)

    class Meta:
        db_table = 'tbl_Technologies'


class TblUser(models.Model):
    # Field name made lowercase.
    userid = models.AutoField(db_column='UserID', primary_key=True)
    # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName', blank=True, null=True)
    # Field name made lowercase.
    lastname = models.TextField(db_column='LastName', blank=True, null=True)
    # Field name made lowercase.
    accountemail = models.TextField(
        db_column='AccountEmail', blank=True, null=True)
    # Field name made lowercase.
    accountphone = models.TextField(
        db_column='AccountPhone', blank=True, null=True)
    # Field name made lowercase.
    usertype = models.IntegerField(db_column='UserType', blank=True, null=True)
    # Field name made lowercase.
    password = models.TextField(db_column='Password', blank=True, null=True)
    # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)
    # Field name made lowercase.
    deleted = models.BooleanField(db_column='Deleted', blank=True, null=True)
    # Field name made lowercase.
    usercode = models.IntegerField(db_column='UserCode', blank=True, null=True)
    # Field name made lowercase.
    status = models.IntegerField(db_column='Status', blank=True, null=True)
    # Field name made lowercase.
    deptid = models.IntegerField(db_column='DeptID', blank=True, null=True)
    # Field name made lowercase.
    managerid = models.IntegerField(
        db_column='ManagerID', blank=True, null=True)
    # Field name made lowercase.
    exempttimesheet = models.BooleanField(
        db_column='ExemptTimesheet', blank=True, null=True)
    # Field name made lowercase.
    createddate = models.DateTimeField(
        db_column='CreatedDate', blank=True, null=True)
    # Field name made lowercase.
    uan = models.BigIntegerField(db_column='UAN', blank=True, null=True)
    # Field name made lowercase.
    pan = models.TextField(db_column='PAN', blank=True, null=True)
    # Field name made lowercase.
    lastlogin = models.DateTimeField(
        db_column='LastLogin', blank=True, null=True)
    # Field name made lowercase.
    imageurl = models.TextField(db_column='ImageUrl', blank=True, null=True)
    # Field name made lowercase.
    timesheetcounter = models.IntegerField(db_column='TimesheetCounter')

    class Meta:
        db_table = 'tbl_User'
        verbose_name = 'Octal Employee'
        verbose_name_plural = 'Octal Employees'

    def __str__(self):
        return f'{self.firstname}[{self.usercode}]'

class TblUserlog(models.Model):
    # Field name made lowercase.
    id = models.AutoField(db_column='ID', primary_key=True)
    # Field name made lowercase.
    userid = models.IntegerField(db_column='UserID', blank=True, null=True)
    # Field name made lowercase.
    logindate = models.DateField(db_column='LoginDate', blank=True, null=True)
    # Field name made lowercase.
    logintime = models.DateTimeField(
        db_column='LoginTime', blank=True, null=True)
    # Field name made lowercase.
    logouttime = models.DateTimeField(
        db_column='LogoutTime', blank=True, null=True)
    # Field name made lowercase.
    workingminutes = models.IntegerField(
        db_column='WorkingMinutes', blank=True, null=True)
    # Field name made lowercase.
    isactive = models.BooleanField(db_column='IsActive', blank=True, null=True)
    # Field name made lowercase.
    createddate = models.DateTimeField(
        db_column='CreatedDate', blank=True, null=True)
    # Field name made lowercase.
    modifieddate = models.DateTimeField(
        db_column='ModifiedDate', blank=True, null=True)

    class Meta:
        db_table = 'tbl_UserLog'


class TblUsertype(models.Model):
    # Field name made lowercase.
    usertypeid = models.AutoField(db_column='UserTypeID', primary_key=True)
    # Field name made lowercase.
    usertype = models.TextField(db_column='UserType', blank=True, null=True)

    class Meta:
        db_table = 'tbl_UserType'
