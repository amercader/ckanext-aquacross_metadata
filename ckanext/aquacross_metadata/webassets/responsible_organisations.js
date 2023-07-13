// Enable JavaScript's strict mode. Strict mode catches some common
// programming errors and throws exceptions, prevents some unsafe actions from
// being taken, and disables some confusing and bad JavaScript features.
"use strict";

var MAX_ORG = $('input[name="md_responsible_party_name[]"]').length;
var org_count = 1;

function addOrganisation() {
   // disable the remove button in last visible div block
   if( org_count > 1 ) {
      var remove_btn = "#responsible_organisation" + org_count + "_remove";
      $(remove_btn).prop('disabled', true);
      $(remove_btn).prop('class', 'btn btn-default');
      $(remove_btn).hide();
   }

   // increment
   org_count++;

   // show this div block
   var next_div_id = "responsible_organisation" + org_count;
   $('#' + next_div_id).show();

   // disable the add button if max count reached
   if( org_count >= MAX_ORG )
       $('#responsible_organisation1_add').prop('disabled', true);

   make_responsible_organisation_json();
}

function removeOrganisation(id) {
   // hide this div block
   var element_id = "responsible_organisation" + id;
   $('#' + element_id).hide();

   // enable the add button
   $('#responsible_organisation1_add').prop('disabled', false);

   // enable the remove button in previous div block
   if( org_count > 1 ) {
      var remove_btn = "#responsible_organisation" + (id-1) + "_remove";
      $(remove_btn).prop('disabled', false);
      $(remove_btn).prop('class', 'btn btn-danger');
      $(remove_btn).show();
   }

   // decrement
   org_count--;
 
   make_responsible_organisation_json();
}


function make_responsible_organisation_json() {
    var org_dict = new Array();
    var json = "";
    var count = 0;
    for (var i=0; i < MAX_ORG; i++) {
        // if this div id is visible, process
        var div_id = "responsible_organisation" + (i+1);
        if( $('#' + div_id).is(':visible') ) {
            var organisation = $('input[name="md_responsible_party_name[]"]')[i].value;
            var email = $('input[name="md_responsible_party_email[]"]')[i].value;
            if( organisation === "" && email === "" ) {
                // no form values for this organisation, continue to next
                continue;
            }

            // process form values into JSON
            org_dict[count] = {};
            org_dict[count]["organisation"] = organisation;
            org_dict[count]["email"] = email;
            org_dict[count]["role"] = $('select[name="md_responsible_party_role[]"]')[i].value;
            count++;
        }
    }
    // set hidden form input with responsible organisations in a json encoding
    json = JSON.stringify(org_dict);
    $('#field-md_responsible_organisations').val(json);
}


// manage responsible organisations - init
ckan.module('responsible_organisations', function ($, _) {
    return {
        initialize: function () {

            // process legacy organisation data, if any...
            var legacy_organisation = $('input[name="md_responsible_party_name[]"]')[0].value
            var legacy_email = $('input[name="md_responsible_party_email[]"]')[0].value
            var legacy_role = $('select[name="md_responsible_party_role[]"]')[0].value
            for (var i=0; i < MAX_ORG; i++) {
                $('input[name="md_responsible_party_name[]"]')[i].value = "";
                $('input[name="md_responsible_party_email[]"]')[i].value = "";
                $('select[name="md_responsible_party_role[]"]')[i].value = "Point of Contact";
            }
            if( legacy_organisation )
                $('input[name="md_responsible_party_name[]"]')[0].value = legacy_organisation;
            if( legacy_email )
                $('input[name="md_responsible_party_email[]"]')[0].value = legacy_email;
            if( legacy_role.trim() )
                $('select[name="md_responsible_party_role[]"]')[0].value = legacy_role;
            // ... legacy processed

            // get empty select tag element
            var responsible_organisations_json = $('#field-md_responsible_organisations').val();
            var responsible_organisations_dict = null;
            try {
                responsible_organisations_dict = JSON.parse(responsible_organisations_json);
            } catch (e) {
                // do not process
                responsible_organisations_dict = null
            }

            if( responsible_organisations_dict ) {
                for (var i=0; i < responsible_organisations_dict.length; i++){
                    var organisation = responsible_organisations_dict[i].organisation;
                    var email = responsible_organisations_dict[i].email;
                    var role = responsible_organisations_dict[i].role;

                    $('input[name="md_responsible_party_name[]"]')[i].value = organisation;
                    $('input[name="md_responsible_party_email[]"]')[i].value = email;
                    if( organisation === "" && email === "" )
                        $('select[name="md_responsible_party_role[]"]')[i].value = "Point of Contact"
                    else
                        $('select[name="md_responsible_party_role[]"]')[i].value = role;
                    if( i > 0 )
                        addOrganisation();
                }
            }

            make_responsible_organisation_json(); // update json data field, required for the legacy data
        }
    };
});

// manage responsible organisations - on change
ckan.module('responsible_organisations_change', function ($, _) {
    return {
        initialize: function () {
            // register for onChange event for the select options list
            var delegated = this.el;
            this.el.on('change', delegated, this._onChange);
        },
        _onChange: function (event) {
            make_responsible_organisation_json();
        }
    };
});

