$(document).ready(function (){
    $("#login-form").submit(function (e) {
        e.preventDefault()
        let thisForm = $(this);
        let formData = thisForm.serialize();
        console.log("success "+formData)

        $.ajax({
            url:"{% url 'login_api' %}",
            method: 'POST',
            data: formData,
            dataType: 'json',
            success: function (data){
                console.log("success search")
            },
            error: function (errorData) {
                console.log("error")
                console.log(errorData)
            }
        })

    })
})
