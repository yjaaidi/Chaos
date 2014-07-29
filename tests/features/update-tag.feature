Feature: update tag

    Scenario: the Tag must exist
        When I put to "/tags/7ffab230-3d48-4eea-aa2c-22f8680230b6" with:
        """
        {"wording": "foo"}
        """
        Then the status code should be "404"

    Scenario: a tag must have a wording
        Given I have the following tags in my database:
            | wording   | created_at          | updated_at          | is_visible | id                                   |
            | weather   | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |
            | strike    | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | False      | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |
        When I put to "/tags/7ffab230-3d48-4eea-aa2c-22f8680230b6" with:
        """
        {}
        """
        Then the status code should be "400"
        And the header "Content-Type" should be "application/json"

    Scenario: I can update the wording of a tag
        Given I have the following tags in my database:
            | wording   | created_at          | updated_at          | is_visible | id                                   |
            | weather   | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | True       | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |
            | strike    | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | False      | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |
        When I put to "/tags/7ffab230-3d48-4eea-aa2c-22f8680230b6" with:
        """
        {"wording": "foo"}
        """
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "tag.wording" should be "foo"


    Scenario: I can't update a invisible tag
        Given I have the following tags in my database:
            | wording   | created_at          | updated_at          | is_visible | id                                   |
            | weather   | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | False      | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |
        When I put to "/tags/7ffab230-3d48-4eea-aa2c-22f8680230b6" with:
        """
        {"wording": "foo"}
        """
        Then the status code should be "404"
        And the header "Content-Type" should be "application/json"
