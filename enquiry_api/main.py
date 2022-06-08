import json
from datetime import datetime
from datetime import timedelta
import pytest
import requests

bearer = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiI2YmY3MDczYy00ZmZmLTQ0OTAtODI4NS04Yjk2YTVjMWZhZWMiLCJzdWIiOiIwNDI4NTM5Zi1hMmZkLTRiZjUtOTM3OS0zYmYwOGRjMDFhNjMiLCJ1bmlxdWVfbmFtZSI6ImFkbWluQHN3aW5nZXJzdGVzdC5vbm1pY3Jvc29mdC5jb20iLCJlbWFpbCI6ImFkbWluQHN3aW5nZXJzdGVzdC5vbm1pY3Jvc29mdC5jb20iLCJnaXZlbl9uYW1lIjoiU3VwZXIiLCJmYW1pbHlfbmFtZSI6IkFkbWluIiwicGljdHVyZSI6IiIsInRpbWVfem9uZSI6IlBhY2lmaWMvVG9uZ2F0YXB1IiwidXBkYXRlZF9hdCI6IjE2NTQ2MDI4MjciLCJyb2xlIjoie1wibmFtZVwiOlwiU3VwZXIgQWRtaW5cIixcInBlcm1pc3Npb25zXCI6WzEsMiwzLDQsNSw2LDcsOCw5LDEwLDExLDEyLDEzLDE0LDE1LDE2LDE3LDE4LDE5LDIwLDIxLDIyLDIzLDI1LDI2LDI3LDI4LDI5LDMwLDMxLDMyLDMzLDM0LDM1LDM2LDM3LDM4LDM5LDQwLDQxLDQyLDQzLDQ0LDQ1LDQ2LDQ3LDQ4LDQ5LDUwLDUxLDUyLDUzLDU0LDU1LDU2LDU3LDU4LDU5LDYwLDYxLDYyLDYzLDY0LDY1LDY2LDY3LDY4LDY5LDcwLDcxLDcyLDczLDc0LDc1LDc2LDc3LDc4LDc5LDgwLDgxLDgyLDgzLDg0LDg1LDg2XSxcInZhbGlkaXR5VHlwZVwiOjAsXCJzdGFydERhdGVWYWxpZGl0eVwiOm51bGwsXCJlbmREYXRlVmFsaWRpdHlcIjpudWxsLFwiZGF5c09mV2Vla1ZhbGlkaXR5XCI6W10sXCJkYXRlc1ZhbGlkaXR5XCI6W10sXCJtb2RpZmllZEF0XCI6XCIyMDIyLTA0LTIwVDA4OjAyOjQ0LjQ2NzYwMDMrMDA6MDBcIixcImlkXCI6XCI2YjE0Nzc2ZC0zMzNhLTQxOTMtYmFiYS0wOGQ4M2FhYWI2OWNcIn0iLCJhcmVhIjoie1widHlwZVwiOjAsXCJuYW1lXCI6XCJHbG9iYWxcIixcImlkXCI6XCIwMWJiMjI4MS04MmFjLTRkODgtODNlMi0yODNmZGExOTE3NjNcIn0iLCJuYmYiOjE2NTQ2MDI4NjcsImV4cCI6MTY1NDYwNjQ2NywiaWF0IjoxNjU0NjAyODY3LCJpc3MiOiJodHRwczovL3N3aW5nZXJzLWNybS1hcGktcWEuYXp1cmV3ZWJzaXRlcy5uZXQvIiwiYXVkIjoiU3dpbmdlcnNDUk1BdWRpZW5jZSJ9.E64GoHAaQdt35yl4mRVn1wyR4MUaLp_wwDcQxl0XGR_82FmOIIvLomhmulOTA46UnfDKEWB0z3w2d-lq7YI2wbycK8Ppf43O_i4P0SiaD8AZLppTLbtAZbjz6-dVXbHmE6xwg3KDGqO4l68Llh1rSJj0rYo5z3Wa9Qk1AF217B4CLZmXZHjp9juxQWtVFkRyW-Y8_hO6AsscUBSeyqNJdJEdZjoHNP7gcN_LWiRWW1w7qwSunmapqZrrDJxWQf4l-wMJiyAjlf3QcmpJOOVhETNOxBWBQehCn-ImA9A2UAjjZgnu12mQc-jVEJRXvEq_nCchW3k65IgZOArTChGzOw"

headers = {
    'Accept': '*/*',
    'Content-Type': 'application/json',
    'authorization': bearer
}


