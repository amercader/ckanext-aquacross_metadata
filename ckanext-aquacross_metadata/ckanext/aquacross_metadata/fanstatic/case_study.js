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
        $('#field-md_bbox_north').val('4405785.74') ;
        $('#field-md_bbox_south').val('2871127.78') ;
        $('#field-md_bbox_west').val('3209840.75') ;
        $('#field-md_bbox_east').val('4502460.20') ;
      } else if (case_study == 'Case Study 2 - Mediterranean - Andalusia Spain and Morocco') {
        $('#field-md_bbox_north').val('1679697.28') ;
        $('#field-md_bbox_south').val('1444513.28') ;
        $('#field-md_bbox_west').val('2876401.76') ;
        $('#field-md_bbox_east').val('3011049.04') ;
      } else if (case_study == 'Case Study 3 - Danube River Basin') {

        $('#field-md_bbox_north').val('3038400.00') ;
        $('#field-md_bbox_south').val('2190500.00') ;
        $('#field-md_bbox_west').val('4183100.00') ;
        $('#field-md_bbox_east').val('5854500.00') ;

      } else if ( case_study == 'Case Study 4 - Lough Erne - Ireland') {
        $('#field-md_bbox_north').val('3643775.38') ;
        $('#field-md_bbox_south').val('3546248.75') ;
        $('#field-md_bbox_west').val('3154508.05') ;
        $('#field-md_bbox_east').val('3236010.17') ;
      } else if ( case_study == 'Case Study 5 - Vouga River - Portugal') {
        $('#field-md_bbox_north').val('2169207.83') ;
        $('#field-md_bbox_south').val('2125973.01') ;
        $('#field-md_bbox_west').val('2733158.31') ;
        $('#field-md_bbox_east').val('2768907.70') ;
      } else if ( case_study == 'Case Study 6 - Ronne a - Sweden' ) {
        $('#field-md_bbox_north').val('55.9049') ;
        $('#field-md_bbox_south').val('55.8416') ;
        $('#field-md_bbox_west').val('13.4956') ;
        $('#field-md_bbox_east').val('13.6006') ;
      } else if ( case_study == 'Case Study 7 - Swiss Plateau' ) {
        $('#field-md_bbox_north').val('2743898.44') ;
        $('#field-md_bbox_south').val('2565779.02') ;
        $('#field-md_bbox_west').val('4008277.87') ;
        $('#field-md_bbox_east').val('4296379.47') ;
      } else if ( case_study == 'Case Study 8 - The Azores' ) {
         $('#field-md_bbox_north').val('2793309.68') ;
        $('#field-md_bbox_south').val('2250076.72') ;
        $('#field-md_bbox_west').val('943762.94') ;
        $('#field-md_bbox_east').val('1328056.08') ;

      }







    }


 };

});