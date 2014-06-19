Feature: Create disruption

    Scenario: Reference is required
        When I Post to "/disruptions"
        Then the status code should be "400"

    Scenario: creation of disruption
        Given I provide this json:
        """
        {"reference": "foo"}
        """
        And I set the header "Content-type" to "application/json"
        When I Post to "/disruptions"
        Then the status code should be "201"
        And the header "Content-Type" should contain the value "application/json"
        And the field "disruption.reference" should contain the value "foo"
        And the field "disruption.note" should be null
