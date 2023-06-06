from django import forms
from .models import Book
 
# class BookForm(forms.Form):
#     name =  forms.CharField()
#     author_name = forms.CharField()
#     content = forms.CharField()

class BookForm(forms.ModelForm):
    timestamp = forms.CharField(widget=forms.DateInput(attrs={"type":"date"}))
    # category = forms.CharField()
    class Meta:
        model = Book
        fields = ("name", "author_name", "content","timestamp")



        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)

            print(self.fields)

            for field in self.fields.values():
                field.widget.attrs.update({"class": "alma"})

                # class adini deyismek ucun bundan istifade edirik

                # self.fields["name"].widget.attrs.update({"class":"underline"})

                # self.fields["name"].widget.attrs["class"]+="underline"