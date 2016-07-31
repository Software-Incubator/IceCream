function validateBranch () {
    console.log("Branch Changed");

    if ($("#Branch").val() == "MCA") {
        $("#Year").val("1");
    }
    else  {
        $("#Year").val("2");
    }
}


$(document).ready(function () {
    $("#Year").val("2");
});