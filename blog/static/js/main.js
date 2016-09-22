/**
 * Created by JUSTICE on 9/11/2016.
 */

$(document).ready(function() {

  $("#owl").owlCarousel({

      autoPlay: 3000,
      navigation : true, // Show next and prev buttons
      slideSpeed : 300,
      //paginationSpeed : 400,
      singleItem:true,
      autoHeight : true,
      transitionStyle: "fade"

      // "singleItem:true" is a shortcut for:
      // items : 1,
      // itemsDesktop : false,
      // itemsDesktopSmall : false,
      // itemsTablet: false,
      // itemsMobile : false

  });

});
