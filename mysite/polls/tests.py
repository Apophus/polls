from django.test import LiveServerTestCase
from selenium import webdriver

class PollsTest(LiveServerTestCase):

	def setUp(self):
		self.driver = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_create_new_poll_via_admin_site(self):
		"kilel opens web browser and goes to admin page"
		self.browser.get(self.live_server_url + '/admin')

		#he sees the farmiliar 'Django administration' heading
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Django administration', body.text)

		#TODO: use admin site to create a Poll
		self.fail('finish this test')