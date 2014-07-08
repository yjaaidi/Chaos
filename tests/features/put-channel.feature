Feature: channel can be deleted

    Scenario: modify of one channel
        Given I have the following channels in my database:
            | name   | max_size   | created_at          | updated_at          | content_type| id                                   |
            | short  | 140        | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | text/plain  | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |
            | email  | 520        | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | text/plain  | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |
        When I put "/channels/7ffab230-3d48-4eea-aa2c-22f8680230b6" with:
        """
        {"name": "foo", "max_size": 500, "content_type": "text/type"}
        """
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "channel.name" should be "foo"
        And the field "channel.max_size" should be 500
