from rest_framework import serializers
from .models import Teacher, Student, Book

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ('id', 'name', 'email', 'age', 'subject_teaches', 'phone', 'address', 'city')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'name', 'written_by', 'price', 'subject')
        
######## Using Serializer class #########
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    age = serializers.IntegerField()
    grade = serializers.IntegerField()
    phone = serializers.CharField(max_length=15)
    address = serializers.CharField(max_length=100)
    city = serializers.CharField(max_length=100)




    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.age = validated_data.get('age', instance.age)
        instance.grade = validated_data.get('grade', instance.grade)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.address = validated_data.get('address', instance.address)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance


############## Field Level Validations ##############
    def validate_name(self,name):
        if any(char.isdigit() for char in name):
            raise serializers.ValidationError("Name cannot contain numbers")
        return name

    def validate_email(self,email):
        if "@" not in email:
            raise serializers.ValidationError("Email should be of gmail.com")
        return email
    
    def validate_phone(self,phone):
        if len(phone) > 15:
            raise serializers.ValidationError("Phone number should be of 10 digits")
        return phone

    ############### Object Level Validation ################
    # def validate(self, attrs):
    #     if attrs['age']  > 25:
    #         raise serializers.ValidationError("Age should be lesser than 25")
        
    #     if attrs['grade'] < 1:
    #         raise serializers.ValidationError("Grade should be greater than 0")
    #     return attrs



############# Function Validation #############
    def email_validation(email):
        if email[-8:] != "@gmail.com":
            raise serializers.ValidationError("Email should be of gmail.com")
        return email


    
        


    