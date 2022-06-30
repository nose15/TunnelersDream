from django import forms


class GetFirstPoint(forms.Form):
    x = forms.FloatField(label='X')
    z = forms.FloatField(label='Z')
    x_margin = forms.IntegerField(label="How far can the X coordinate of the point be moved from your specified point? "
                                        "(We do this to make a chance for better fitting lines to be created)")
    z_margin = forms.IntegerField(label="How far can the X coordinate of the point be moved from your specified point? "
                                        "(We do this to make a chance for better fitting lines to be created)")


class GetSecondPoint(forms.Form):
    x1 = forms.FloatField(label='X')
    z1 = forms.FloatField(label='Z')
    x_margin = forms.IntegerField(label="How far can the X coordinate of the point be moved from your specified point? "
                                        "(We do this to make a chance for better fitting lines to be created)")
    z_margin = forms.IntegerField(label="How far can the X coordinate of the point be moved from your specified point? "
                                        "(We do this to make a chance for better fitting lines to be created)")
