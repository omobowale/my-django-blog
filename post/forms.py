from django import forms
from post.models import Post
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

bad_words = ["abuse", "idiot", "stupid"]

class PostForm(forms.ModelForm):
    
    title = forms.CharField(required=False)  # disable default required check
    content = forms.CharField(required=False)  # disable default required check
    
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'image']
        
        
    def clean_title(self):
        print("I must get here.")
        title = self.cleaned_data.get("title")
        if not title:
            raise forms.ValidationError("Title cannot be empty")
        
        return title
        
        
    def clean_content(self):
        content = self.cleaned_data.get("content")
        if not content:
            raise forms.ValidationError("Content cannot be empty")
        
        found_bad_words = []
        
        for word in bad_words:
            if word in content:
                found_bad_words.append(word)
        
        
        if len(found_bad_words) > 0:
            raise forms.ValidationError(f"Content cannot contain bad word(s):  {", ".join(found_bad_words)}")
        
        return content
        


class RegistrationForm(UserCreationForm):
    
    
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "first_name", "last_name"]
        