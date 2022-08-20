

    $('.cat-courses-li').css('display','none');
    $('.latest-c').css('display','flex');


$('.splide__list').on('click', '.category-li', function () {
    alert("click");
});

    $('.category-li').each(function(){
           $(this).click(()=>{

//            alert('am clicked')
            $('.cat-courses-li').css('display','flex');
            $('.cat-courses-li').css('padding-top','10px');
            $('.latest-c').css('display','none');

//            let catId=$(this).attr('id').substring(4)

            let catId=$(this).find('.u-cat-no').text();


            let catName=$(this).find('.course-category-name').text()
             $('.sub-title .cat-name').html(catName)

            $('.u-course').css('visibility','hidden');
            $('.u-course').css('opacity',1);
            $('.u-course').css('display','none');



            $('.course-'+catId).css('visibility','visible');
            $('.course-'+catId).css('opacity',1);
            $('.course-'+catId).css('display','flex');



        })
    })





//  var getCategoryCourses=$.ajax({
//    url:"../assets/php/getCategoryCourses",
//    method:"POST",
//    data:{categoryId:categoryId}
//  })
//  getCategoryCourses.done((response)=>{
//
//    $('.category-course-title').html(categoryName+" - courses")
//    $('.category-course-title').append('<div class="show-add-box-btn">Add new course</div>')
//    $('.show-add-box-btn').click(()=>{
//      hideExpandable()
//      moveExpandableTop()
//      $('.add-course-box').slideDown(1000)
//    })
//
//    if(response.trim()==="error")
//    {
//      feedback(3,"Something went wrong, try Again Later.")
//    }
//    else if(response.trim()==="empty")
//    {
//      feedback(2,"no courses yet")
//    }
//    else
//    {
//      $('.skill_courses').html(response)
//
//      // when the course is clicked
//      $('.course-item').each(function(){
//
//        $(this).click(()=>{
//
//          let courseId=$(this).attr('id').substring(9)
//          let courseTitle=$('#c-course-'+courseId).find('.trend-course-title').text().trim()
//          let courseDesc=$('#c-course-'+courseId).find('.course-description-txt-data').text().trim()
//          let img_path=$('#c-course-'+courseId+' .s-course-img').find('img').attr('src');
//
//          $.cookie("selectedCourseId",courseId)
//          $.cookie("selectedCourseTitle",courseTitle)
//          $.cookie("selectedCourseDesc",courseDesc)
//          $.cookie("selectedCoursCover",img_path)
//
//          window.location.href="course"
//
//        })
//
//      })
      // end of course clicked