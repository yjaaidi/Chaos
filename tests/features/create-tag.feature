Feature: Create tag

    Scenario: wording is required
        When I post to "/tags"
        Then the status code should be "400"

    Scenario: creation of tag
        When I post to "/tags" with:
        """
        {"name": "foo"}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "tag.name" should be "foo"

    Scenario: Tag are created
        Given I post to "/tags" with:
        """
        {"name": "foo"}
        """
        When I get "/tags"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "tags" should have a size of 1
        And the field "tags.0.name" should be "foo"

    Scenario: Tag doublon
        Given I post to "/tags" with:
        """
        {"name": "foo"}
        """
        Given I post to "/tags" with:
        """
        {"name": "foo"}
        """
        Then the status code should be "400"
        And the header "Content-Type" should be "application/json"

