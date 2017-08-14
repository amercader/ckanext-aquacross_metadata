// Enable JavaScript's strict mode. Strict mode catches some common
// programming errors and throws exceptions, prevents some unsafe actions from
// being taken, and disables some confusing and bad JavaScript features.
"use strict";

// list of case studies with spatial bounding box area
var case_studies =  [ {"value":"cs1", 
                       "name":"Case Study 1 - North Sea", 
                       "area": {"west": -5.00, "south": 48.00, "east": 12.95, "north": 62.00}
                      },
                      {"value":"cs2",
                       "name":"Case Study 2 - Mediterranean - Andalusia Spain and Morocco",
                       "area": { "west": -5.84, "south": 34.80, "east": -4.68, "north": 36.97 }
                      },
                      {"value":"cs3", 
                       "name":"Case Study 3 - Danube River Basin",
                       "area": { "west":  8.15, "south": 42.08, "east": 29.76, "north": 50.24 }
                      },
                      {"value":"cs4",
                       "name":"Case Study 4 - Lough Erne - Ireland",
                       "area": { "west": -8.13, "south": 53.77, "east": -6.75, "north": 54.64 }
                      },
                      {"value":"cs5",
                       "name":"Case Study 5 - Vouga River - Portugal",
                       "area": { "west": -8.86, "south": 40.48, "east": -8.45, "north": 40.87 }
                      },
                      {"value":"cs6",
                       "name":"Case Study 6 - Ronne a - Sweden",
                       "area": { "west": 13.50, "south": 55.84, "east": 13.60, "north": 55.90 }
                      },
                      {"value":"cs7",
                       "name":"Case Study 7 - Swiss Plateau",
                       "area": { "west":  5.96, "south": 46.13, "east":  9.67, "north": 47.80 }
                      },
                      {"value":"cs8",
                       "name":"Case Study 8 - The Azores",
                       "area": { "west":-32.44, "south": 36.02, "east":-23.89, "north": 40.62 }
                      }
                    ];

// Function to convert number string to a float and back.
// This is a way to clean up the numbers if missing number before decimal point, etc.
// But strings are kept as is, such bad valves will be flagged by the form validator on sumbit
// Input argument: Pass in element id with hash (#), so that jQuery can select the form element's value
function cleanNumber(form_field) {

    // if no form field or form field value, return
    if( !form_field || !$(form_field).val() )
        return;

    // clean the form field value, refer to the Javascript Number regarding reformatting
    var number_string = $(form_field).val().trim();
    if( number_string ) {
        var number_float = Number(number_string);
        if( !isNaN(number_float) ) {
             number_string = number_float.toString();
        }
    }
    $(form_field).val(number_string);
}

