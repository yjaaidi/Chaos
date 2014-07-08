Feature: list channel

    Scenario: if there is no channel the list is empty
        When I get "/channels"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        and "channels" should be empty

    Scenario: list of two channels
        Given I have the following channels in my database:
            | name   | max_size   | created_at          | updated_at          | content_type| id                                   |
            | short  | 140        | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | text/plain  | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |
            | email  | 520        | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | text/plain  | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |
        When I get "/channels"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "channels" should have a size of 2
        And the field "channels.0.name" should be "short"
        And the field "channels.0.max_size" should be 140
        And the field "channels.0.content_type" should be "text/plain"

    Scenario: I have a 400 if the id doesn't have the correct format
            Given I have the following channels in my database:
            | name   | max_size   | created_at          | updated_at          | content_type| id                                   |
            | short  | 140        | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | text/plain  | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |
            | email  | 520        | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | text/plain  | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |
        When I get "/channels/7ffab230-3d48a-a2c-22f8680230b6"
        Then the status code should be "400"

