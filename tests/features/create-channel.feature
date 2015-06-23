Feature: Create Channel

    Scenario: we cannot create channel without client
        When I post to "/channels" with:
        """
        {"name": "foo", "max_size": 500, "content_type": "text/type"}
        """
        Then the status code should be "400"

    Scenario: we cannot create channel without channel type
        I fill in header "X-Customer-Id" with "5"
        When I post to "/channels" with:
        """
        {"name": "foo", "max_size": 500, "content_type": "text/type"}
        """
        Then the status code should be "400"

    Scenario: creation of channel
        I fill in header "X-Customer-Id" with "5"
        When I post to "/channels" with:
        """
        {"name": "foo", "max_size": 500, "content_type": "text/type", "types": ["web","mobile"]}
        """
        Then the status code should be "201"
        And the header "Content-Type" should be "application/json"
        And the field "channel.name" should be "foo"
        And the field "channel.max_size" should be 500
        And the field "channel.types.0" should be "web"

    Scenario: We can't create a channel without name, max_size and
        I fill in header "X-Customer-Id" with "5"
        When I post to "/channels" with:
        """
        {"name": "foo", "max_size": 500}
        """
        Then the status code should be "400"
        And the header "Content-Type" should be "application/json"

    Scenario: creation of channel with duplicate types fails
        I fill in header "X-Customer-Id" with "5"
        When I post to "/channels" with:
        """
        {"name": "foo", "max_size": 500, "content_type": "text/type", "types": ["mobile", "mobile"}]}
        """
        Then the status code should be "400"

    #channel_type_values = ["web", "sms", "email", "mobile", "notification", "twitter", "facebook"]
    Scenario: creation of channel with wrong types fails
        I fill in header "X-Customer-Id" with "5"
        When I post to "/channels" with:
        """
        {"name": "foo", "max_size": 500, "content_type": "text/type", "types": ["mail"]}
        """
        Then the status code should be "400"
