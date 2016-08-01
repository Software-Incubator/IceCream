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
    $("#Name").focusout(function (event) {
        if (event.charCode!=0) {
            var regex = new RegExp("^[a-zA-Z ]+$");
            if (!regex.test($(this).val())) {
                $( "#Name" ).after( "<span class='validationerror'>Invalid Name </span>" );
            }
        }
    });

    $("#Name").focusin(function () {
        if (event.charCode!=0) {
            $("#Name").siblings("span").each(function () {
                $(this).remove()
            });
        }
    });

    $("#Email").focusout(function (event) {
        if (event.charCode!=0) {
            var regex = new RegExp("^[+a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$");
            if (!regex.test($("#Email").val())) {
                $( "#Email" ).after( "<span class='validationerror'>Invalid Email</span>" );
            }
        }
    });

    $("#Email").focusin(function () {
        if (event.charCode!=0) {
            $("#Email").siblings("span").each(function () {
                $(this).remove()
            });
        }
    });


    $("#Contact").focusout(function (event) {
        if (event.charCode!=0) {
            var regex = new RegExp("^[0-9]{10}$");
            if (!regex.test($("#Contact").val())) {
                $( "#Contact" ).after( "<span class='validationerror'>Invalid Mobile Number </span>" );
            }
        }
    });

    $("#Contact").focusin(function () {
        if (event.charCode!=0) {
            $("#Contact").siblings("span").each(function () {
                $(this).remove()
            });
        }
    });


    $("#Student").focusout(function (event) {
        if (event.charCode!=0) {
            var regex = new RegExp("^[0-9]{7}[dD]?$");
            if (!regex.test($("#Student").val())) {
                $( "#Student" ).after( "<span class='validationerror'>Invalid Student Number </span>" );
            }
        }
    });

    $("#Student").focusin(function () {
        if (event.charCode!=0) {
            $("#Student").siblings("span").each(function () {
                $(this).remove()
            });
        }
    });


});


$(document).ready(function () {
    $("#Year").val("2");
});