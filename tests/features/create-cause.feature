Feature: Create cause

    Scenario: wording is required
        When I post to "/causes"
        Then the status code should be "400"

    Scenario: creation of cause
        When I post to "/causes" with:
        """
        {"wording": "foo"}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "cause.wording" should be "foo"

    Scenario: Cause are created
        Given I post to "/causes" with:
        """
        {"wording": "foo"}
        """
        When I get "/causes"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "causes" should have a size of 1
        And the field "causes.0.wording" should be "foo"
