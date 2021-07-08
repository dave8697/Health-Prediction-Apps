document.forms[0].onsubmit=function()
{
    var fname = this.elements[1].value;
    var letters = /^[A-Za-z\s]+$/;
    if(!fname.match(letters))
    {
        alert("\nInvalid Name: Please enter a valid First name");
        return false;
    }

    var lname = this.elements[2].value;
    var letters = /^[A-Za-z\s]+$/;
    if(!lname.match(letters))
    {
        alert("\nInvalid Name: Please enter a valid Last name");
        return false;
    }

    var email = this.elements[5].value;
    var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    if (emailPattern.test(email) == false)
    {
        alert("\nEmail should be in the format: abc@xyz.com");
        return false;
    }
    else
    return true;
}