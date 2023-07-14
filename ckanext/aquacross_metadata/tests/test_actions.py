import pytest

from ckan.tests import factories, helpers


@pytest.mark.usefixtures("clean_db")
def test_organization_list_does_not_return_qc():

    factories.Organization(name="qc")
    factories.Organization(name="myorg1")
    factories.Organization(name="myorg2")

    org_list = helpers.call_action("organization_list")

    assert len(org_list) == 2
    assert "qc" not in org_list

    org_list = helpers.call_action("organization_list", all_fields=True)

    assert len(org_list) == 2
    assert "qc" not in [org["name"] for org in org_list]
