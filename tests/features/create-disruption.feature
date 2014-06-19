Feature: Create disruption

    Scenario: Reference is required
        When I post to "/disruptions"
        Then the status code should be "400"

    Scenario: creation of disruption
        When I post to "/disruptions" with:
        """
        {"reference": "foo"}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "disruption.reference" should be "foo"
        And the field "disruption.note" should be null

    Scenario: Disruption are created
        Given I post to "/disruptions" with:
        """
        {"reference": "foo", "note": "hello"}
        """
        When I get "/disruptions"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "disruptions" should have a size of 1
        And the field "disruptions.0.reference" should be "foo"
        And the field "disruptions.0.note" should be "hello"
