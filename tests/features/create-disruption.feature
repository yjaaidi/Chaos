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

    Scenario: We can create a disruption with a publication_period
        When I post to "/disruptions" with:
        """
        {"reference": "foo", "publication_period": {"begin": "2014-06-24T10:35:00Z", "end": "2014-06-24T23:59:59Z"}}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "disruption.reference" should be "foo"
        And the field "disruption.note" should be null
        And the field "disruption.publication_period.begin" should be "2014-06-24T10:35:00Z"
        And the field "disruption.publication_period.end" should be "2014-06-24T23:59:59Z"

    Scenario: Publication period must be complete
        When I post to "/disruptions" with:
        """
        {"reference": "foo", "publication_period": {"begin": "2014-06-24T10:35:00Z"}}
        """
        Then the status code should be "400"
        And the header "Content-Type" should be "application/json"

    Scenario: We can create a disruption with a publication_period
        When I post to "/disruptions" with:
        """
        {"reference": "foo", "publication_period": {"begin": "2014-06-24T10:35:00Z", "end": "2014-06-24T23:59:59Z"}}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "disruption.reference" should be "foo"
        And the field "disruption.note" should be null
        And the field "disruption.publication_period.begin" should be "2014-06-24T10:35:00Z"
        And the field "disruption.publication_period.end" should be "2014-06-24T23:59:59Z"

    Scenario: Disruption are created with publication_period
        Given I post to "/disruptions" with:
        """
        {"reference": "foo", "publication_period": {"begin": "2014-06-24T10:35:00Z", "end": "2014-06-24T23:59:59Z"}}
        """
        When I get "/disruptions"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "disruptions.0.reference" should be "foo"
        And the field "disruptions.0.publication_period.begin" should be "2014-06-24T10:35:00Z"
        And the field "disruptions.0.publication_period.end" should be "2014-06-24T23:59:59Z"

    Scenario: We can create a disruption with a end_publication_date null
        When I post to "/disruptions" with:
        """
        {"reference": "foo", "publication_period": {"begin": "2014-06-24T10:35:00Z", "end": null}}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "disruption.reference" should be "foo"
        And the field "disruption.note" should be null
        And the field "disruption.publication_period.begin" should be "2014-06-24T10:35:00Z"
        And the field "disruption.publication_period.end" should be null
