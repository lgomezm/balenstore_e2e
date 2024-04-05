from base_e2e import BaseE2ETest


class TestCreateVisit(BaseE2ETest):
    def test_login_and_logout(self):
        self.input_text(test_id="login-email", text="luis@test.com")
        self.input_text(test_id="login-password", text="password")
        self.click_button(test_id="login-button")

        self.assert_contains_text(test_id="nav-brand", text="Antique Store")

        self.click_button(test_id="logout-button")
        self.assert_visible("login-title")
        self.assert_contains_text(test_id="login-title", text="Log in")

    def test_create_visit(self):
        # Login pathway
        self.input_text(test_id="login-email", text="luis@test.com")
        self.input_text(test_id="login-password", text="password")
        self.click_button(test_id="login-button")

        # Go to Quotation Visits view
        self.click_button(test_id="visits-link")

        # Click 'New Quotation Visit' button
        self.click_button(test_id="new-visit-button")

        # Provide data to create a quotation visit
        self.input_text(test_id="visit-name", text="E2E Visit")
        self.input_text(test_id="visit-address-1", text="333 Michigan St NE")
        self.input_text(test_id="visit-city", text="Grand Rapids")
        self.select_option_value(test_id="visit-state", value="MI")
        self.input_text(test_id="visit-zip", text="49503")
        self.click_button(test_id="visit-submit-button")

        # Validate success modal is displayed and contains expected text
        self.assert_modal_contains(
            modal_test_id="visit-success-modal",
            title="Success!",
            body="The quotation visit has been created. It will be reviewed soon!",
        )
