from rest_framework import serializers  # type: ignore
from restapp4.models import employee


class employee_serializer(serializers.Serializer):
    name = serializers.CharField(max_length=20)
    email = serializers.EmailField()
    salary = serializers.IntegerField()
    age = serializers.IntegerField()

    def create(self, validated_data):
        return employee.objects.create(**validated_data)

    def update(self, instance, validate_data):
        instance.name = validate_data.get("name", instance.name)
        instance.email = validate_data.get("email", instance.email)
        instance.salary = validate_data.get("salary", instance.salary)
        instance.age = validate_data.get("age", instance.age)
        instance.save()
        return instance

    # fiels level validations
    def validate_age(self, value):
        if value > 100:
            raise serializers.ValidationError("Age should not eceed 100!")
        if value < 18:
            raise serializers.ValidationError("Age must be greater than 18")
        return value

    # object level validations
    def validate(self, data):
        name = data.get("name")
        salary = data.get("salary")
        age = data.get("age")
        if name.lower() == "ipsita" and age != 20:
            raise serializers.ValidationError("for ipsita name must be 20")
        if salary < 30000:
            raise serializers.ValidationError(
                "salary must be greater than or equal to 30000"
            )

        return data
