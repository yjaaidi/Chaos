Feature: Create severity

    Scenario: we cannot create severity without client
        When I post to "/severities" with:
        """
        {"wordings": [{"key": "test", "value": "foo"}]}
        """
        Then the status code should be "400"

    Scenario: wordings is required
    I fill in header "X-Customer-Id" with "5"
        When I post to "/severities"
        Then the status code should be "400"


    Scenario: creation of severity
        I fill in header "X-Customer-Id" with "5"
        When I post to "/severities" with:
        """
        {"wordings": [{"key": "test", "value": "foo"}]}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "severity.wordings.0.key" should be "test"
        And the field "severity.wordings.0.value" should be "foo"
        And the field "severity.color" should be null

    Scenario: Severity are created
        I fill in header "X-Customer-Id" with "5"
        Given I post to "/severities" with:
        """
        {"wordings": [{"key": "test", "value": "foo"}]}
        """
        When I get "/severities"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "severities" should have a size of 1
        And the field "severities.0.wordings.0.value" should be "foo"
        And the field "severities.0.wordings.0.key" should be "test"
        And the field "severities.0.color" should be null

    Scenario: We can create a severity with a color
        I fill in header "X-Customer-Id" with "5"
        When I post to "/severities" with:
        """
        {"wordings": [{"key": "test", "value": "foo"}], "color": "#123456"}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "severity.wordings.0.value" should be "foo"
        And the field "severity.wordings.0.key" should be "test"
        And the field "severity.color" should be "#123456"

    Scenario: We can create a severity with a priority
        I fill in header "X-Customer-Id" with "5"
        When I post to "/severities" with:
        """
        {"wordings": [{"key": "test", "value": "foo"}], "color": "#123456", "priority": 2, "effect": null}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "severity.wordings.0.value" should be "foo"
        And the field "severity.wordings.0.key" should be "test"
        And the field "severity.color" should be "#123456"
        And the field "severity.priority" should be "2"
        And the field "severity.effect" should be null
        When I get "/severities"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "severities" should have a size of 1
        And the field "severities.0.priority" should be "2"

    Scenario: We can't create a severity with any effect
        When I post to "/severities" with:
        """
        {"wordings": [{"key": "test", "value": "foo"}], "color": "#123456", "priority": 2, "effect": "foo"}
        """
        Then the status code should be "400"
        And the header "Content-Type" should be "application/json"

    Scenario: We can create a no_service severity
        I fill in header "X-Customer-Id" with "5"
        When I post to "/severities" with:
        """
        {"wordings": [{"key": "test", "value": "foo"}], "color": "#123456", "priority": 1, "effect": "no_service"}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "severity.wording" should be "foo"
        And the field "severity.color" should be "#123456"
        And the field "severity.priority" should be "1"
        And the field "severity.effect" should be "no_service"

    Scenario: We can create a reduced_service severity
        I fill in header "X-Customer-Id" with "5"
        When I post to "/severities" with:
        """
        {"wordings": [{"key": "test", "value": "foo"}], "color": "#123456", "priority": 2, "effect": "reduced_service"}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "severity.wording" should be "foo"
        And the field "severity.color" should be "#123456"
        And the field "severity.priority" should be "2"
        And the field "severity.effect" should be "reduced_service"

    Scenario: We can create a significant_delays severity
        I fill in header "X-Customer-Id" with "5"
        When I post to "/severities" with:
        """
        {"wordings": [{"key": "test", "value": "foo"}], "color": "#123456", "priority": 3, "effect": "significant_delays"}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "severity.wording" should be "foo"
        And the field "severity.color" should be "#123456"
        And the field "severity.priority" should be "3"
        And the field "severity.effect" should be "significant_delays"

    Scenario: We can create a detour severity
        I fill in header "X-Customer-Id" with "5"
        When I post to "/severities" with:
        """
        {"wordings": [{"key": "test", "value": "foo"}], "color": "#123456", "priority": 4, "effect": "detour"}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "severity.wording" should be "foo"
        And the field "severity.color" should be "#123456"
        And the field "severity.priority" should be "4"
        And the field "severity.effect" should be "detour"

    Scenario: We can create a additional_service severity
        I fill in header "X-Customer-Id" with "5"
        When I post to "/severities" with:
        """
        {"wordings": [{"key": "test", "value": "foo"}], "color": "#123456", "priority": 5, "effect": "additional_service"}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "severity.wording" should be "foo"
        And the field "severity.color" should be "#123456"
        And the field "severity.priority" should be "5"
        And the field "severity.effect" should be "additional_service"

    Scenario: We can create a modified_service severity
        I fill in header "X-Customer-Id" with "5"
        When I post to "/severities" with:
        """
        {"wordings": [{"key": "test", "value": "foo"}], "color": "#123456", "priority": 6, "effect": "modified_service"}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "severity.wording" should be "foo"
        And the field "severity.color" should be "#123456"
        And the field "severity.priority" should be "6"
        And the field "severity.effect" should be "modified_service"

    Scenario: We can create a other_effect severity
        I fill in header "X-Customer-Id" with "5"
        When I post to "/severities" with:
        """
        {"wordings": [{"key": "test", "value": "foo"}], "color": "#123456", "priority": 7, "effect": "other_effect"}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "severity.wording" should be "foo"
        And the field "severity.color" should be "#123456"
        And the field "severity.priority" should be "7"
        And the field "severity.effect" should be "other_effect"

    Scenario: We can create a unknown_effect severity
        I fill in header "X-Customer-Id" with "5"
        When I post to "/severities" with:
        """
        {"wordings": [{"key": "test", "value": "foo"}], "color": "#123456", "priority": 8, "effect": "unknown_effect"}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "severity.wording" should be "foo"
        And the field "severity.color" should be "#123456"
        And the field "severity.priority" should be "8"
        And the field "severity.effect" should be "unknown_effect"

    Scenario: We can create a stop_moved severity
        I fill in header "X-Customer-Id" with "5"
        When I post to "/severities" with:
        """
        {"wordings": [{"key": "test", "value": "foo"}], "color": "#123456", "priority": 9, "effect": "stop_moved"}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "severity.wording" should be "foo"
        And the field "severity.color" should be "#123456"
        And the field "severity.priority" should be "9"
        And the field "severity.effect" should be "stop_moved"