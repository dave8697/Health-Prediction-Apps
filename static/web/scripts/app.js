function onlyNumber(evt) {
         
    // Only ASCII character in that range allowed
    var ASCIICode = (evt.which) ? evt.which : evt.keyCode
    if (ASCIICode > 31 && (ASCIICode < 48 && ASCIICode != 46 || ASCIICode > 57))
        return false;
    return true;
}

function onlyAge(evt) {
         
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
    else
    return true;
}