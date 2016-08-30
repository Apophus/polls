from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PollsTest(LiveServerTestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_create_new_poll_via_admin_site(self):
		#kilel opens web browser and goes to admin page"
		self.browser.get(self.live_server_url + '/admin/')

		#he sees the farmiliar 'Django administration' heading
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Django administration', body.text)

		#types in username and password and hits return
		username_field = self.browser.find_element_by_name('username')
		username_field.send_keys('larrisa')

		password_field = self.browser.find_element_by_name('password')
		password_field.send_keys('hkilel07')
		password_field.send_keys(Keys.RETURN)

		#username and password are accepted and 
		#redirected to admin page
		body = self.browser.find_element_by_tag_name('body')
		self.assertIn('Site administration', body.text)

		#check if there's a hyperlink called polls
		polls_links = self.browser.find_element_by_link_text('Polls')
		self.assertEquals(len(polls_links), 2)

		#TODO: use admin site to create a Poll
		self.fail('finish this test')