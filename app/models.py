from django.db import models

# Create your models here.
class c_language(models.Model):
    username = models.CharField(max_length=100)
    basics = models.PositiveIntegerField(default=0, verbose_name="basics")
    printf_scanf = models.PositiveIntegerField(default=0, verbose_name="printf_scanf")
    variables = models.PositiveIntegerField(default=0, verbose_name="variables")
    datatypes = models.PositiveIntegerField(default=0, verbose_name="datatypes")
    typeConversion = models.PositiveIntegerField(default=0, verbose_name="typeConversion")
    operators = models.PositiveIntegerField(default=0, verbose_name="operators")
    conditional_statements = models.PositiveIntegerField(default=0, verbose_name="conditional_statements")
    loops = models.PositiveIntegerField(default=0, verbose_name="loops")
    break_continue = models.PositiveIntegerField(default=0, verbose_name="break_continue")
    strings = models.PositiveIntegerField(default=0, verbose_name="strings")
    arrays = models.PositiveIntegerField(default=0, verbose_name="arrays")
    pointers = models.PositiveIntegerField(default=0, verbose_name="pointers")
    functions = models.PositiveIntegerField(default=0, verbose_name="functions")
    files = models.PositiveIntegerField(default=0, verbose_name="files")
    structures = models.PositiveIntegerField(default=0, verbose_name="structures")


    def __str__(self):
        return self.username
    
class java_language(models.Model):
    username = models.CharField(max_length=100)
    basics = models.PositiveIntegerField(default=0, verbose_name="basics")
    print_scanner = models.PositiveIntegerField(default=0, verbose_name="print_scanner")
    variables = models.PositiveIntegerField(default=0, verbose_name="variables")
    datatypes = models.PositiveIntegerField(default=0, verbose_name="datatypes")
    typeConversion = models.PositiveIntegerField(default=0, verbose_name="typeConversion")
    conditional_statements = models.PositiveIntegerField(default=0, verbose_name="conditional_statements")
    loops = models.PositiveIntegerField(default=0, verbose_name="loops")
    break_continue = models.PositiveIntegerField(default=0, verbose_name="break_continue")
    lists = models.PositiveIntegerField(default=0, verbose_name="lists")
    dictionary = models.PositiveIntegerField(default=0, verbose_name="dictionary")
    pointers = models.PositiveIntegerField(default=0, verbose_name="pointers")
    files = models.PositiveIntegerField(default=0, verbose_name="files")
    classes_objects = models.PositiveIntegerField(default=0, verbose_name="classes_objects")
    ModulesAndPackages = models.PositiveIntegerField(default=0, verbose_name="Modules and Packages")


    def __str__(self):
        return self.username
    
class python_language(models.Model):
    username = models.CharField(max_length=100)
    basics = models.PositiveIntegerField(default=0, verbose_name="basics")
    print_input = models.PositiveIntegerField(default=0, verbose_name="print_input")
    variables = models.PositiveIntegerField(default=0, verbose_name="variables")
    datatypes = models.PositiveIntegerField(default=0, verbose_name="datatypes")
    typeConversion = models.PositiveIntegerField(default=0, verbose_name="typeConversion")
    conditional_statements = models.PositiveIntegerField(default=0, verbose_name="conditional_statements")
    loops = models.PositiveIntegerField(default=0, verbose_name="loops")
    break_continue = models.PositiveIntegerField(default=0, verbose_name="break_continue")
    lists = models.PositiveIntegerField(default=0, verbose_name="lists")
    dictionary = models.PositiveIntegerField(default=0, verbose_name="dictionary")
    pointers = models.PositiveIntegerField(default=0, verbose_name="pointers")
    files = models.PositiveIntegerField(default=0, verbose_name="files")
    classes_objects = models.PositiveIntegerField(default=0, verbose_name="classes_objects")
    ModulesAndPackages = models.PositiveIntegerField(default=0, verbose_name="Modules and Packages")


    def __str__(self):
        return self.username
    
    