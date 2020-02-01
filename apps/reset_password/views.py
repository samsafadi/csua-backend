from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.core.mail import send_mail
from django.shortcuts import redirect

import ldap_bindings
from forms import PasswordResetForm

REDIRECT = "csua.berkeley.edu"

def PasswordResetView(request):
    if request.method == "POST":
        form = PasswordResetForm(request.POST)
        username = form.cleaned_data["username"]
        email = form.cleaned_data["email"]
        if ldap_bindings.valid_username_email(username, email):
            send_mail
            (
                'CSUA Account Password Reset Link',
                'Reset Your password at this link:', # TODO: make link
                'django@csua.berkeley.edu',
                email,
                True
            )
            return redirect(REDIRECT)
        else:
            return redirect(REDIRECT)
    else:
        form = PasswordResetForm()

    return render(request, "html thing", {"form": form})

def password_reset_url(request, uid,


def valid_password(password):
    """
    The password must be at least nine characters long. Also, it must include characters from
    two of the three following categories:
    -alphabetical
    -numerical
    -punctuation/other
    """
    punctuation = set("""!@#$%^&*()_+|~-=\`{}[]:";'<>?,./""")
    alpha = False
    num = False
    punct = False

    if len(password) < 9:
        return False

    for character in password:
        if character.isalpha():
            alpha = True
        if character.isdigit():
            num = True
        if character in punctuation:
            punct = True
    return (alpha + num + punct) >= 2
