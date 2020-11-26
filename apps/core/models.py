from model_utils.models import SoftDeletableModel
from django.db import models

# Create your models here.


class BestPraticesModel(SoftDeletableModel):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class State(BestPraticesModel):
    uf = models.CharField(verbose_name="Estado", max_length=2)
    description = models.CharField(max_length=100, blank=True, null=True)
    cod_ibge = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Estado"

    def __str__(self):
        return self.uf


class City(BestPraticesModel):
    name = models.CharField(verbose_name="Cidade", max_length=100, blank=True, null=True, db_index=True)
    state = models.ForeignKey(State, max_length=2, blank=True, null=True, on_delete=models.DO_NOTHING)
    latitude = models.DecimalField(max_digits=14, decimal_places=12, blank=True, null=True)
    longitude = models.DecimalField(max_digits=14, decimal_places=12, blank=True, null=True)
    cod_ibge = models.IntegerField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "Cidade"

    def __str__(self):
        return self.name


class Neighborhood(BestPraticesModel):
    description = models.CharField(verbose_name="Bairro", max_length=100, blank=True, null=True)
    city = models.ForeignKey(City, blank=True, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "Bairro"

    def __str__(self):
        return self.description


class Place(BestPraticesModel):
    zip_code = models.CharField(verbose_name="CEP", max_length=10)
    description = models.CharField(max_length=200, blank=True, null=True)
    place_type = models.CharField(max_length=80, blank=True, null=True)
    latitude = models.DecimalField(max_digits=14, decimal_places=12, blank=True, null=True)
    longitude = models.DecimalField(max_digits=14, decimal_places=12, blank=True, null=True)
    city = models.ForeignKey(City, blank=True, null=True, on_delete=models.DO_NOTHING)
    neighborhood = models.ForeignKey(Neighborhood, blank=True, null=True, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "Localidade"

    def __str__(self):
        return self.zip_code

    def get_zipcode_formated(self):
        return self.zip_code.replace(".", "").replace("-", "")


class Address(BestPraticesModel):
    place = models.ForeignKey(Place, on_delete=models.DO_NOTHING, blank=True, null=True)
    street = models.CharField(verbose_name="Rua", max_length=300, blank=True, null=True)
    number = models.CharField(verbose_name="Número", max_length=20, null=True, blank=True)
    complement = models.CharField(verbose_name="Complemento", max_length=100, null=True, blank=True)
    reference_point = models.CharField(verbose_name="Ponto de referência", max_length=100, null=True, blank=True)
    latitude = models.DecimalField(max_digits=14, decimal_places=12, blank=True, null=True)
    longitude = models.DecimalField(max_digits=14, decimal_places=12, blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, blank=True, null=True)
    neighborhood = models.ForeignKey(Neighborhood, on_delete=models.DO_NOTHING, blank=True, null=True)
    state = models.ForeignKey(State, on_delete=models.DO_NOTHING, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Endereço"

    def __str__(self):
        return "{}, {}, {}, {} - {}".format(self.street, self.number, self.neighborhood, self.city, self.state)
