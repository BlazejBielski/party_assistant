from utilities.dishcore_model import DishCoreModel
from utilities.dishmark_model import DishMarkModel
from utilities.timestamp_model import TimeStampModel


class Soup(TimeStampModel, DishMarkModel, DishCoreModel):

    class Meta:
        verbose_name = "Soup"
        verbose_name_plural = "Soups"


class MainDish(TimeStampModel, DishMarkModel, DishCoreModel):

    class Meta:
        verbose_name = 'Main dish'
        verbose_name_plural = 'Main dishes'


class Appetizer(TimeStampModel, DishMarkModel, DishCoreModel):

    class Meta:
        verbose_name = 'Appetizer'
        verbose_name_plural = 'Appetizers'


class SideDishes(TimeStampModel, DishMarkModel, DishCoreModel):

    class Meta:
        verbose_name = 'Side dish'
        verbose_name_plural = 'Side dishes'


# class Picture(TimeStampModel):
#     soup = models.ForeignKey('Soup', on_delete=models.CASCADE, related_name='soup_image')
#     main_dish = models.ForeignKey('MainDish', on_delete=models.CASCADE, related_name='main_dish_image')
#     appetizer = models.ForeignKey('Appetizer', on_delete=models.CASCADE, related_name='appetizer_image')
#     side_dish = models.ForeignKey('SideDishes', on_delete=models.CASCADE, related_name='side_dish_image')
#     image = models.FileField(upload_to='images/', validators=[validate_file_type])
