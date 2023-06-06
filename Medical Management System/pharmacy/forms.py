from cgi import FieldStorage
from turtle import filling
from django.forms import ModelForm
from .models import *
from crispy_forms.helper import FormHelper, Layout
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.forms import Form
from django.http import JsonResponse
from django.core.exceptions import ValidationError
from phonenumber_field.formfields import PhoneNumberField
from django.core.validators import RegexValidator

import json
class PatientPicForm1(forms.ModelForm):
    class Meta:
        model=Patients
        fields='__all__'
        exclude=['admin','gender','mobile','address','dob']
      
# class BillingForm(forms.ModelForm):
#     class Meta:
#         model = Billing
#         fields = ('patient_name', 'age', 'mobile', 'description', 'quantity', 'price', 'total')
#         widgets = {
#             'patient_name': forms.TextInput(attrs={'class': 'form-control'}),
#             'age': forms.TextInput(attrs={'class': 'form-control'}),
#             'mobile': forms.TextInput(attrs={'class': 'form-control'}),
#             'description': forms.TextInput(attrs={'class': 'form-control'}),
#             'quantity': forms.TextInput(attrs={'class': 'form-control'}),
#             'price': forms.TextInput(attrs={'class': 'form-control'}),
#             'total': forms.TextInput(attrs={'class': 'form-control'}),
#         }

#     def __init__(self, *args, **kwargs):
#         super(BillingForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'POST'
#         self.helper.layout = Layout(
#             FieldStorage(
#                 '',
#                 'patient_name',
#                 'age',
#                 'mobile',
#                 'description',
#                 'quantity',
#                 'price',
#                 'total',
#             ),
#             ButtonHolder(
#                 Submit('submit', 'Submit', css_class='btn btn-success')
#             )
#         )
# class BillingForm(forms.ModelForm):
#     class Meta:
#         model = Billing
#         fields = (
#             'patient_name',
#             'age',
#             'mobile',
#             'description',
#             'quantity',
#             'price',
#             'total',
#         )

#     def __init__(self, *args, **kwargs):
#         super(BillingForm, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_method = 'POST'
#         self.helper.layout = Layout(
#             Field('patient_name', css_class='form-control'),
#             Field('age', css_class='form-control'),
#             Field('mobile', css_class='form-control'),
#             Field('description', css_class='form-control'),
#             Field('quantity', css_class='form-control'),
#             Field('price', css_class='form-control'),
#             Field('total', css_class='form-control'),
#             ButtonHolder(
#                 Submit('submit', 'Submit', css_class='btn btn-success')
#             )
#         )


# class BillingForm(forms.ModelForm):
#     quantity = forms.IntegerField()
#     price = forms.DecimalField()

#     class Meta:
#         model = Billing
#         fields = ['patient_name', 'age', 'mobile', 'description', 'quantity', 'price']

#     def clean(self):
#         cleaned_data = super().clean()
#         quantity = cleaned_data.get('quantity')
#         price = cleaned_data.get('price')
#         if quantity and price:
#             total = quantity * price
#             cleaned_data['total'] = total
#         return cleaned_data


# class BillingForm(forms.ModelForm):
#     class Meta:
#         model = Billing
#         fields = ('patient_name', 'age', 'mobile', 'tablet', 'quantity', 'price')

# class BillingForm(forms.ModelForm):
#     tablet = forms.CharField(max_length=50)
#     quantity = forms.CharField(max_length=50)
#     price = forms.CharField(max_length=50)

#     class Meta:
#         model = Billing
#         fields = ['patient_name', 'age', 'mobile', 'tablet', 'quantity', 'price']

#     def clean(self):
#         cleaned_data = super().clean()
#         quantity = cleaned_data.get('quantity')
#         price = cleaned_data.get('price')
#         if quantity and price:
#             total = sum([int(qty) * int(p) for qty, p in zip(quantity.split(','), price.split(','))])
#             cleaned_data['total'] = total
#         return cleaned_data

class BillingForm(forms.ModelForm):
    patient_name = forms.CharField(max_length=50, required=True)
    age = forms.IntegerField(required=True)
    mobile = forms.CharField(max_length=50, required=True)
    tablet = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 80}), max_length=2000, required=True)
    quantity = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 80}), max_length=2000, required=True)
    price = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'cols': 80}), max_length=2000, required=True)

    class Meta:
        model = Billing
        fields = ['patient_name', 'age', 'mobile', 'tablet', 'quantity', 'price']

    def clean(self):
        cleaned_data = super().clean()
        quantity = cleaned_data.get('quantity')
        price = cleaned_data.get('price')
        if quantity and price:
            # Split the quantity and price strings by comma
            quantity_list = quantity.split(',')
            price_list = price.split(',')
            # Calculate the total
            total = 0
            for i in range(len(quantity_list)):
                total += int(quantity_list[i]) * int(price_list[i])
            cleaned_data['total'] = str(total)
        return cleaned_data
    
    





class DateInput(forms.DateInput):
    input_type = "date"

from phonenumber_field.formfields import PhoneNumberField
class ClientForm(forms.Form):
    mobile = PhoneNumberField()

