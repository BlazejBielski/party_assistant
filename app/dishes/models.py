from utilities.dishcore_model import DishCoreModel
from utilities.dishmark_model import DishMarkModel
from utilities.timestamp_model import TimeStampModel


class Soup(TimeStampModel, DishMarkModel, DishCoreModel):
    class Meta:
        verbose_name = "Soup"
        verbose_name_plural = "Soups"


class MainDish(TimeStampModel, DishMarkModel, DishCoreModel):
    class Meta:
        verbose_name = "Main dish"
        verbose_name_plural = "Main dishes"


class Appetizer(TimeStampModel, DishMarkModel, DishCoreModel):
    class Meta:
        verbose_name = "Appetizer"
        verbose_name_plural = "Appetizers"


class SideDish(TimeStampModel, DishMarkModel, DishCoreModel):
    class Meta:
        verbose_name = "Side dish"
        verbose_name_plural = "Side dishes"
