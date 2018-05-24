Feature: Example REST API
Scenario: Test weather api
		Given the API at the URL "http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=1677fe49fafb9c9d7700bdd796263189"
		When I send a GET request
		Then a 200 status code should be returned

