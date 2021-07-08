function onlyNumber(evt) {
         
    // Only ASCII character in that range allowed
    var ASCIICode = (evt.which) ? evt.which : evt.keyCode
    if (ASCIICode > 31 && (ASCIICode < 48 || ASCIICode > 57))
        return false;
    return true;
}
document.forms[0].onsubmit=function()
{
    var name = this.elements[1].value;
    var letters = /^[A-Za-z\s]+$/;
    if(!name.match(letters))
    {
        alert("\nInvalid Name: Please enter a valid name");
        return false;
    }

    var email = this.elements[6].value;
    var emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/;
    if (emailPattern.test(email) == false)
    {
        alert("\nEmail should be in the format: abc@xyz.com");
        return false;
    }
    var pass1 = this.elements[7].value;
    var pass2 = this.elements[8].value;

    if (pass1 != pass2)
    {
        alert ("\nPassword did not match: Please try again");
        return false;
    }
    else
    return true;
}