const user_input = $("#user-input")
const search_icon = $('#search-icon')
const artists_div = $('#replaceable-content')
const endpoint = '/home/'
const delay_by_in_ms = 700
let scheduled_function = false


let ajax_call = function (endpoint, request_parameters) {
	$.getJSON(endpoint, request_parameters)
		.done(response => {
			// fade out the artists_div, then:
			artists_div.fadeTo('slow', 0).promise().then(() => {
				// replace the HTML contents
				artists_div.html(response['html_from_view'])
				// fade-in the div with new contents
				artists_div.fadeTo('slow', 1)
				// stop animating search icon
				search_icon.removeClass('blink')
			})
		})
}



user_input.on('keyup', function () {


    $('.s-bck').css('display','block')
    $('.s-ic').css('display','none')

    if ($('.is-s').css('display') !== 'none' )
    {
         $('#replaceable-content').css('display','flex')
         $('.is-s').css('display','none')
    }


	const request_parameters = {
		q: $(this).val() // value of user_input: the HTML element with ID user-input
	}

	// start animating the search icon with the CSS class
	search_icon.addClass('blink')

	// if scheduled_function is NOT false, cancel the execution of the function
	if (scheduled_function) {
		clearTimeout(scheduled_function)
	}

	// setTimeout returns the ID of the function to be executed
	scheduled_function = setTimeout(ajax_call, delay_by_in_ms, endpoint, request_parameters)
})


if(window.location.href.indexOf("home") > -1)
{
    $('.link-dash').css('color','rgb(255,178,0)')
}

if(window.location.href.indexOf("user-profile") > -1)
{
    $('.link-prof').css('color','rgb(255,178,0)')
}

if(window.location.href.indexOf("teaching-request") > -1)
{
    $('.link-req').css('color','rgb(255,178,0)')
}

if(window.location.href.indexOf("change-password") > -1)
{
    $('.link-passwd').css('color','rgb(255,178,0)')
}

if(window.location.href.indexOf("enrolled-course") > -1)
{
    $('.u-enrol-courses').css('display','flex');
    $('.link-enrolled').css('color','rgb(255,178,0)')
    var w= window.innerWidth;
}

if(window.location.href.indexOf("logout") > -1)
{
    $('.link-lg-out').css('color','rgb(255,178,0)')
}

$('.m-c-txt').each(function(){
    $(this).click(()=>{
        let pdf_path=$(this).attr("href")
//        let countView=$.ajax({
//            url:"{% url 'UJUZI:guest_registration' %}",
//            method:"POST",
//            dataType:'json',
//            data:{data:pdf_path}
//        })
//        countView.done((response)=>{
//                //result after request
//        })
    })
})


