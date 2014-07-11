Feature: channel can be deleted

    Scenario: list of two disruptions
        Given I have the following disruptions in my database:
            | reference | note  | created_at          | updated_at          | status    | id                                   |
            | foo       | hello | 2014-04-02T23:52:12 | 2014-04-02T23:55:12 | published | 7ffab230-3d48-4eea-aa2c-22f8680230b6 |
            | bar       | bye   | 2014-04-04T23:52:12 | 2014-04-06T22:52:12 | published | 7ffab232-3d48-4eea-aa2c-22f8680230b6 |

        When I get "/disruptions"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "disruptions" should have a size of 2
        And the field "disruptions.0.id" should be "7ffab230-3d48-4eea-aa2c-22f8680230b6"
        And the field "disruptions.1.id" should be "7ffab232-3d48-4eea-aa2c-22f8680230b6"

        When I delete "/disruptions/7ffab230-3d48-4eea-aa2c-22f8680230b6"
        Then the status code should be "204"


        When I get "/disruptions"
        Then the status code should be "200"
        And the header "Content-Type" should be "application/json"
        And the field "disruptions" should have a size of 1
        And the field "disruptions.0.id" should be "7ffab232-3d48-4eea-aa2c-22f8680230b6"