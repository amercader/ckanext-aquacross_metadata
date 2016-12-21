// Enable JavaScript's strict mode. Strict mode catches some common
// programming errors and throws exceptions, prevents some unsafe actions from
// being taken, and disables some confusing and bad JavaScript features.
"use strict";

ckan.module('case_study', function ($, _) {
  return {
    initialize: function () {
      var delegated = this.el
      this.el.on('change', delegated, this._onChange);
      //var text_clean_1 =  $('#field-md_bbox_north')
      //this.el.on('click', text_clean_1, this._onClick);
      //console.log("I've been initialized for element: ", this.el);

    },

    _onChange: function (event) {
      /*console.log("changed");
       console.log("value:"+$('#field-md_aquacross_case_study').val());
      console.log($('#field-md_bbox_north'));*/

      var case_study = $('#field-md_aquacross_case_study').val();

      if ( case_study == 'Case Study 1 - North Sea') {
        $('#field-md_bbox_north').val('62') ;
        $('#field-md_bbox_south').val('48') ;
        $('#field-md_bbox_west').val('-5') ;
        $('#field-md_bbox_east').val('12.95') ;
      } else if (case_study == 'Case Study 2 - Mediterranean - Andalusia Spain and Morocco') {
        $('#field-md_bbox_north').val('36.97') ;
        $('#field-md_bbox_south').val('34.80') ;
        $('#field-md_bbox_west').val('-5.84') ;
        $('#field-md_bbox_east').val('-4.68') ;
      } else if (case_study == 'Case Study 3 - Danube River Basin') {

        $('#field-md_bbox_north').val('50.24') ;
        $('#field-md_bbox_south').val('42.08') ;
        $('#field-md_bbox_west').val('8.15') ;
        $('#field-md_bbox_east').val('29.76') ;

      } else if ( case_study == 'Case Study 4 - Lough Erne - Ireland') {
        $('#field-md_bbox_north').val('54.64') ;
        $('#field-md_bbox_south').val('53.77') ;
        $('#field-md_bbox_west').val('-8.13') ;
        $('#field-md_bbox_east').val('-6.75') ;
      } else if ( case_study == 'Case Study 5 - Vouga River - Portugal') {
        $('#field-md_bbox_north').val('40.87') ;
        $('#field-md_bbox_south').val('40.48') ;
        $('#field-md_bbox_west').val('-8.86') ;
        $('#field-md_bbox_east').val('-8.45') ;
      } else if ( case_study == 'Case Study 6 - Ronne a - Sweden' ) {
        $('#field-md_bbox_north').val('55.90') ;
        $('#field-md_bbox_south').val('55.84') ;
        $('#field-md_bbox_west').val('13.50') ;
        $('#field-md_bbox_east').val('13.60') ;
      } else if ( case_study == 'Case Study 7 - Swiss Plateau' ) {
        $('#field-md_bbox_north').val('47.80') ;
        $('#field-md_bbox_south').val('46.13') ;
        $('#field-md_bbox_west').val('5.96') ;
        $('#field-md_bbox_east').val('9.67') ;
      } else if ( case_study == 'Case Study 8 - The Azores' ) {
         $('#field-md_bbox_north').val('40.62') ;
        $('#field-md_bbox_south').val('36.02') ;
        $('#field-md_bbox_west').val('-32.44') ;
        $('#field-md_bbox_east').val('-23.89') ;

      }
      var north =   $('#field-md_bbox_north').val();
      var south =   $('#field-md_bbox_south').val();
      var west =   $('#field-md_bbox_west').val();
      var east =   $('#field-md_bbox_east').val();
      var spatial_query = '{ "type": "Polygon", "coordinates": [[['+east+","+south+"], ["+east+","+north+"], ["+west+", "+north+"], ["+west+","+south+"],["+east+","+south+"]]]}"
      //console.log(spatial_query)
      $('#field-hidden_spatial_query').val(spatial_query );





    }


 };

});