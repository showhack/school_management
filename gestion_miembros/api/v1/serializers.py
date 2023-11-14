from datetime import datetime
import re
from rest_framework import serializers

from gestion_miembros.models import GrupoEtario, Pais, Provincia, Municipio, Direccion, Persona, Atleta, Entrenador, \
    RelacionEntrenadorGrupoEtario


class GrupoEtarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = GrupoEtario
        fields = '__all__'


class PaisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pais
        fields = '__all__'


class ProvinciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Provincia
        fields = '__all__'


class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'


class DireccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Direccion
        fields = '__all__'


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'


# --------------------Validations of CI--------------------------------


    def validate_ci(self, value):
        """
        Check that the DNI has 11 digits and the first 6 correspond to a valid date.
        """
        if len(value) != 11 or not value.isdigit():
            raise serializers.ValidationError(
                "El DNI debe tener 11 dígitos y sólo contener números")

        # Convertir los primeros 6 dígitos del DNI a una fecha
        try:
            datetime.strptime(value[:6], "%y%m%d").date()
        except ValueError:
            raise serializers.ValidationError(
                "Los primeros 6 dígitos del DNI deben ser una fecha válida (AAMMDD)")

        return value

    def get_edad(self, obj):
        """
        Calculate the age based on the DNI.
        """
        birth_date = datetime.strptime(obj.dni[:6], "%y%m%d").date()
        today = datetime.today().date()
        return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

    def create(self, validated_data):
        """
        Create a Persona instance.
        """
        # Remove 'edad' from validated_data as it's calculated automatically
        validated_data.pop('edad', None)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        """
        Update a Persona instance.
        """
        # Remove 'edad' from validated_data as it's calculated automatically
        validated_data.pop('edad', None)
        return super().update(instance, validated_data)


# ----------------------Validations of name---------------------------------------------------


    def validate_nombre(self, value):
        """
        Check that the full name is well-formed.
        """
        # Verificar que cada palabra comience con una letra mayúscula
        if not all(word[0].isupper() for word in value.split()):
            raise serializers.ValidationError(
                "Cada palabra en el nombre completo debe comenzar con una letra mayúscula")

        # Verificar que el nombre completo sólo contenga letras y espacios
        if not re.match(r'^[A-Za-z\s]*$', value):
            raise serializers.ValidationError(
                "El nombre completo sólo puede contener letras y espacios")

        return value


class AtletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Atleta
        fields = '__all__'


class EntrenadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entrenador
        fields = '__all__'


class RelacionEntrenadorGrupoEtarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = RelacionEntrenadorGrupoEtario
        fields = '__all__'
