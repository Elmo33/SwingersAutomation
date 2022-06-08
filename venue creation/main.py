import json
import requests
from variables import Vars
import pytest
from datetime import datetime

bearer = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiJiNDE3YTIxMC1jNWNlLTQyMjMtYmIwYi0wMzYxODU5YWNjYzEiLCJzdWIiOiIwNDI4NTM5Zi1hMmZkLTRiZjUtOTM3OS0zYmYwOGRjMDFhNjMiLCJ1bmlxdWVfbmFtZSI6ImFkbWluQHN3aW5nZXJzdGVzdC5vbm1pY3Jvc29mdC5jb20iLCJlbWFpbCI6ImFkbWluQHN3aW5nZXJzdGVzdC5vbm1pY3Jvc29mdC5jb20iLCJnaXZlbl9uYW1lIjoiU3VwZXIiLCJmYW1pbHlfbmFtZSI6IkFkbWluIiwicGljdHVyZSI6IiIsInRpbWVfem9uZSI6IlBhY2lmaWMvVG9uZ2F0YXB1IiwidXBkYXRlZF9hdCI6IjE2NTQ2MDc1OTMiLCJyb2xlIjoie1wibmFtZVwiOlwiU3VwZXIgQWRtaW5cIixcInBlcm1pc3Npb25zXCI6WzEsMiwzLDQsNSw2LDcsOCw5LDEwLDExLDEyLDEzLDE0LDE1LDE2LDE3LDE4LDE5LDIwLDIxLDIyLDIzLDI1LDI2LDI3LDI4LDI5LDMwLDMxLDMyLDMzLDM0LDM1LDM2LDM3LDM4LDM5LDQwLDQxLDQyLDQzLDQ0LDQ1LDQ2LDQ3LDQ4LDQ5LDUwLDUxLDUyLDUzLDU0LDU1LDU2LDU3LDU4LDU5LDYwLDYxLDYyLDYzLDY0LDY1LDY2LDY3LDY4LDY5LDcwLDcxLDcyLDczLDc0LDc1LDc2LDc3LDc4LDc5LDgwLDgxLDgyLDgzLDg0LDg1LDg2XSxcInZhbGlkaXR5VHlwZVwiOjAsXCJzdGFydERhdGVWYWxpZGl0eVwiOm51bGwsXCJlbmREYXRlVmFsaWRpdHlcIjpudWxsLFwiZGF5c09mV2Vla1ZhbGlkaXR5XCI6W10sXCJkYXRlc1ZhbGlkaXR5XCI6W10sXCJtb2RpZmllZEF0XCI6XCIyMDIyLTA0LTIwVDA4OjAyOjQ0LjQ2NzYwMDMrMDA6MDBcIixcImlkXCI6XCI2YjE0Nzc2ZC0zMzNhLTQxOTMtYmFiYS0wOGQ4M2FhYWI2OWNcIn0iLCJhcmVhIjoie1widHlwZVwiOjAsXCJuYW1lXCI6XCJHbG9iYWxcIixcImlkXCI6XCIwMWJiMjI4MS04MmFjLTRkODgtODNlMi0yODNmZGExOTE3NjNcIn0iLCJuYmYiOjE2NTQ2MDc2MTcsImV4cCI6MTY1NDYxMTIxNiwiaWF0IjoxNjU0NjA3NjE3LCJpc3MiOiJodHRwczovL3N3aW5nZXJzLWNybS1hcGktcWEuYXp1cmV3ZWJzaXRlcy5uZXQvIiwiYXVkIjoiU3dpbmdlcnNDUk1BdWRpZW5jZSJ9.ZW5SKZp0ll8UkvFlOric2TrSU42KEdoiKsUdS6szfgTp1ujZc2uxSAn-lwtyseY9qFsi8jCxfYglXFb7BuucZzztJ-dnj_GokqfYrThM-eT9Ocq-gfaSNo4BmMJbjl4bQxzt1qxcrt9vIH15UkVVIBsRV3VpGLb7auxDGoo-7xJt7bGvoN6uI3WAATWKhJYphugaZTCZsIogCHsL1KIZOspDWumTtWv2Ip8oSgVAJ-0I7gejpmgD3pGK5Ig2BhEEbawU0yTC9YEN9CMkK2BPJ7-v0zV2ya9ABAvsp_d_2yLOHk16AYP0wZhNqy92V_xlmoiFc4PG8m-f9QCZgQExmg"


