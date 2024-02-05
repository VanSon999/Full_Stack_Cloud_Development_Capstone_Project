from django.db import models
from django.utils.timezone import now


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=30, default='Porsche')
    description = models.CharField(null=True, max_length=500)

    def __str__(self):
        return "Name: " + self.name + ", Description: " + self.description

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, null=False, on_delete=models.CASCADE)
    dealer_id = models.IntegerField(null=False)
    name = models.CharField(null=False, max_length=30, default='Porsche')
    SEDAN = "Sedan"
    SUV = "SUV"
    WAGON = "Wagon"
    SPORT = "Sport"
    OTHER = "Other"
    CAR_CHOICES = [
        (SEDAN, "Sedan"), (SUV, "SUV"), (WAGON, "Station wagon"), 
        (SPORT, "Sports Car"), (OTHER, 'Other')
    ]
    type = models.CharField(null=False, max_length=20, choices=CAR_CHOICES, default=SUV)
    year = models.DateField(null=True)

    def __str__(self):
        return "Name: " + self.name + ", Type: " + self.type + \
        ", Year: " + self.year.strftime("%m/%d/%Y") + ", Car Make Name: " + self.car_make.name + \
        ", Dealer Id: " + str(self.dealer_id)

# <HINT> Create a plain Python class `CarDealer` to hold dealer data


# <HINT> Create a plain Python class `DealerReview` to hold review data