// manage the case study options list
ckan.module('case_study_list', function ($, _) {
    return {
        initialize: function () {
            // initialise the case study options list...

            // get empty select tag element
            var select_tag = document.getElementById("field-md_aquacross_case_study");

            // build select options list, add to above select tag...
            // first, create an empty option named 'None' 
            var opt = document.createElement('option');
            opt.value = "";
            opt.innerHTML = "None";
            opt.selected = true;
            select_tag.appendChild(opt);
            for(var i=0; i < case_studies.length; i++) {
                // next, create options from the JSON 'case_studies' list
                var opt = document.createElement('option');
                opt.value = case_studies[i]['value'];
                opt.innerHTML = case_studies[i]['name'];
                select_tag.appendChild(opt);
            }
            // finally, build an option named 'Custom'
            var opt = document.createElement('option');
            opt.value = "custom";
            opt.innerHTML = "Custom";
            select_tag.appendChild(opt);

            // register for onChange event for the select options list
            var delegated = this.el;
            this.el.on('change', delegated, this._onChange);

            // get the current metadata bounding box if exists if the form...
            // then check the north, south, east, west values from the text form fields
            var spatial_field_east = $('#field-md_bbox_east').val();
            var spatial_field_south = $('#field-md_bbox_south').val();
            var spatial_field_west = $('#field-md_bbox_west').val();
            var spatial_field_north = $('#field-md_bbox_north').val();

            // check if the bounding box info is all empty
            if( spatial_field_west === "" &&
                spatial_field_south === "" &&
                spatial_field_east === "" &&
                spatial_field_north === "" ) {

                // bounding box is all empty, no further processing required as no bounding box was not entered (or partly entered)
                return;
            }

            // have non-empty bounding box info, check if it is a pre-defined case study
            var case_study_match = false;
            for(var i=0; i < case_studies.length; i++) {
                if( Number(spatial_field_west) === Number(case_studies[i]['area']['west']) && 
                    Number(spatial_field_south) === Number(case_studies[i]['area']['south']) &&
                    Number(spatial_field_east) === Number(case_studies[i]['area']['east']) && 
                    Number(spatial_field_north) === Number(case_studies[i]['area']['north']) ) {

                    // pre-defined case study area match. Select this in dropdown list
                    $('#field-md_aquacross_case_study').val(case_studies[i]['value']);
                    case_study_match = true;
                    break;
                } 
            }

            // if not a pre-defined case study area match
            if( case_study_match === false ) {

                // have non-empty and non-predefined bounding box info, it is a custom area
                // therefore enable the input text boxes for editing
                $('#field-md_aquacross_case_study').val("custom");
                $('#field-md_bbox_north').prop("readonly",false);
                $('#field-md_bbox_south').prop("readonly",false);
                $('#field-md_bbox_west').prop("readonly",false);
                $('#field-md_bbox_east').prop("readonly",false);
            }
        },
        _onChange: function (event) {
            // select option changed...

            // get selected option
            var case_study = $('#field-md_aquacross_case_study').val();
            var extent_boxes_readonly = false;

            if( case_study === "" ) {
                // no case study or custom area selected, reset input form fields to empty values, make non-editable
                $('#field-md_bbox_north').val("");
                $('#field-md_bbox_south').val("");
                $('#field-md_bbox_west').val("");
                $('#field-md_bbox_east').val("");
                extent_boxes_readonly = true;
            }
            else if( case_study === "custom" ) {
                // custom area selected, reset input form fields to empty values, make editable
                $('#field-md_bbox_north').val("");
                $('#field-md_bbox_south').val("");
                $('#field-md_bbox_west').val("");
                $('#field-md_bbox_east').val("");
                extent_boxes_readonly = false;
            }
            else {
                // pre-defined case study selected
                var west = 0.0;
                var south = 0.0;
                var east = 0.0;
                var north = 0.0;

                // find case study coordinates in the JSON 'case_studies' list
                for(var i=0; i < case_studies.length; i++) {
                    if( case_study === case_studies[i]['value'] ) {
                        west = case_studies[i]['area']['west'];
                        south = case_studies[i]['area']['south'];
                        east = case_studies[i]['area']['east'];
                        north = case_studies[i]['area']['north'];
                        extent_boxes_readonly = true;
                        break;
                    }
                }

                // check if we found the coordinates in the JSON 'case_studies' list
                if( extent_boxes_readonly === true ) {
                    // yes, have case study coordinates, set north, south, east and west text boxes  
                    $('#field-md_bbox_north').val(north);
                    $('#field-md_bbox_south').val(south);
                    $('#field-md_bbox_west').val(west);
                    $('#field-md_bbox_east').val(east);
                }
                else {
                    // unknown case study...
                    $('#field-md_bbox_north').val("");
                    $('#field-md_bbox_south').val("");
                    $('#field-md_bbox_west').val("");
                    $('#field-md_bbox_east').val("");
                }
            }

            // enable/disable extent coordinate input boxes for editing
            $('#field-md_bbox_north').prop("readonly",extent_boxes_readonly);
            $('#field-md_bbox_south').prop("readonly",extent_boxes_readonly);
            $('#field-md_bbox_west').prop("readonly",extent_boxes_readonly);
            $('#field-md_bbox_east').prop("readonly",extent_boxes_readonly);

            // clean up the numbers in terms of formatting 
            cleanNumber( '#field-md_bbox_north' );
            cleanNumber( '#field-md_bbox_south' );
            cleanNumber( '#field-md_bbox_west' );
            cleanNumber( '#field-md_bbox_east' );
        }
    };
});

// manage the spatial bounding box text input boxes
ckan.module('spatial_bbox_inputs', function ($, _) {
    return {
        initialize: function () {
            // initialise... add onBlur handler for the text box
            var delegated = this.el
            this.el.on('blur', delegated, this._onBlur);
        },
        _onBlur: function (event) {
            // clean up the numbers in terms of formatting for all the spatial coordinate input boxes
            cleanNumber( '#field-md_bbox_north' );
            cleanNumber( '#field-md_bbox_south' );
            cleanNumber( '#field-md_bbox_west' );
            cleanNumber( '#field-md_bbox_east' );
        }
    };
});

