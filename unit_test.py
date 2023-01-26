import unittest


# def power_on_kiosk():
#     print('Powering on the check-in kiosk...')


# def return_to_welcome_page():
#     print('Returning check-in kiosk to Welcome Page')


# def power_off_kiosk():
#     print('Powering off the check-in kiosk...')

# class CheckInKioskTests(unittest.TestCase):

#   def test_check_in_with_flight_number(self):
#     print('Testing the check-in process based on flight number')

#   def test_check_in_with_passport(self):
#     print('Testing the check-in process based on passport')

#   # Write your code below:

#   @classmethod
#   def setUpClass(cls):
#     power_on_kiosk()

#   @classmethod
#   def tearDownClass(cls):
#     power_off_kiosk()

#   def setUp(self):
#     return_to_welcome_page()


# unittest.main()


# import sys


# class LinuxTests(unittest.TestCase):

#     @unittest.skipUnless(sys.platform.startswith("win"), "This test only runs on Linux")
#     def test_linux_feature(self):
#         print("This test should only run on win")

#     @unittest.skipIf(not sys.platform.startswith("win"), "This test only runs on Linux")
#     def test_other_linux_feature(self):
#         print("This test should only run on Windows")


# def regional_jet():
#     print('This is a regional jet...')
#     return True


# def get_daily_movie():
#     print('Retrieving the movie set to play on today\'s flight...')
#     return 'Parasite'


# def get_licensed_movies():
#     print('Retrieving the list of licenses movies from the database...')
#     licensed_movies = ['Parasite', 'Nomadland', 'Roma']
#     return licensed_movies


# def get_wifi_status():
#     print('Checking WiFi signal...')
#     print('WiFi is active')
#     return True


# def get_device_temp():
#     print('Reading the temperature of the entertainment system device...')
#     return 33.2


# def get_maximum_display_brightness():
#     print('Calculating maximum display brightness in nits...')
#     return 399.99999999


# class EntertainmentSystemTests(unittest.TestCase):

#     @unittest.skipIf(regional_jet(), 'Not available on regional jets')
#     def test_movie_license(self):
#         daily_movie = get_daily_movie()
#         licensed_movies = get_licensed_movies()
#         self.assertIn(daily_movie, licensed_movies)

#     @unittest.skipUnless(regional_jet() is False, 'Not available on regional jets')
#     def test_wifi_status(self):
#         wifi_enabled = get_wifi_status()
#         self.assertTrue(wifi_enabled)

#     def test_device_temperature(self):
#         if regional_jet():
#             self.skipTest('Not available on regional jets')

#         device_temp = get_device_temp()
#         self.assertLess(device_temp, 35)

#     def test_maximum_display_brightness(self):
#         if regional_jet():
#             self.skipTest('Not available on regional jets')

#         brightness = get_maximum_display_brightness()
#         self.assertAlmostEqual(brightness, 400)


# unittest.main()


# unittest.main()


########################### Expected Failures ###########################


