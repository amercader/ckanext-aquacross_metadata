// Enable JavaScript's strict mode. Strict mode catches some common
// programming errors and throws exceptions, prevents some unsafe actions from
// being taken, and disables some confusing and bad JavaScript features.
"use strict";

ckan.module('spatial_query', function ($, _) {
  return {
    initialize: function () {
      var delegated = this.el
      //this.el.on('click', delegated, this._onClick);
      this.el.on('blur', delegated, this._onBlur);
      //var text_clean_1 =  $('#field-md_bbox_north')
      //this.el.on('click', text_clean_1, this._onClick);
      //console.log("I've been initialized for element: ", this.el);


    },

    _onBlur: function (event) {

      //console.log("bluring");
      var north =   $('#field-md_bbox_north').val();
      var south =   $('#field-md_bbox_south').val();
      var west =   $('#field-md_bbox_west').val();
      var east =   $('#field-md_bbox_east').val();
     var spatial_query = '{ "type": "Polygon", "coordinates": [[['+east+","+south+"], ["+east+","+north+"], ["+west+", "+north+"], ["+west+","+south+"],["+east+","+south+"]]]}"
      $('#field-hidden_spatial_query').val(spatial_query );
      //console.log($('#field-hidden_spatial_query').val())
    },


    _onClick: function (event) {

      //console.log("clicked")

      this.value = '';

    }


 };

});