(function ($) {
Drupal.behaviors.resume = {
  attach: function(context, settings) {
    // Hide all the job attributes.
    $('#experience .job .attributes').hide();

    // Show job attributes/details when user clicks the toggle.
    $('#experience .job a.toggle-details').click(function() {
      $(this).parent().next('.attributes').slideToggle('slow');
      return false;
    })
  }
};
})(jQuery);