class PatientForm(forms.Form):

    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    password = forms.CharField(label="Password", max_length=50, widget=forms.PasswordInput(attrs={"class":"form-control"}))
    reg_no = forms.CharField(label="Reg No", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    phone_number = forms.CharField(label="Mobile", max_length=50)
    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )
    gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    dob= forms.DateField(label="dob", widget=DateInput(attrs={"class":"form-control"}))

    # Validations for patient
    def clean_reg_no(self):
        reg_no = self.cleaned_data['reg_no']
        if  not  reg_no:
            raise ValidationError("This field is required")
        for instance in Patients.objects.all():
            if instance.reg_no==reg_no:
                raise ValidationError( "Registration number aready exist")
      
        return reg_no


    def clean_phone_number(self):
        phone_number=self.cleaned_data.get('phone_number')
        if not phone_number:
            raise forms.ValidationError('This field is requied')
        elif len(phone_number) < 10:
            raise forms.ValidationError('Invalid Number')
        for instance in Patients.objects.all():
            if instance.phone_number==phone_number:
                raise ValidationError( "PhoneNumber aready exist")
        
        return phone_number
        
            
   
    def clean_username(self):
        username = self.cleaned_data['username']
        if  not  username:
            raise ValidationError("This field is required")
        for instance in CustomUser.objects.all():
            if instance.username==username:
                raise ValidationError( "Username aready exist")
      
        return username

    def clean_firstName(self):
        first_name = self.cleaned_data['first_name']
        if  not  first_name:
            raise ValidationError("This field is required")
        return first_name

    def clean_secondName(self):
        last_name = self.cleaned_data['last_name']
        if  not  last_name:
            raise ValidationError("This field is required")
        return last_name

class EditPatientForm(forms.Form):
    username = forms.CharField(label="Username", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    email = forms.EmailField(label="Email", max_length=50, widget=forms.EmailInput(attrs={"class":"form-control"}))
    
    first_name = forms.CharField(label="First Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    last_name = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    address = forms.CharField(label="Address", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    phone_number = forms.CharField(label="Mobile", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    gender_list = (
        ('Male','Male'),
        ('Female','Female')
    )
    gender = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
    dob= forms.DateField(label="dob", widget=DateInput(attrs={"class":"form-control"}))
   
    
    

class StockForm(forms.ModelForm):
    valid_to= forms.DateField(label="Expiry Date", widget=DateInput(attrs={"class":"form-control"}))

    class Meta:
        model=Stock
        fields='__all__'
        exclude=['valid_from','reorder_level','receive_quantity', 'prescrip_drug_acess']

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model=Prescription
        fields='__all__' 

class CustomerForm(ModelForm):
    class Meta:
        model=Pharmacist
        fields='__all__'
        exclude=['admin','gender','mobile','address']


       

class DoctorForm(ModelForm):
    class Meta:
        model=Doctor
        fields='__all__'
        exclude=['admin','gender','mobile','address']

        def clean_firstName(self):
            first_name = self.cleaned_data['first_name']
            if  not  first_name:
                raise ValidationError("This field is required")
            return first_name

        def clean_mobile(self):
            mobile=self.cleaned_data.get('mobile')
            if not mobile:
                raise forms.ValidationError('This field is requied')
            return mobile
        def clean_username(self):
            username = self.cleaned_data['username']
            if  not  username:
                raise ValidationError("This field is required")
            for instance in CustomUser.objects.all():
                if instance.username==username:
                    raise ValidationError( "Username aready exist")

class ClerkForm(ModelForm):
    class Meta:
        model=PharmacyClerk
        fields='__all__'
        exclude=['admin','gender','mobile','address']
class HodForm(ModelForm):
    class Meta:
        model=AdminHOD
        fields='__all__'
        exclude=['admin','gender','mobile','address']

class PatientSearchForm1(ModelForm):
    
    class Meta:
        model=Patients
        fields='__all__'
        exclude=['profile_pic','gender','mobile','address','dob']
class PatientForm7(ModelForm):
     class Meta:
        model=Patients
        fields='__all__'






class DispenseForm(ModelForm):
    # gender_list = (
       
    # )
    # drug_id = forms.ChoiceField(label="Gender", choices=gender_list, widget=forms.Select(attrs={"class":"form-control"}))
   
    class Meta:
        model=Dispense
        fields='__all__'
        exclude=['stock_ref_no']
        
    #     drug_id = forms.CharField(label="Last Name", max_length=50, widget=forms.TextInput(attrs={"class":"form-control"}))
    # # def updateItem(self,request):
 
    #     data=json.loads(request.body)
    #     drugId=data['drugId']
    #     print('ACTION:',drugId)
    #     drug_name = forms.CharField(label="Mobile", max_length=50, widget=forms.TextInput(attrs={"value":drugId}))

    # # # stock=Stock.objects.get(id=drugId)
    # # # # drugs=Stock.objects.all()
    # # # form=DispenseForm(request.POST or None,instance=stock,initial={'patient_id':queryset} )
    # # # if form.is_valid():
    # # #     instance=form.save(commit=False)
    # # #     instance.quantity-=instance.dispense_quantity
        
    # #     # instance.save()
    #     return JsonResponse('jamara dd',  safe=False)
 
class ReceiveStockForm(ModelForm):
    valid_to= forms.DateField(label="Expiry Date", widget=DateInput(attrs={"class":"form-control"}))

    class Meta:
        model=Stock
        fields='__all__'
        exclude=['category' ,'drug_name','valid_from','dispense_quantity','reorder_level','date_from','date_to','quantity','manufacture']


class ReorderLevelForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['reorder_level']

