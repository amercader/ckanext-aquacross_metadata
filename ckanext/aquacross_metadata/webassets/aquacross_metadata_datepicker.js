"use strict";

ckan.module('aquacross_metadata_datepicker', function ($, _) {
  return {
    initialize: function () {
      $.proxyAll(this, /_on/);

      var data_field_id = this.options.id;
      var data_field_id_selector = '#' + data_field_id;
      var current_date = $(data_field_id_selector).val();
      
      $(data_field_id_selector).datepicker();
      $(data_field_id_selector).datepicker( "option", "dateFormat", "yy-mm-dd" );
      $(data_field_id_selector).datepicker( "option", "changeMonth", true );
      $(data_field_id_selector).datepicker( "option", "changeYear", true );
      $(data_field_id_selector).datepicker( "option", "yearRange", "1900:2050");
      $(data_field_id_selector).datepicker( "setDate" , current_date );
    },
  };
});