class TestEnquiry:
    last_enquiry = json.load(open("last_enquiry.json", "r"))
    reference_number = last_enquiry["referenceNumber"]
    booking_id = last_enquiry["bookingId"]
    basket_id = last_enquiry["basketId"]
    main_id = last_enquiry["id"]
    payment_id = last_enquiry["payment_id"]
    beo_id = last_enquiry["beo_id"]
    day = "2022-06-14"
    date = datetime.strptime(f"{day} 17:05:00", "%Y-%m-%d %H:%M:%S")
    op_date = f"{day}T00:00:00"

    @staticmethod
    def format_date(date):
        return str(date).replace(" ", "T") + ".000Z"

    @staticmethod
    def save_last_enquiry(response, element=""):
        with open("last_enquiry.json", "r+") as last_enquiry:
            enquiry = json.load(last_enquiry)
            print(enquiry)
            if element:
                pass
            else:
                enquiry["referenceNumber"] = TestEnquiry.reference_number = response["referenceNumber"]
                enquiry["bookingId"] = TestEnquiry.basket_id = response["bookingId"]
                enquiry["basketId"] = TestEnquiry.booking_id = response["basketId"]
                enquiry["id"] = TestEnquiry.main_id = response["id"]

            last_enquiry.seek(0)
            last_enquiry.truncate(0)
            last_enquiry.write(json.dumps(enquiry))

    def test_create_inquiry(self):
        url = "https://swingers-crm-api-qa.azurewebsites.net/api/Inquiries"
        payload = json.dumps(json.load(open("payloads/inquiries.json", "r")))
        response = requests.post(url=url, headers=headers, data=payload)

        assert response.status_code == 200

        self.save_last_enquiry(response.json())
        print(response.text)
        print(TestEnquiry.reference_number)
        print(TestEnquiry.booking_id)
        print(TestEnquiry.basket_id)
        print(TestEnquiry.main_id)

    def test_requirements(self):
        url = f"https://swingers-crm-api-qa.azurewebsites.net/api/Inquiries/{TestEnquiry.main_id}"
        payload = json.load(open("payloads/requirements.json", "r"))
        payload["referenceNumber"] = TestEnquiry.reference_number
        payload["bookingId"] = TestEnquiry.booking_id
        payload["basketId"] = TestEnquiry.basket_id
        payload["id"] = TestEnquiry.main_id
        payload = json.dumps(payload)
        response = requests.put(url=url, headers=headers, data=payload)

        assert response.status_code == 200
        print(response.text)

    def test_schedule_space(self):
        url = "https://swingers-crm-api-qa.azurewebsites.net/api/Bookings/SchedulerReservationChangeAsync"

        payload = json.load(open("payloads/space.json", "r"))
        payload["bookingId"] = TestEnquiry.booking_id
        payload["reservations"][0]["bookingId"] = TestEnquiry.booking_id
        payload["reservations"][0]["operationalDate"] = TestEnquiry.op_date
        payload["reservations"][0]["start"] = self.format_date(TestEnquiry.date)
        payload["reservations"][0]["end"] = self.format_date(TestEnquiry.date + timedelta(minutes=20))
        payload["reservations"][0]["frontBufferStart"] = self.format_date(TestEnquiry.date - timedelta(minutes=5))
        payload["reservations"][0]["frontBufferEnd"] = self.format_date(TestEnquiry.date)
        payload["reservations"][0]["backBufferStart"] = self.format_date(TestEnquiry.date + timedelta(minutes=20))
        payload["reservations"][0]["backBufferEnd"] = self.format_date(TestEnquiry.date + timedelta(minutes=25))
        payload["inquiry"]["id"] = TestEnquiry.main_id
        payload = json.dumps(payload)

        response = requests.post(url=url, headers=headers, data=payload)

        print(response.text)
        assert response.status_code == 200


    def test_schedule_golf(self):
        url = "https://swingers-crm-api-qa.azurewebsites.net/api/Bookings/GolfCalendarReservationChangeAsync"

        payload = json.load(open("payloads/golf.json", "r"))
        payload["firstRound"]["bookingId"] = TestEnquiry.booking_id
        payload["firstRound"]["operationalDate"] = TestEnquiry.op_date
        payload["firstRound"]["start"] = self.format_date(TestEnquiry.date)
        payload["firstRound"]["end"] = self.format_date(TestEnquiry.date + timedelta(minutes=20))
        payload["firstRound"]["frontBufferStart"] = self.format_date(TestEnquiry.date - timedelta(minutes=5))
        payload["firstRound"]["backBufferEnd"] = self.format_date(TestEnquiry.date + timedelta(minutes=25))
        payload["inquiry"]["id"] = TestEnquiry.main_id
        payload = json.dumps(payload)

        response = requests.post(url=url, headers=headers, data=payload)

        assert response.status_code == 200
        print(response.text)

    def test_package(self):
        url = f"https://swingers-crm-api-qa.azurewebsites.net/api/Bookings/{TestEnquiry.booking_id}"
        payload = json.load(open("payloads/package.json", "r"))
        payload["id"] = TestEnquiry.booking_id
        payload["bookingId"] = TestEnquiry.booking_id
        payload["operationalDate"] = TestEnquiry.op_date
        payload = json.dumps(payload)
        response = requests.put(url=url, headers=headers, data=payload)

        TestEnquiry.beo_id = response.json()["beoId"]
        print(response.text)
        self.test_requirements()
        assert response.status_code == 200

    def test_payment(self):
        url = "https://swingers-crm-api-qa.azurewebsites.net/api/Payments"
        payload = json.load(open("payloads/payment.json", "r"))
        payload["bookingId"] = TestEnquiry.booking_id
        payload["dueDate"] = TestEnquiry.op_date
        payload = json.dumps(payload)
        response = requests.post(url=url, headers=headers, data=payload)

        print(response.text)
        TestEnquiry.payment_id = response.json()["id"]
        assert response.status_code == 200

    def test_overwrite(self):
        url = "https://swingers-crm-api-qa.azurewebsites.net/api/Payments/Overwrite"
        payload = json.dumps({"reason": "test", "id": TestEnquiry.payment_id})
        response = requests.put(url=url, headers=headers, data=payload)

        print(response.text)
        assert response.status_code == 200

    def test_sent_to_client(self):
        url = f"https://swingers-crm-api-qa.azurewebsites.net/api/Bookings/SendToClientAsync/{TestEnquiry.main_id}"
        payload = json.load(open("payloads/sent_to_client.json", "r"))
        payload["id"] = TestEnquiry.booking_id
        payload["operationalDate"] = TestEnquiry.op_date
        payload["beoId"] = TestEnquiry.beo_id
        payload = json.dumps(payload)
        response = requests.put(url=url, headers=headers, data=payload)
        print(payload)
        print(response.text)
        assert response.status_code == 200
