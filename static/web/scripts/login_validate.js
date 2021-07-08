window.onload = function()
{
    document.forms[0].onsubmit = function()
    {
        var email_value = this.elements[0].value;
        if(email_value == "")
        {
            alert("Email cannot be blank");
            return false;
        }
        var password_value = this.elements[1].value;
        if(password_value == "")
        {
            alert("Enter a password first");
            return false;
        }
        return true;
    }
}