Feature: update severity

    Scenario: the Severity must exist
        When I put to "/severities/7ffab230-3d48-4eea-aa2c-22f8680230b6" with:
        """
        {"wording": "foo"}
        """
        Then the status code should be "404"

    Scenario: a severity must have a wording
        Given I have the following severities in my database:
            | wording   | color   | created_at          | updated_at          | is_visible | id                                   |
            | blocking  | #123456 | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |
            | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | False      | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |
        When I put to "/severities/7ffab230-3d48-4eea-aa2c-22f8680230b6" with:
        """
        {"color": "foo"}
        """
        Then the status code should be "400"
        And the header "Content-Type" should be "application/json"

    Scenario: I can update the wording of a severity
        Given I have the following severities in my database:
            | wording   | color   | created_at          | updated_at          | is_visible | id                                   |
            | blocking  | #123456 | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |
            | good news | #654321 | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | False      | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |
        When I put to "/severities/7ffab230-3d48-4eea-aa2c-22f8680230b6" with:
        """
        {"wording": "foo", "color": "blue"}
        """
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "severity.wording" should be "foo"
        And the field "severity.color" should be "blue"

    Scenario: I can't update a invisible severity
        Given I have the following severities in my database:
            | wording   | color   | created_at          | updated_at          | is_visible | id                                   |
            | blocking  | #123456 | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | False      | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |
        When I put to "/severities/7ffab230-3d48-4eea-aa2c-22f8680230b6" with:
        """
        {"wording": "foo"}
        """
        Then the status code should be "404"
        And the header "Content-Type" should be "application/json"
