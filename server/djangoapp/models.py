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
class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, 
        short_name, st, state, zip):
        self.address = address
        self.city = city
        self.full_name = full_name  # Full name of dealership
        self.id = id  # Dealership id
        self.lat = lat
        self.long = long
        self.short_name = short_name
        self.st = st  # State alpha code
        self.state = state  # Full state name
        self.zip = zip
        self.idx = 0

    def __str__(self):
        return self.full_name + ", " + self.state

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, dealership, id, name, purchase, review, car_make=None, car_model=None, car_year=None, purchase_date=None, sentiment="neutral"):
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year
        self.dealership = dealership
        self.id = id  # The id of the review
        self.name = name  # Name of the reviewer
        self.purchase = purchase  # Did the reviewer purchase the car? bool
        self.purchase_date = purchase_date
        self.review = review  # The actual review text
        self.sentiment = sentiment  # Watson NLU sentiment analysis of review

    def __str__(self):
        return "Reviewer: " + self.name + " Review: " + self.review