class TestVenue:
    venue_id = "38cfd187-f197-4ef5-a135-f2332f066da3"
    venue_area_id = "38cfd187-f197-4ef5-a135-f2332f066da3"
    space_config_id = "87993ecc-b143-49c7-ce54-08da488628aa"
    today = datetime.now().strftime("%Y-%m-%d") + "T00:00:00"
    headers = {
        'Accept': '*/*',
        'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundaryYlvo4TgjRisqHV2S',
        'authorization': bearer
    }

    def test_create_venue(self):
        TestVenue.headers['Content-Type'] = 'multipart/form-data; boundary=----WebKitFormBoundaryYlvo4TgjRisqHV2S'
        venue_url = "https://swingers-crm-api-qa.azurewebsites.net/api/Venues"
        venue_name = "DEBUG 1"
        code = "20001"
        response = requests.post(url=venue_url, data=Vars.venue_payload(venue_name, code), headers=TestVenue.headers)

        print()
        print(response.text)
        assert response.status_code == 200

        TestVenue.venue_id = response.json()["id"]

    def test_create_space_config(self):
        TestVenue.headers['Content-Type'] = 'application/json'
        url = "https://swingers-crm-api-qa.azurewebsites.net/api/EventSpaceConfigs"
        payload = json.load(open("payloads/space_config.json", "r"))
        payload["venueId"] = TestVenue.venue_id
        payload["startDate"] = TestVenue.today
        payload = json.dumps(payload)

        response = requests.post(url=url, data=payload, headers=TestVenue.headers)

        print(response.text)
        assert response.status_code == 200

    def test_apply_space_config(self):
        TestVenue.headers['Content-Type'] = 'application/json'
        url = f"https://swingers-crm-api-qa.azurewebsites.net/api/EventSpaceConfigs/{TestVenue.venue_id}"
        payload = json.load(open("payloads/apply_space_config.json", "r"))
        payload["venueId"] = TestVenue.venue_id
        payload["startDate"] = TestVenue.today
        payload["status"] = 1
        payload["rootEventSpace"]["maximumSeatedCapacity"] = 100
        payload["rootEventSpace"]["maximumCapacity"] = 100
        payload["venueAreaId"] = TestVenue.venue_id
        payload["id"] = TestVenue.space_config_id
        payload = json.dumps(payload)

        response = requests.put(url=url, data=payload, headers=TestVenue.headers)
        print(payload)
        print(response.text)
        assert response.status_code == 200

    def test_create_golf(self):
        TestVenue.headers['Content-Type'] = 'multipart/form-data; boundary=----WebKitFormBoundarypXFFgqowibovAUgp'
        payload = Vars.golf_payload(TestVenue.venue_id, TestVenue.today, "golf 3")

        url = "https://swingers-crm-api-qa.azurewebsites.net/api/GolfCourses"

        response = requests.post(url=url, data=payload, headers=TestVenue.headers)

        print(response.text)
        assert response.status_code == 200

    @pytest.mark.skip(reason="not ready")
    def test_create_space(self):
        space_url = "https://swingers-crm-api-qa.azurewebsites.net/api/EventSpaces/db9c59d5-689b-4425-2534-08da327736f9"

    @pytest.mark.skip(reason="not ready")
    def test_create_product(self):
        TestVenue.headers['Content-Type'] = 'multipart/form-data; boundary=----WebKitFormBoundaryzuiKAVLPu3NqbywJ'
        url = "https://swingers-crm-api-qa.azurewebsites.net/api/ProductConfig"

        # ------------------------ golf ------------------------
        payload = Vars.product_payload("epic golf", TestVenue.today, "0e4a7ad4-d779-430f-6bbe-08da3980802c")

        response = requests.post(url=url, data=payload, headers=TestVenue.headers)

        product_id = response.json()["productId"]
        print(product_id)
        print(response.text)
        print(response.status_code)

        # ------------------------ space ------------------------
        payload = Vars.product_payload("epic space", TestVenue.today, "57f4f93f-bbb2-4412-6bbf-08da3980802c")

        response = requests.post(url=url, data=payload, headers=TestVenue.headers)

        product_id = response.json()["productId"]
        print(product_id)
        print(response.text)
        print(response.status_code)

    @pytest.mark.skip(reason="not ready")
    def test_create_package(self):
        TestVenue.headers['Content-Type'] = 'multipart/form-data; boundary=----WebKitFormBoundary9AZNgnbwC7ADHvCf'
        url = "https://swingers-crm-api-qa.azurewebsites.net/api/PackageConfigs"
        payload = Vars.package_payload("auto package1", TestVenue.today, "a80933a1-57a4-46a0-c31b-08da3d59c33d",
                                       "446f9883-cfc1-4921-c31c-08da3d59c33d", "a")
        response = requests.post(url=url, data=payload, headers=TestVenue.headers)
        print(response.status_code)
        print(json.dumps(response.json(), indent=4, sort_keys=True))

    def test_business_organization(self):
        url = "https://swingers-crm-api-qa.azurewebsites.net/api/BusinessOrganizations"
        payload = json.load(open("payloads/sent_to_client.json", "r"))
        payload["id"] = TestVenue.booking_id
        payload["operationalDate"] = TestVenue.op_date
        payload["beoId"] = TestVenue.beo_id
        payload = json.dumps(payload)
